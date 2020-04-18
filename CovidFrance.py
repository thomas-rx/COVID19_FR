#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/modules')

from APIEngine import *
from GraphEngine import *
from MathsEngine import *
from TwitterEngine import *
from TimeEngine import *
from ConfigEngine import *

api, auth = twitter_auth()  # API TWEEPY
directory = os.path.join(os.path.dirname(__file__), '../config.ini')
graphIMG = directory + "data/graphIMG.png"
LogTime = "[" + datetime.now().strftime("%D %H:%M:%S") + "] "

# ----------------------------------#

if check_time():  # On vérifie le créneau horaire si activé dans le fichier config.ini
    pass
else:
    sys.exit()

# ----------------------------------#

if get_last_tweet() == 1:  # On vérifie que le bot n'a pas déjà posté aujourd'hui
    print(LogTime + "Un tweet posté avec l'application [" + get_config('TwitterAPI',
                                                                       'app_name') + "] existe déjà pour aujourd'hui !")
    sys.exit()
elif get_last_tweet() == 0:
    print(LogTime + "Aucun tweet n'a été posté aujourd'hui, suite du programme...")
else:
    print(LogTime + "Erreur.")
    sys.exit()

# ----------------------------------#

gouvData = get_data("GOUVERNEMENT")  # On récupère les données du gouvernement

# ----------------------------------#

if gouvData != None:  # Si elles sont valides
    check_data_change()  # On vérifie quelles sont un minimum cohérentes
    worldometersData = get_data(
        "WORLDOMETERS")  # Si c'est bon, on récupère les données de Worldometers (je l'ai mis ici pour éviter de spam l'api et de se faire ban-ip)
else:
    print(LogTime + "Aucune donnée pour aujourd'hui ! (Source: Gouvernement)\n")
    sys.exit()

# ----------------------------------#

difference_data = calc_difference()  # On fait les calculs de toutes les données
percentage_data = percentage_calc()  # On récupère les pourcentages

print("\n----------------------------------------\n")

def format_data(data):
    return str("{0:,}".format(data))

# ----------------------------------#

# On met en forme les deux tweets
first_tweet_form = str("‪La 🇫🇷 est confinée depuis:"
                       + "\n" + get_days() + " jours"
                       + "\n"
                       + "\n" + "🟩 " + format_data(gouvData['casGueris']) + " guéris " + percentage_data[
                           'casGueris'] + " " + difference_data['casGueris']
                       + "\n" + "🟧 " + format_data(gouvData['casMalades']) + " malades " + difference_data[
                           'casMalades_GOUV']
                       + "\n" + "🟥 " + "dont " + format_data(gouvData['casReanimation']) + " cas graves " +
                       difference_data['casReanimation']
                       + "\n" + "⬛ " + format_data(gouvData['totalDeces']) + " morts " + percentage_data[
                           'totalDeces'] + " " + difference_data['totalDeces']
                       + "\n"
                       + "\n" + "‪◾️ " + format_data(gouvData['decesHopital']) + " en hôpitaux " +
                       difference_data['decesHopital']
                       + "\n" + "‪◾️ " + format_data(gouvData['decesEhpad']) + " en ESMS " + difference_data[
                           'decesEhpad']
                       + "\n"
                       + "\n" + "‪ 🦠 — " + format_data(gouvData['casConfirmes']) + " cas " + difference_data[
                           'casConfirmes']
                       + "\n"
                       + "\n" + "‪Graphique 📈 — ⬇️‬ "
                       + "\n" + "#ConfinementJour" + get_days() + " | #COVID19")

second_tweet_form = str(
    "🏠 " + format_data(gouvData['casEhpad']) + " cas en EHPAD" + " " + difference_data['casEhpad']
    + "\n" + "🛏 " + format_data(gouvData['casHopital']) + " hospitalisés" + " " + difference_data['casHopital']
    + "\n" + "🔬 " + format_data(worldometersData['totalTests']) + " dépistages"
    + "‪\n" + ""
    + "‪\n" + "📈 Évolution #graphique du #COVID19 en #France‬")

print(first_tweet_form)
print("\n------------------\n")
print(second_tweet_form)

print("\n----------------------------------------\n")

# input("\n----------------------------------------\nPressez ENTRER pour valider le tweet [...]") #Décommenter pour utiliser le bot manuellement

# ----------------------------------#
# On sauvegarde toutes les données
save_data_graph(gouvData['casConfirmes'], gouvData['casHopital'], gouvData['casReanimation'], gouvData['totalDeces'],
                gouvData['casGueris'])
print(LogTime + "Données du graphique mises à jours !")

save_gouv_data(gouvData)
print(LogTime + "Données du gouvernement sauvegardées !")

save_worldometers_data(worldometersData)
print(LogTime + "Données de Worldometers sauvegardées !")

make_graph()  # On génère le graphique
print(LogTime + "Graphique généré !")

# ----------------------------------#
# On tweet
tweet_post = api.update_status(first_tweet_form)

api.update_with_media(graphIMG, second_tweet_form, in_reply_to_status_id=tweet_post.id, retry_count=10, retry_delay=5,
                      retry_errors={503})

# On envoie le lien du tweet sur le compte privé du propriétaire
api.send_direct_message(recipient_id=get_config('TwitterAPI', 'preview_id'),
                        text="https://twitter.com/" + get_config('TwitterAPI', 'account_name') + "/status/" + str(
                            tweet_post.id))
