from bs4 import BeautifulSoup
import time as t
import pmu
import zebet
import arb
import requests
import betfirst
import ladbrokes
import bwin
import log
import napoleon

# don't forget to : export DISPLAY=:0 on wsl !!

def get_all_arbs():
    startTotal = t.time()
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

    endTotal = t.time()
    print("Total time: ", round(endTotal - startTotal, 2), " s")




# sim1 = arb.str_similarity("Genoa", "Genoa CFC")
# print("sim1: ", sim1)

# sim2 = arb.str_similarity("Venise", "Venezia")
# print("sim2: ", sim2)

# sim3 = arb.str_similarity("Betis Séville", "RealBetis")
# print("sim3: ", sim3)

# betfirstGames = [('RedBullSalzbourg', 'WSGTirol', [1.23, 5.1, 8.25])]
# bwinGames = [('RedBullSalzbourg', 'WSGTirol', [8, 5.1, 1])]

# bookies = []

# bookies.append(("betfirst", betfirstGames))
# bookies.append(("bwin", bwinGames))

# arb.get_arbs(bookies)

# games = napoleon.get_games({"sport": "football", "competition": "liga"})
# print(games)

start = t.time()
arb.arb_serie_a()
end = t.time()
print("Time for seria: ", round(end - start, 2), " s")
print()
