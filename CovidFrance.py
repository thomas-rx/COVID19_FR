#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
import sys

from modules.TwitterEngine import *
from modules.APIEngine import *
from modules.GraphEngine import *
from modules.MathsEngine import *
from modules.TimeEngine import *
from modules.ConfigEngine import *

api, auth = TwitterAuth() #API TWEEPY
directory = getConfig('System', 'directory')
graphIMG = directory + "data/graphIMG.png"
LogTime = "[" + datetime.now().strftime("%D %H:%M:%S") + "] "

#----------------------------------#

if(checkTime() == True): #On vérifie le créneau horaire si activé dans le fichier config.ini
	pass
else:
	sys.exit()

#----------------------------------#

if(getLastTweet() == 1): #On vérifie que le bot n'a pas déjà posté aujourd'hui
	print(LogTime + "Un tweet posté avec l'application [" + getConfig('TwitterAPI', 'app_name') + "] existe déjà pour aujourd'hui !")
	sys.exit()
elif(getLastTweet() == 0):
	print(LogTime + "Aucun tweet n'a été posté aujourd'hui, suite du programme...")
else:
	print(LogTime + "Erreur.")
	sys.exit()

#----------------------------------#

gouvData = getData("GOUVERNEMENT") #On récupère les données du gouvernement

#----------------------------------#

if(gouvData !=  None): #Si elles sont valides
	checkDataChange() #On vérifie quelles sont un minimum cohérentes
	worldometersData = getData("WORLDOMETERS") #Si c'est bon, on récupère les données de Worldometers (je l'ai mis ici pour éviter de spam l'api et de se faire ban-ip)
else:
	print(LogTime + "Aucune donnée pour aujourd'hui ! (Source: Gouvernement)\n")
	sys.exit()

#----------------------------------#

DiffData = CalcDifference() #On fait les calculs de toutes les données
percentageData = percentageCalc()  #On récupère les pourcentages

print("\n----------------------------------------\n")

#----------------------------------#

#On met en forme les deux tweets
firstTweetForm = str("‪La 🇫🇷 est confinée depuis:"
		+ "\n" + getDays() + " jours" 
		+ "\n"
		+ "\n" + "🟩 " + str("{0:,}".format(gouvData['casGueris'])) + " guéris " + percentageData['casGueris'] + " " + DiffData['casGueris']
		+ "\n" + "🟧 " + str("{0:,}".format(gouvData['casMalades'])) + " malades " + DiffData['casMalades_GOUV']
		+ "\n" + "🟥 " + "dont " + str("{0:,}".format(gouvData['casReanimation'])) + " cas graves " + DiffData['casReanimation']
		+ "\n" + "⬛ " 	+ str("{0:,}".format(gouvData['totalDeces'])) + " morts " + percentageData['totalDeces'] + " " + DiffData['totalDeces']
		+ "\n"
		+ "\n" + "‪◾️ " + str("{0:,}".format(gouvData['decesHopital'])) + " en hôpitaux " + DiffData['decesHopital']
		+ "\n" + "‪◾️ " + str("{0:,}".format(gouvData['decesEhpad'])) + " en ESMS " + DiffData['decesEhpad'] 
		+ "\n"
		+ "\n" + "‪ 🦠 — " + str("{0:,}".format(gouvData['casConfirmes'])) + " cas " + DiffData['casConfirmes']
		+ "\n"
		+ "\n" + "‪Graphique 📈 — ⬇️‬ "
		+ "\n" + "#ConfinementJour" + getDays() + " | #COVID19")

secondTweetForm = str("🏠 " + str("{0:,}".format(gouvData['casEhpad'])) + " cas en EHPAD" + " " + DiffData['casEhpad']
		+ "\n" + "🛏 " + str("{0:,}".format(gouvData['casHopital'])) + " hospitalisés" + " " + DiffData['casHopital']
		+ "\n" + "🔬 " + str("{0:,}".format(worldometersData['totalTests'])) + " dépistages" 
		+ "‪\n" + ""
		+ "‪\n" + "📈 Évolution #graphique du #COVID19 en #France‬")

print(firstTweetForm)
print("\n------------------\n")
print(secondTweetForm)

print("\n----------------------------------------\n")

#input("\n----------------------------------------\nPressez ENTRER pour valider le tweet [...]") #Décommenter pour utiliser le bot manuellement
 
#----------------------------------# 
#On sauvegarde toutes les données
saveDataGraph(gouvData['casConfirmes'], gouvData['casHopital'], gouvData['casReanimation'], gouvData['totalDeces'], gouvData['casGueris'])
print(LogTime + "Données du graphique mises à jours !")

saveGouvData(gouvData)
print(LogTime + "Données du gouvernement sauvegardées !")

saveWorldometersData(worldometersData)
print(LogTime + "Données de Worldometers sauvegardées !")

makeGraph() #On génère le graphique
print(LogTime + "Graphique généré !")

#----------------------------------#
#On tweet
TweetPost = api.update_status(firstTweetForm) 

api.update_with_media(graphIMG, secondTweetForm, in_reply_to_status_id = TweetPost.id, retry_count=10, retry_delay=5, retry_errors=set([503]))

#On envoie le lien du tweet sur le compte privé du propriétaire
api.send_direct_message(recipient_id  = getConfig('TwitterAPI', 'preview_id'), text = "https://twitter.com/" + getConfig('TwitterAPI', 'account_name') + "/status/" + str(TweetPost.id))
