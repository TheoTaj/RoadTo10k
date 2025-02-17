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
        "ligue1": "https://napoleonsports.be/fr-be/sport-bets/football/france/ligue-1/all",
        "liga": "https://napoleonsports.be/fr-be/sport-bets/football/spain/laliga/all",
        "bundesliga": "https://napoleonsports.be/fr-be/sport-bets/football/germany/bundesliga/all?ct=m",
        "premier-league": "https://napoleonsports.be/fr-be/sport-bets/football/england/premier-league/all",
        "serie-a": "https://napoleonsports.be/fr-be/sport-bets/football/italy/serie-a/all",
        "primeira": "https://napoleonsports.be/fr-be/sport-bets/football/portugal/primeira-liga/all",
        "a-league": "https://napoleonsports.be/fr-be/sport-bets/football/australia/a-league/all",
        "bundesliga-austria": "https://napoleonsports.be/fr-be/sport-bets/football/austria/bundesliga/all",
        "division-1a": "https://napoleonsports.be/fr-be/sport-bets/football/belgium/jupiler-pro-league/all",
        "super-lig": "https://napoleonsports.be/fr-be/sport-bets/football/turkey/super-lig/all"
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
        try :
            a = float(split2[1])
            b = float(split2[4])
            c = float(split2[7])
        except:
            continue
        games.append((
            team1,
            team2,
            [a, b, c]
        ))


    driver.quit()
    return games
