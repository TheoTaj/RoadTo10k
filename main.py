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
import scooore

# don't forget to : export DISPLAY=:0 on wsl !!

def get_all_arbs():
    
    start = t.time()
    arb.arb_ligue1()
    end = t.time()
    print("Time for ligue1: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_liga()
    end = t.time()
    print("Time for liga: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_bundesliga()
    end = t.time()
    print("Time for bundesliga: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_premier_league()
    end = t.time()
    print("Time for premier league: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_serie_a()
    end = t.time()
    print("Time for serie a: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_primeira()
    end = t.time()
    print("Time for primeira: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_a_league()
    end = t.time()
    print("Time for a league: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_bundesliga_austria()
    end = t.time()
    print("Time for bundesliga austria: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_division_1a()
    end = t.time()
    print("Time for division 1a: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_super_lig()
    end = t.time()
    print("Time for super lig: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_champions_league()
    end = t.time()
    print("Time for champions league: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_europa_league()
    end = t.time()
    print("Time for europa league: ", round(end - start, 2), " s")
    print()

    start = t.time()
    arb.arb_conference_league()
    end = t.time()
    print("Time for conference league: ", round(end - start, 2), " s")
    print()

    


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
# arb.arb_ligue1()
# end = t.time()
# print("Time for ligue1: ", round(end - start, 2), " s")
# print()

#_________________________________________________________________________________________




while True:
    startTotal = t.time()
    get_all_arbs()
    endTotal = t.time()
    delta = round(endTotal - startTotal, 2)
    print("Total time: ", delta, " s")

    time.sleep(3600 - delta)