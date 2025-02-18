from bs4 import BeautifulSoup
import requests
import time

competition_urls = {
	'football':
	{
		"ligue1": "https://www.zebet.be/fr/competition/96-ligue_1",
		"liga": "https://www.zebet.be/fr/competition/306-laliga",
		"bundesliga": "https://www.zebet.be/fr/competition/268-bundesliga",
		"premier-league": "https://www.zebet.be/fr/competition/94-premier_league",
		"serie-a": "https://www.zebet.be/fr/competition/305-serie_a",
		"primeira": "https://www.zebet.be/fr/competition/154-portugal_liga",
		"a-league": "https://www.zebet.be/fr/competition/2169-australie_a_league",
		"bundesliga-austria": "https://www.zebet.be/fr/competition/131-autriche_bundesliga",
		"division-1a": "https://www.zebet.be/fr/competition/101-belgique_jupiler_pro_league",
		"super-lig": "https://www.zebet.be/fr/competition/254-turquie_super_lig",
		"champions-league": "https://www.zebet.be/fr/competition/6674-ligue_des_champions"
	},
	'basketball':
	{
		"nba": "https://www.zebet.be/fr/competition/206-nba",
		"euroleague": "https://www.zebet.be/fr/competition/12044-euroleague",
	}
}

def get_page(competition):
	if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
		url = competition_urls[competition["sport"]][competition["competition"]]
	else:
		return None
	response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"})
	html = BeautifulSoup(response.content, 'html.parser')
	time.sleep(3)
	return html

def get_games(competition):
	html = get_page(competition)
	games = []
	game_elements = html.select(".pari-1")
	for el in game_elements:
		names = el.select(".pmq-cote-acteur")
		team1 = "".join(names[0].text.split())
		if (competition["sport"] == "football"):
			team2 = "".join(names[4].text.split())
		elif (competition["sport"] == "basketball"):
			team2 = "".join(names[2].text.split())
		odd_els = el.select(".pmq-cote")
		odds = []
		for odd_el in odd_els[::2]:
			odds.append(float(odd_el.text.replace(",", ".")))
		games.append((
			team1, 
			team2,
			odds
		))
	return games