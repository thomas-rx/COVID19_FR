#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import os
import sys
from modules.APIEngine import GouvernementAPI, WorldometersAPI
from modules.GraphEngine import make_world_graph, make_local_graph, save_data_graph
from modules.MathsEngine import percentage_calc, save_worldometers_data, save_gouv_data, calc_difference, \
    check_data_change
from modules.TwitterEngine import TwitterEngine
from modules.TimeEngine import check_time, get_days, datetime, log_time
from modules.ConfigEngine import TwitterAPIConfig, BaseConfigEngine

twitter_conf = TwitterAPIConfig()
twitter_handler = TwitterEngine(twitter_conf)

# ----------------------------------#

if not check_time():  # On vérifie le créneau horaire si activé dans le fichier config.ini
    sys.exit()

# ----------------------------------#
try:
    if twitter_handler.is_there_a_last_tweet():  # On vérifie que le bot n'a pas déjà posté aujourd'hui
        print(log_time() + "Un tweet posté avec l'application [" +
              twitter_conf.app_name + "] existe déjà pour aujourd'hui !")
        sys.exit()

    else:
        print(log_time() + "Aucun tweet n'a été posté aujourd'hui, suite du programme...")

except Exception as why:
    print(log_time() + "Erreur : " + why)
    sys.exit()

# ----------------------------------#

gouvData = GouvernementAPI.get_data()  # On récupère les données du gouvernement

# ----------------------------------#

if gouvData is not None:  # Si elles sont valides
    check_data_change()  # On vérifie quelles sont un minimum cohérentes
    worldometersData = WorldometersAPI.get_data()

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
first_tweet_form = str("‪Bilan du #COVID19 en #France🇫🇷 "
                       + "\n"
                       + "\n" + "🟩 " +
                       format_data(gouvData['casGueris']) + " guéris " +
                       "(" + difference_data['casGueris'] + ")"
                       + "\n"
                       + "\n" + "🟧 ≃ " +
                       format_data(gouvData['casMalades']) + " malades " +
                       "(" + difference_data['casMalades_GOUV'] + ")"
                       + "\n"
                       + "\n" + "🟥 " +
                       format_data(gouvData['casReanimation']) + " cas graves " +
                       "(" + difference_data['casReanimation'] + ")"
                       + "\n"
                       + "\n" + "⬛ " +
                       format_data(gouvData['totalDeces']) + " décès " +
                       "(" + difference_data['totalDeces'] + ")"
                       + "\n"
                       + "\n"
                       + "\n" + "‪🦠 — " +
                       format_data(gouvData['casConfirmes']) + " cas " +
                       "(" + difference_data['casConfirmes'] + ")"
                       + "\n" + "🔬 — ≃ " +
                       format_data(
                           worldometersData['totalTests']) + " dépistages"
                       + "\n"
                       + "\n" + "‪📃 — Ministère de la Santé‬ ")

second_tweet_form = str("📈 Évolutions #graphiques du #COVID19 en #France‬")

print(first_tweet_form)

# Décommenter pour utiliser le bot manuellement
# input("\n----------------------------------------\nPressez ENTRER pour valider le tweet [...]")

# ----------------------------------#

# On sauvegarde toutes les données
save_data_graph(gouvData['casConfirmes'], gouvData['casHopital'],
                gouvData['casReanimation'], gouvData['totalDeces'], gouvData['casGueris'])
print(log_time() + "Données du graphique mises à jours !")

save_gouv_data(gouvData)
save_worldometers_data(worldometersData)
print(log_time() + "Données sauvegardées !")

make_local_graph()  # On génère le graphique
make_world_graph()
print(log_time() + "Graphiques générés !")

img_packed = ('/root/COVID19-France/data/localGraph.png',
              '/root/COVID19-France/data/worldGraph.png')
media_tweet = [twitter_handler.api.media_upload(
    i).media_id_string for i in img_packed]
print(log_time() + "Préparation des images pour le tweet terminée !")

# ----------------------------------#
# On tweet
posted_tweet = twitter_handler.api.update_status(first_tweet_form)

twitter_handler.api.update_status(status=second_tweet_form, media_ids=media_tweet, in_reply_to_status_id=posted_tweet.id,
                                  retry_count=10, retry_delay=5, retry_errors={503})

# On envoie le lien du tweet sur le compte privé du propriétaire
twitter_handler.api.send_direct_message(recipient_id=twitter_conf.preview_id,
                                        text="https://twitter.com/" + twitter_conf.account_name + "/status/" + str(
                                            posted_tweet.id))
