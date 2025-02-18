import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service



competition_urls = {
    'football':
    {
        "ligue1": "https://www.scooore.be/fr/sports/sports-hub/football/france/ligue_1",
        "liga": "https://www.scooore.be/fr/sports/sports-hub/football/spain/la_liga",
        "bundesliga": "https://www.scooore.be/fr/sports/sports-hub/football/germany/bundesliga",
        "premier-league": "https://www.scooore.be/fr/sports/sports-hub/football/england/premier_league",
        "serie-a": "https://www.scooore.be/fr/sports/sports-hub/football/italy/serie_a",
        "primeira": "https://www.scooore.be/fr/sports/sports-hub/football/portugal/primeira_liga",
        "a-league": "https://www.scooore.be/fr/sports/sports-hub/football/australia/a-league",
        "bundesliga-austria": "https://www.scooore.be/fr/sports/sports-hub/football/austria/bundesliga",
        "division-1a": "https://www.scooore.be/fr/sports/sports-hub/football/belgium/jupiler_pro_league",
        "super-lig": "https://www.scooore.be/fr/sports/sports-hub/football/turkey/super_lig",
        "champions-league": "https://www.scooore.be/fr/sports/sports-hub/football/champions_league",
        "europa-league": "https://www.scooore.be/fr/sports/sports-hub/football/europa_league",
        "europa-conference": "https://www.scooore.be/fr/sports/sports-hub/football/conference_league"
	},
    'basketball':
    {
        "nba": "https://betfirst.dhnet.be/basket/%C3%A9tats-unis-nba/",
		"euroleague": "https://betfirst.dhnet.be/basket/europe-euroligue/"
    }

}



def get_page(competition):
    if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
        url = competition_urls[competition["sport"]][competition["competition"]]
    else:
        return None
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Active le mode headless
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)

    return driver  # Retourne le driver pour pouvoir interagir avec la page
    
def get_games(competition):
    driver = get_page(competition)
    games = []

    if driver is None:
        print("scooore, driver is None")
        return []
    
    try:
        elements1 = driver.find_elements(By.CLASS_NAME, "KambiBC-sandwich-filter__event-list-item")
    except:
        print("Erreur lors de la récupération des données")
        return []

    for el in elements1:
        split = el.text.split("\n")

        if len(split) < 8:
            continue

        team1 = split[2]
        team2 = split[3]

        try:
            a = float(split[5])
            b = float(split[6])
            c = float(split[7])
        except:
            continue

        games.append((team1, team2, [a, b, c]))

    driver.quit()
    return games

