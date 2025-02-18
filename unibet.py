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
        "ligue1": "https://fr.unibetsports.be/betting/sports/filter/football/france/ligue_1/all/matches",
        "liga": "https://fr.unibetsports.be/betting/sports/filter/football/spain/la_liga/all/matches",
        "bundesliga": "https://fr.unibetsports.be/betting/sports/filter/football/germany/bundesliga/all/matches",
        "premier-league": "https://fr.unibetsports.be/betting/sports/filter/football/england/premier_league/all/matches",
        "serie-a": "https://fr.unibetsports.be/betting/sports/filter/football/italy/serie_a/all/matches",
        "primeira": "https://fr.unibetsports.be/betting/sports/filter/football/portugal/primeira_liga/all/matches",
        "a-league": "https://fr.unibetsports.be/betting/sports/filter/football/australia/a-league/all/matches",
        "bundesliga-austria": "https://fr.unibetsports.be/betting/sports/filter/football/austria/bundesliga/all/matches",
        "division-1a": "https://fr.unibetsports.be/betting/sports/filter/football/belgium/jupiler_pro_league/all/matches",
        "super-lig": "https://fr.unibetsports.be/betting/sports/filter/football/turkey/super_lig/all/matches",
        "champions-league": "https://fr.unibetsports.be/betting/sports/filter/football/champions_league/all/matches",
        "europa-league": "https://fr.unibetsports.be/betting/sports/filter/football/europa_league/all/matches",
        "europa-conference": "https://fr.unibetsports.be/betting/sports/filter/football/conference_league/all/matches"
	},
    'basketball':
    {
        "nba": "https://fr.unibetsports.be/betting/sports/filter/basketball/nba/all/matches",
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
    # service = Service("/home/pi/my_env/bin/chromedriver")
    # driver = webdriver.Chrome(service = service, options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)

    return driver

def get_games(competition):
    driver = get_page(competition)
    games = []

    if driver is None:
        print("Driver is none")
        return []

    try:
        elements1 = driver.find_elements(By.CLASS_NAME, "_1dfe7")
        elements2 = driver.find_elements(By.CLASS_NAME, "bb419")
    except:
        print("Erreur lors de la récupération des données")
        return []

    diff = abs(len(elements1) - len(elements2))

    for i in range(min(len(elements1), len(elements2))):
        split1 = elements1[i + diff].text.split("\n")
        split2 = elements2[i].text.split("\n")

        team1 = split1[0]
        team2 = split1[1]
        try:
            a = float(split2[0])
            b = float(split2[1])
            c = float(split2[2])
        except:
            continue
        
        games.append((team1, team2, [a, b, c]))
    
    return games

def get_basket(competition):
    driver = get_page(competition)
    games = []

    if driver is None:
        print("Driver is none")
        return []

    try:
        elements1 = driver.find_elements(By.CLASS_NAME, "_1dfe7")
        elements2 = driver.find_elements(By.CLASS_NAME, "bb419")
    except:
        print("Erreur lors de la récupération des données")
        return []

    diff = abs(len(elements1) - len(elements2))

    for i in range(min(len(elements1), len(elements2))):
        split1 = elements1[i + diff].text.split("\n")
        split2 = elements2[i].text.split("\n")

        team1 = split1[0]
        team2 = split1[1]
        try:
            a = float(split2[0])
            b = float(split2[1])
        except:
            continue
        
        games.append((team1, team2, [a, b]))
    
    return games
