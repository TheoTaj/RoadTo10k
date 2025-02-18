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
        "ligue1": "https://www.betcenter.be/fr/football/france-ligue-1",
        "liga": "https://www.betcenter.be/fr/football/espagne-laliga",
        "bundesliga": "https://www.betcenter.be/fr/allemagne-bundesliga", 
        "premier-league": "https://www.betcenter.be/fr/angleterre-premier-league",
        "serie-a": "https://www.betcenter.be/fr/football/italie-serie-a",
        "primeira": "https://www.betcenter.be/fr/football/portugal-primeira-liga",
        "a-league": "https://www.betcenter.be/fr/football/australie-a-league",
        "bundesliga-austria": "https://www.betcenter.be/fr/football/autriche-bundesliga",
        "division-1a": "https://www.betcenter.be/fr/football/belgique-pro-league",
        "super-lig": "https://www.betcenter.be/fr/football/turquie-super-lig",
        "champions-league": "https://www.betcenter.be/fr/football/ligue-des-champions-de-l-uefa",
        "europa-league": "https://www.betcenter.be/fr/ligue-europa"
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
        print("URL not found")
        return None

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(10)

    return driver

def get_games(competition):
    driver = get_page(competition)
    games = []

    if driver is None:
        print("Driver is none")
        return []

    try:
        elements1 = driver.find_elements(By.CLASS_NAME, "game-header--names")
        elements2 = driver.find_elements(By.CLASS_NAME, "market-list__markets")
    except:
        print("Erreur lors de la récupération des données")
        return []

    size = min(len(elements1), len(elements2))
    # print("len elements1: ", len(elements1))
    # print("len elements2: ", len(elements2))
   
    for i in range(size):
        # print("itération")
        split1 = elements1[i].text.split("\n")
        if len(split1) < 2:
            print("in continue1")
            continue
        team1 = split1[0]
        team2 = split1[1]

        split2 = elements2[i].text.split("\n")
        if len(split2) < 6:
            # print("in continue2")
            continue
        try:
            a = float(split2[1])
            b = float(split2[3])
            c = float(split2[5])
        except:
            print("in exception")
            continue

        games.append((team1, team2, [a, b, c]))


    return games