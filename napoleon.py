import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

competition_urls = {
    'football':
    {
        "ligue1": "https://napoleonsports.be/fr-be/sport-bets/football/france/ligue-1/all",
        "liga": "https://napoleonsports.be/fr-be/sport-bets/football/spain/laliga/all",
        "bundesliga": "https://napoleonsports.be/fr-be/sport-bets/football/germany/bundesliga/all?ct=m",
        "premier-league": "https://napoleonsports.be/fr-be/sport-bets/football/england/premier-league/all",
        "serie-a": "https://napoleonsports.be/fr-be/sport-bets/football/italy/serie-a/all",
        "primeira": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/portugal-37/primeira-liga-102851",
        "a-league": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/australie-60/a-league-2068",
        "bundesliga-austria": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/autriche-8/bundesliga-102835",
        "division-1a": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/belgique-35/jupiler-pro-league-0:12",
        "super-lig": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/turquie-31/s%C3%BCper-lig-102832"
	},
    'basketball':
    {
        "nba": "https://www.ladbrokes.be/fr/sports/#!/basket/us-nba/",
		"euroleague": "https://www.ladbrokes.be/fr/sports/#!/basket/eu-eurolega/"
    }

}

def get_page(competition):
    if(competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
        url = competition_urls[competition["sport"]][competition["competition"]]
    else:
        return None

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)

    return driver

def get_games(competition):
    driver = get_page(competition)
    games = []

    if driver is None:
        return []

    try:
        elements1 = driver.find_elements(By.CLASS_NAME, "event__sections") 
        elements2 = driver.find_elements(By.CLASS_NAME, "odd-offer__odd-buttons-wrapper")
    
    except:
        print("Erreur lors de la récupération des données")
        return []

    size = min(len(elements1), len(elements2))
    for i in range(size):
        split1 = elements1[i].text.split("\n")
        if len(split1) < 2:
            continue

        team1 = split1[0]
        team2 = split1[1]

        split2 = elements2[i].text.split("\n")
        if len(split2) < 8:
            continue
        
        a = float(split2[1])
        b = float(split2[4])
        c = float(split2[7])

        games.append((
            team1,
            team2,
            [a, b, c]
        ))


    driver.quit()
    return games
