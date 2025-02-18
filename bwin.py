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
        "ligue1": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/france-16/ligue-1-102843",
        "liga": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/espagne-28/laliga-102829",
        "bundesliga": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/allemagne-17/bundesliga-102842",
        "premier-league": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/angleterre-14/premier-league-102841",
        "serie-a": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/italie-20/serie-a-102846",
        "primeira": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/portugal-37/primeira-liga-102851",
        "a-league": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/australie-60/a-league-2068",
        "bundesliga-austria": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/autriche-8/bundesliga-102835",
        "division-1a": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/belgique-35/jupiler-pro-league-0:12",
        "super-lig": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/turquie-31/s%C3%BCper-lig-102832",
        "champions-league": "https://www.bwin.be/en/sports/football-4/betting/europe-7/uefa-champions-league-0:3",
        "europa-league": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/europe-7/europa-league-0:5",
        "europa-conference": "https://www.bwin.be/fr/sports/football-4/paris-sportifs/europe-7/conference-league-0:9"
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
    
    for i in range(4):
        try:
            elements1 = driver.find_elements(By.CLASS_NAME, "participants-pair-game")
            elements2 = driver.find_elements(By.CLASS_NAME, "grid-group-container")

        except:
            print("Erreur lors de la récupération des données")
            continue

        size = min(len(elements1), len(elements2))

        for i in range(size):
            split1 = elements1[i].text.split("\n")
            if len(split1) < 2:
                continue
            team1 = split1[0]
            team2 = split1[1]

            split2 = elements2[i + 1].text.split("\n")

            if len(split2) < 3:
                continue

            try:
                a = float(split2[0])
                b = float(split2[1])
                c = float(split2[2])
            except:
                continue


            #vérifier si le tuple n'est pas déjà dans la liste, attention ne vérifier que les noms d'équipes car les odds peuvent changer.
            # Si le tuple y est déjà on écrase l'ancien tuple par le nouveau, sinon on ajoute le nouveau tuple
            tuple = (team1, team2, [a, b, c])

            sizeGames = len(games)
            inserted = False
            for i in range(sizeGames):
                t = games[i]
                if t[0] == team1 and t[1] == team2:
                    games[i] = tuple
                    inserted = True
                    break
            
            if inserted == False:
                games.append(tuple)

        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1) 

    driver.quit()
    return games
