#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import os
import sys
from modules.APIEngine import get_data
from modules.GraphEngine import make_world_graph, make_local_graph, save_data_graph
from modules.MathsEngine import percentage_calc, save_worldometers_data, save_gouv_data, calc_difference, check_data_change
from modules.TwitterEngine import twitter_auth, get_last_tweet
from modules.TimeEngine import check_time, get_days, datetime, log_time
from modules.ConfigEngine import get_config, get_config_boolean

api, auth = twitter_auth()  # API TWEEPY

# ----------------------------------#

if check_time():  # On vérifie le créneau horaire si activé dans le fichier config.ini
    pass
else:
    sys.exit()

# ----------------------------------#

if get_last_tweet() == 1:  # On vérifie que le bot n'a pas déjà posté aujourd'hui
    print(log_time() + "Un tweet posté avec l'application [" + get_config('TwitterAPI',
                                                                       'app_name') + "] existe déjà pour aujourd'hui !")
    sys.exit()
elif get_last_tweet() == 0:
    print(log_time() + "Aucun tweet n'a été posté aujourd'hui, suite du programme...")
else:
    print(log_time() + "Erreur.")
    sys.exit()

# ----------------------------------#

gouvData = get_data("GOUVERNEMENT")  # On récupère les données du gouvernement

# ----------------------------------#

if gouvData != None:  # Si elles sont valides
    check_data_change()  # On vérifie quelles sont un minimum cohérentes
    worldometersData = get_data(
        "WORLDOMETERS")  # Si c'est bon, on récupère les données de Worldometers (je l'ai mis ici pour éviter de spam l'api et de se faire ban-ip)
else:
    print(log_time() + "Aucune donnée pour aujourd'hui ! (Source: Gouvernement)\n")
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
print(log_time() + "Données du graphique mises à jours !")

save_gouv_data(gouvData)
print(log_time() + "Données du gouvernement sauvegardées !")

save_worldometers_data(worldometersData)
print(log_time() + "Données de Worldometers sauvegardées !")

make_local_graph()  # On génère le graphique
print(log_time() + "Graphique pour la France généré !")

make_world_graph()
print(log_time() + "Graphique pour le monde généré !")

img_packed = ('data/localGraph.png', 'data/worldGraph.png')
media_tweet = [api.media_upload(i).media_id_string  for i in img_packed] 
print(log_time() + "Préparation des images pour le tweet terminée !")

# ----------------------------------#
# On tweet
posted_tweet = api.update_status(first_tweet_form)

api.update_status(status = second_tweet_form,  media_ids = media_tweet, in_reply_to_status_id = posted_tweet.id, retry_count=10, retry_delay=5, retry_errors=set([503]))

# On envoie le lien du tweet sur le compte privé du propriétaire
api.send_direct_message(recipient_id=get_config('TwitterAPI', 'preview_id'),
                        text="https://twitter.com/" + get_config('TwitterAPI', 'account_name') + "/status/" + str(
                            posted_tweet.id))