from difflib import SequenceMatcher
import logging as log
import zebet
import betfirst
import ladbrokes
import bwin
import log
import napoleon
import unibet
import betcenter
import circus
import scooore


mismatch_ligue1 = [["Brest", "Stade Brestois"], ["Olympique Marseille", "Marseille"], ["ParisSG", "Paris Saint-Germain"], ["ParisSG", "PSG"], ["Lyon", "Olympique Lyonnais"],
    ["Reims", "Stade Reims"], ["Lens", "RC Lens"], ["Nice", "OGC Nice"], ["Rennes", "Stade Rennais"], ["Olympique Lyon", "Lyon"], ["PSG", "Paris SG"], ["Lyon", "Olympique Lyon"]]

mismatch_liga = [["Girona FC", "FC Gerone"], ["Girona FC", "Gérone"], ["Deportivo Alaves", "Alavés"], ["Deportivo Alaves", "Alaves"], ["DeportivoAlavés", "Alaves"], ["DeportivoAlavés", "Alavés"],
    ["Atlético Madrid", "Atlético"], ["Espanyol Barcelone", "Espanyol"], ["Athletic Bilbao", "Bilbao"], ["Betis Séville", "Real Betis Balompie"], ["Betis Séville", "Betis"], 
    ["Betis Séville", "RealBetis"], ["Mallorca", "Majorque"], ["Mallorca", "RealMajorque"], ["FC Gerone", "Girona"], ["FC Gerone", "GironaFC"]]

mismatch_bundesliga = [["Borussia M'Gladbach", "M'gladbach"], ["Borussia Monchengladbach", "M'gladbach"], ["FC St. Pauli", "Sankt-Pauli"], ["St. Pauli","Sankt-Pauli"], ["Borussia Dortmund", "Dortmund"], ["Bayern", "Bayern Munich"], ["Bayern", "BayernMunich"], ["Werder Breme", "Werder"],
    ["Werder", "WerderBrême"], ["Eintracht", "Eintracht Francfort"], ["Eintracht", "EintrachtFrancfort"], ["Kiel", "Holstein Kiel"], ["Kiel", "HolsteinKiel"],
    ["Heidenheim", "1. FC Heidenheim 1846"], ["Heidenheim", "FCHeidenheim1846"], ["Mainz 05", "Mayence"], ["Mainz 05", "FSV Mayence"], ["FSV Mainz 05", "Mayence"]]

mismatch_premier_league = [ 
    ["Brighton", "Brighton & Hove Albion FC"], ["Leicester City FC", "Leicester"], ["WestHam", "West Ham United FC"],
    ["West Ham", "West Ham United FC"], ["ManchesterUnited", "Man United"], ["Manchester United FC", "Man United"], ["Tottenham", "Tottenham Hotspur FC"],
    ["Wolverhampton", "Wolves"], ["Wolverhampton", "Wolverhampton Wanderers FC"], ["Wolverhampton Wanderers FC", "Wolves"], ["Newcastle", "Newcastle United FC"],
    ["Manchester City FC", "Man City"], ["ManchesterCity", "Man City"]]

mismatch_serie_a = [["Cagliari", "Cagliari Calcio"], ["AtalantaBergame", "Atalanta"], ["Atalanta Bergame", "Atalanta"],
    ["Hellas", "HellasVerone"], ["Hellas", "Hellas Vérone"], ["Hellas", "Hellas Verone"], ["Como 1907", "Come"], ["Como", "Como 1907"], ["Côme", "Como 1907"],
    ["Udinese", "Udinese Calcio"], ["Monza Brianza", "ACMonza"], ["Monza Brianza", "AC Monza"], ["Monza Brianza", "Monza"], ["Parme Calcio", "ParmeFC"], ["Parme Calcio", "Parme"],
    ["Inter", "InterMilan"], ["Inter", "Inter Milan"], ["Venise", "Venezia"]]

mismatch_primeria = [["Sporting Braga", "Braga"], ["Sporting Braga", "SC Braga"], ["AVS", "AvsFutebolSad"], ["AVS", "AVS Futebol SAD"], ["AVS", "Avs Futebol Sad"], ["AVS", "AVS Futebol"]]

mismatch_a_league = []

mismatch_bundesliga_austria = [["WolfsbergerAC", "RZ Pellets WAC"], ["WolfsbergerAC", "WAC"], ["BW Linz", "FCBlauWeissLinz"], ["WSG Tirol", "WSG Swarovski Tirol"], ["Wolfsberger AC", "RZ Pellets WAC"]]

mismatch_division_1a = [["Oud-HeverleeLeuven", "Louvain"], ["Oud-Heverlee Leuven", "OHL"], ["OHL", "Louvain"], ["Oud-HeverleeLeuven", "OHL"], ["Oud-Heverlee Leuven", "Louvain"],
    ["Anvers", "RoyalAntwerpFC"], ["Anvers", "Antwerp"], ["Anvers", "Royal Antwerp"], ["St.TruidenseVV", "Saint-Trond"], ["UnionSaint-Gilloise", "Union SG"], ["Union SG", "Union Saint-Gilloise"],
    ["FCBruges", "Club Brugge KV"], ["Club Brugge KV", "FC Bruges"], ["Club Brugge KV", "Bruges"], ["AA Gent", "LaGantoise"], ["AA Gent", "La Gantoise"], ["Royale Union SG", "UnionSaint-Gilloise"],
    ["Royale Union SG", "Union Saint-Gilloise"], ["KV Mechelen", "FCMalines"], ["KV Mechelen", "Malines"], ["KV Mechelen", "FC Malines"], ["Saint-Trond", "St.TruidenseVV"], ["Saint-Trond", "Sint Truidense VV"],
    ["Oud-Heverlee Leuven", "OH Louvain"]]

mismatch_super_lig = []

dismatch = [["Linzer ASK", "Grazer AK"], ["Western Sydney", "WesternUnitedFC"], ["Sivasspor", "Rizespor"], ["Konyaspor Club", "Alanyaspor"]]


# renvoie la similarité entre deux chaines de caractères
def str_similarity(a, b):
	return SequenceMatcher(None, a, b).ratio()


#game corrsepond à une game du casino 1, others contient toutes les games du casino 2
def get_game(game, others, mismatch_pairs):
    if not others or game is None:
        return None

    m = 0
    m_obj = None

    for other in others:
        sim = str_similarity(game[0], other[0]) + str_similarity(game[1], other[1])
        if sim > m:
            m = sim
            m_obj = other

    if m_obj is None:
        # print("No match found for " + game[0] + " vs " + game[1])
        return None

    sim1 = None
    sim2 = None
    if str_similarity(game[0], m_obj[0]) >= 0.55:
        sim1 = True
    if str_similarity(game[1], m_obj[1]) >= 0.55:
        sim2 = True

    
    for mismatch in mismatch_pairs:
        if sim1 is None:
            if [game[0], m_obj[0]] == mismatch or [m_obj[0], game[0]] == mismatch:
                sim1 = True

        if sim2 is None:
            if [game[1], m_obj[1]] == mismatch or [m_obj[1], game[1]] == mismatch:
                sim2 = True

    for dis in dismatch:
        if sim1 is True:
            if [game[0], m_obj[0]] == dis or [m_obj[0], game[0]] == dis:
                sim1 = None
        
        if sim2 is True:
            if [game[1], m_obj[1]] == dis or [m_obj[1], game[1]] == dis:
                sim2 = None
        

    if sim1 is None or sim2 is None:
        return None

    return m_obj

#max_odds contient des tuples qui contiennent le nom du casino et sa cote
def get_opti_bet(max_odds, res):
    T = 100
    Ma = T/(max_odds[0][1] * res)
    Mb = T/(max_odds[1][1] * res)
    Mc = T/(max_odds[2][1] * res)
    return [Ma, Mb, Mc]
    



# ici game est un tuple qui contient le nom du casino et la partie du casino 
# others est un tableau qui contient des tuples qui contiennent le nom du casino et la partie du casino
def get_max_odds(game, others):
    nb_bookies = len(others)
    if nb_bookies == 0:
        return None

    a = game[1][2][0]
    b = game[1][2][1]
    c = game[1][2][2]
    oa = [game[0], a]
    ob = [game[0], b]
    oc = [game[0], c]

    for other in others:
        if other is None:
            continue
        if other[1][2][0] > oa[1]:
            oa[0] = other[0]
            oa[1] = other[1][2][0]
        if other[1][2][1] > ob[1]:
            ob[0] = other[0]
            ob[1] = other[1][2][1]
        if other[1][2][2] > oc[1]:
            oc[0] = other[0]
            oc[1] = other[1][2][2]

    return [oa, ob, oc]


#bookies est un tableau qui contient à chaque case un tuple contenant le nom du casino et les games
def get_arbs(bookies, mismatch_pairs):
    nb_bookies = len(bookies)
    if nb_bookies <= 1:
        return []


    gamesOfBookie0 = bookies[0][1]
    nameOfBookie0 = bookies[0][0]
    message = ""
    for game in gamesOfBookie0:
        
        # others doit contenir des tuples qui contiennent le nom du casino et la partie du casino
        others = []
        compteur = 0
        for i in range(1, nb_bookies):
            tuple_info = (bookies[i][0], get_game(game, bookies[i][1], mismatch_pairs))
           
            if tuple_info[1] is not None:
                others.append(tuple_info)

        if not others:
            message += f"No match found for {game[0]} vs {game[1]}\n"
            continue
        message += f"len of others {len(others)}\n"
        message += f"others {others}\n"

        max_odds = get_max_odds((nameOfBookie0, game), others)
        if max_odds is None:
            continue

        a = max_odds[0][1]
        b = max_odds[1][1]
        c = max_odds[2][1]
        res = 1/a + 1/b + 1/c
        if (res) < 1:
            taux = (1 - res) * 100 + 100
            opti_bet = get_opti_bet(max_odds, res)
            text = "Arbitrage trouvé " + str(round(taux, 2)) + "%\n" + "Match: " + game[0] + " vs " + game[1] + "\n" + "Odds a = " + str(round(a, 2)) + " chez " + max_odds[0][0] + " Mise = " + str(round(opti_bet[0], 2)) + "%\n" + "Odds b = " + str(b) + " chez " + max_odds[1][0] + " Mise = " + str(round(opti_bet[1], 2)) + "%\n" + "Odds c = " + str(c) + " chez " + max_odds[2][0] + " Mise = " + str(round(opti_bet[2], 2)) + "%\n"
            log.discord(text)
            message += text
        else :
            taux = (1 - res) * 100 + 100
            message += "Pas d'arbitrage " + str(round(taux, 2)) + "%\n"
            message += "Match: " + game[0] + " vs " + game[1] + "\n"
            message += "Odds a = " + str(a) + " chez " + max_odds[0][0] + "\n"
            message += "Odds b = " + str(b) + " chez " + max_odds[1][0] + "\n"
            message += "Odds c = " + str(c) + " chez " + max_odds[2][0] + "\n"

    message += "\n"
    return message

            



def arb_ligue1():
    # créer un tableau qui contient à chaque case un tuple contenant le nom du casino et les games
    bookies = []
    message = ""

    betfirstGames = betfirst.get_games({"sport": "football", "competition": "ligue1"})
    zebetGames = zebet.get_games({"sport": "football", "competition": "ligue1"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "ligue1"})
    bwinGames = bwin.get_games({"sport": "football", "competition": "ligue1"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "ligue1"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "ligue1"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "ligue1"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "ligue1"})
    

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"


    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))
    
    bookies.sort(key=lambda x: len(x[1]), reverse=True)

    
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_ligue1)
    return message

def arb_liga():
    bookies = []
    message = ""


    
    zebetGames = zebet.get_games({"sport": "football", "competition": "liga"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "liga"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "liga"})
    bwinGames = bwin.get_games({"sport": "football", "competition": "liga"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "liga"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "liga"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "liga"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "liga"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)

    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_liga)
    return message

def arb_bundesliga():
    bookies = []
    message = ""


    zebetGames = zebet.get_games({"sport": "football", "competition": "bundesliga"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "bundesliga"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "bundesliga"})
    bwinGames = bwin.get_games({"sport": "football", "competition": "bundesliga"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "bundesliga"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "bundesliga"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "bundesliga"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "bundesliga"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)

    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_bundesliga)
    return message

def arb_premier_league():

    bookies = []
    message = ""

    zebetGames = zebet.get_games({"sport": "football", "competition": "premier-league"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "premier-league"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "premier-league"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"premier-league"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "premier-league"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "premier-league"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "premier-league"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "premier-league"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)

    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_premier_league)
    return message

def arb_serie_a():
    bookies = []
    message = ""


	
    zebetGames = zebet.get_games({"sport": "football", "competition": "serie-a"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "serie-a"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "serie-a"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"serie-a"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "serie-a"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "serie-a"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "serie-a"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "serie-a"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"
	
    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_serie_a)
    return message

def arb_primeira():
    bookies = []
    message = ""
    
    
    zebetGames = zebet.get_games({"sport": "football", "competition": "primeira"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "primeira"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "primeira"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"primeira"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "primeira"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "primeira"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "primeira"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "primeira"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))
    
    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_primeria)
    return message

def arb_a_league():
    bookies = []
    message = ""


    zebetGames = zebet.get_games({"sport": "football", "competition": "a-league"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "a-league"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "a-league"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"a-league"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "a-league"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "a-league"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "a-league"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "a-league"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_a_league)
    return message

def arb_bundesliga_austria():
    bookies = []
    message = ""

	
    zebetGames = zebet.get_games({"sport": "football", "competition": "bundesliga-austria"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "bundesliga-austria"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "bundesliga-austria"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"bundesliga-austria"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "bundesliga-austria"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "bundesliga-austria"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "bundesliga-austria"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "bundesliga-austria"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_bundesliga_austria)
    return message

def arb_division_1a():
    bookies = []
    message = ""

	
    zebetGames = zebet.get_games({"sport": "football", "competition": "division-1a"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "division-1a"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "division-1a"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"division-1a"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "division-1a"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "division-1a"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "division-1a"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "division-1a"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_division_1a)
    return message

def arb_super_lig():
    bookies = []
    message = ""


    zebetGames = zebet.get_games({"sport": "football", "competition": "super-lig"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "super-lig"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "super-lig"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"super-lig"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "super-lig"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "super-lig"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "super-lig"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "super-lig"})
	
    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_super_lig)
    return message

def arb_champions_league():
    bookies = []
    message = ""


    zebetGames = zebet.get_games({"sport": "football", "competition": "champions-league"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "champions-league"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "champions-league"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"champions-league"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "champions-league"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "champions-league"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "champions-league"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "champions-league"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    mismatch_champions_league = mismatch_ligue1 + mismatch_liga + mismatch_bundesliga + mismatch_premier_league + mismatch_serie_a + mismatch_primeria + mismatch_a_league + mismatch_bundesliga_austria + mismatch_division_1a + mismatch_super_lig
    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_champions_league)
    return message

def arb_europa_league():
    bookies = []
    message = ""

    zebetGames = zebet.get_games({"sport": "football", "competition": "europa-league"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "europa-league"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "europa-league"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"europa-league"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "europa-league"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "europa-league"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "europa-league"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "europa-league"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    mismatch_europa_league = mismatch_ligue1 + mismatch_liga + mismatch_bundesliga + mismatch_premier_league + mismatch_serie_a + mismatch_primeria + mismatch_a_league + mismatch_bundesliga_austria + mismatch_division_1a + mismatch_super_lig

    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_europa_league)
    return message

def arb_conference_league():
    bookies = []
    message = ""

    zebetGames = zebet.get_games({"sport": "football", "competition": "europa-conference"})
    betfirstGames = betfirst.get_games({"sport": "football", "competition": "europa-conference"})
    ladbrokesGames = ladbrokes.get_games({"sport": "football", "competition": "europa-conference"})
    bwinGames = bwin.get_games({"sport":"football", "competition":"europa-conference"})
    napoleonGames = napoleon.get_games({"sport": "football", "competition": "europa-conference"})
    unibetGames = unibet.get_games({"sport": "football", "competition": "europa-conference"})
    betcenterGames = betcenter.get_games({"sport": "football", "competition": "europa-conference"})
    scoooreGames = scooore.get_games({"sport": "football", "competition": "europa-conference"})

    message += "len betfirstGames " + str(len(betfirstGames)) + "\n"
    message += "len zebetGames " + str(len(zebetGames)) + "\n"
    message += "len ladbrokesGames " + str(len(ladbrokesGames)) + "\n"
    message += "len bwinGames " + str(len(bwinGames)) + "\n"
    message += "len napoleonGames " + str(len(napoleonGames)) + "\n"
    message += "len unibetGames " + str(len(unibetGames)) + "\n"
    message += "len betcenterGames " + str(len(betcenterGames)) + "\n"
    message += "len scoooreGames " + str(len(scoooreGames)) + "\n"

    bookies.append(("zebet", zebetGames))
    bookies.append(("betfirst", betfirstGames))
    bookies.append(("ladbrokes", ladbrokesGames))
    bookies.append(("bwin", bwinGames))
    bookies.append(("napoleon", napoleonGames))
    bookies.append(("unibet", unibetGames))
    bookies.append(("betcenter", betcenterGames))
    bookies.append(("scooore", scoooreGames))

    bookies.sort(key=lambda x: len(x[1]), reverse=True)
    mismatch_conference_league = mismatch_ligue1 + mismatch_liga + mismatch_bundesliga + mismatch_premier_league + mismatch_serie_a + mismatch_primeria + mismatch_a_league + mismatch_bundesliga_austria + mismatch_division_1a + mismatch_super_lig

    
    for bo in bookies:
        message += str(bo) + "\n"


    message += get_arbs(bookies, mismatch_conference_league)
    return message






			

        
	


