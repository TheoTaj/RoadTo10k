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
        "ligue1": "https://betfirst.dhnet.be/football/france-ligue-1/",
        "liga": "https://betfirst.dhnet.be/football/espagne-la-liga/",
        "bundesliga": "https://betfirst.dhnet.be/football/allemagne-1-bundesliga/",
        "premier-league": "https://betfirst.dhnet.be/football/angleterre-premier-league/",
        "serie-a": "https://betfirst.dhnet.be/football/italie-serie-a/",
        "primeira": "https://betfirst.dhnet.be/football/portugal-primeira-liga/",
        "a-league": "https://betfirst.dhnet.be/football/australie-league-a/",
        "bundesliga-austria": "https://betfirst.dhnet.be/football/autriche-bundesliga/",
        "division-1a": "https://betfirst.dhnet.be/football/belgique-jupiler-pro-league/",
        "super-lig": "https://betfirst.dhnet.be/football/turquie-super-lig/",
        "champions-league": "https://betfirst.dhnet.be/football/europe-ligue-des-champions/"
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
        print("Betfirst, driver is None")
        return []

    for i in range(5):
        try:
            elements = driver.find_elements(By.CLASS_NAME, "rj-ev-list__ev-card")
        except:
            print("Erreur lors de la récupération des données")
            continue        
            
        for el in elements:
            try:
                j = el.find_elements(By.CLASS_NAME, "rj-ev-list__bet-btn__content")
            except:
                continue
            
            if len(j) < 6:
                continue

            team1 = j[0].text
            team2 = j[4].text

            try:
                a = float(j[1].text)
                b = float(j[3].text)
                c = float(j[5].text)
            except:
                continue

            odds = [a, b, c]
            tuple = (team1, team2, odds)

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


