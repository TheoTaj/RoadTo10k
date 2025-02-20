from bs4 import BeautifulSoup
import time as t
import zebet
import arb
import requests
import betfirst
import ladbrokes
import bwin
import log
import napoleon
import unibet
import betcenter
import circus
import scooore
from datetime import datetime


# don't forget to : export DISPLAY=:0 on wsl !!

def get_all_arbs():
    
    message = ""
    startTotal = t.time()

    start = t.time()
    message += arb.arb_premier_league()
    end = t.time()
    message += "Time for premier league " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_ligue1()
    end = t.time()
    message += "Time for ligue1 " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_liga()
    end = t.time()
    message += "Time for liga " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_bundesliga()
    end = t.time()
    message += "Time for bundesliga " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_serie_a()
    end = t.time()
    message += "Time for serie a " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_primeira()
    end = t.time()
    message += "Time for primeira " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_a_league()
    end = t.time()
    message += "Time for a league " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_bundesliga_austria()
    end = t.time()
    message += "Time for bundesliga austria " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_division_1a()
    end = t.time()
    message += "Time for division 1a " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_super_lig()
    end = t.time()
    message += "Time for super lig " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_champions_league()
    end = t.time()
    message += "Time for champions league " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    message += arb.arb_europa_league()
    end = t.time()
    message += "Time for europa league " + str(round(end - start, 2)) + " s\n"

    start = t.time()
    messagae += arb.arb_conference_league()
    end = t.time()
    message += "Time for conference league " + str(round(end - start, 2)) + " s\n"

    endTotal = t.time()
    message += "Total time: " + str(round(endTotal - startTotal, 2)) + " s\n"

    return message

#_________________________________________________________________________________________
# similarity test:

# sim2 = arb.str_similarity("Royale Union SG", "Union Saint-Gilloise")
# print("sim2: ", sim2)

# sim3 = arb.str_similarity("Betis Séville", "RealBetis")
# print("sim3: ", sim3)

#_________________________________________________________________________________________

# single bookmaker test:

# games = scooore.get_games({"sport": "football", "competition": "ligue1"})
# print(games)

#_________________________________________________________________________________________

# single league test w all bookmakers:

# start = t.time()
# arb.arb_conference_league()
# end = t.time()
# print("Time for ligue1: ", round(end - start, 2), " s")
# print()

#_________________________________________________________________________________________


message = get_all_arbs()
now = datetime.now()
date_heure = now.strftime("%Y-%m-%d %H:%M:%S")
message += date_heure
with open("message.txt", "w") as file:
    file.write(message)

log.send_file_to_discord("message.txt", message="Details de " + date_heure + " :")

