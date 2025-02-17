import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


competition_urls = {
    'football':
    {
        "ligue1": "https://www.ladbrokes.be/fr/sports/#!/calcio/fr-ligue-1/",
        "liga": "https://www.ladbrokes.be/fr/sports/#!/calcio/es-liga/",
        "bundesliga": "https://www.ladbrokes.be/fr/sports/#!/calcio/de-bundesliga/",
        "premier-league": "https://www.ladbrokes.be/fr/sports/#!/calcio/ing-premier-league/",
        "serie-a": "https://www.ladbrokes.be/fr/sports/#!/calcio/it-serie-a/",
        "primeira": "https://www.ladbrokes.be/fr/sports/#!/calcio/pt-primeira-liga/",
        "a-league": "https://www.ladbrokes.be/fr/sports/#!/calcio/au-a-league/",
        "bundesliga-austria": "https://www.ladbrokes.be/fr/sports/#!/calcio/at-bundesliga/",
        "division-1a": "https://www.ladbrokes.be/fr/sports/#!/calcio/be-jupiler-pro-league1/",
        "super-lig": "https://www.ladbrokes.be/fr/sports/#!/calcio/tr-super-lig/"
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
    service = Service("/home/pi/my_env/bin/chromedriver")
    driver = webdriver.Chrome(service = service, options=chrome_options)
    driver.get(url)
    time.sleep(15)

    return driver

def get_games(competition):
    driver = get_page(competition)
    games = []

    if driver is None:
        return []
    
    try:
        elements1 = driver.find_elements(By.CLASS_NAME, "event-players")
        elements2 = driver.find_elements(By.CLASS_NAME, "group-quote-new")

    except:
        print("Erreur lors de la récupération des données")
        return []

    size = len(elements1)

    for i in range(size):
        split1 = elements1[i].text.split("\n")
        team1 = split1[0]
        team2 = split1[1]

        split2 = elements2[i].text.split("\n")
        try:
            a = float(split2[0])
            b = float(split2[1])
            c = float(split2[2])
        except:
            continue
        games.append((team1, team2, [a, b, c]))


    return games