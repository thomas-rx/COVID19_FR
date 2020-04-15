#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
import requests
import json
import datetime
from ConfigEngine import * 

dateSelected = datetime.datetime.now().strftime("%Y-%m-%d") #Date du jour pour parse le JSON
directory = getConfig('System', 'directory')

#dateSelected = '2020-04-14' #Permet de sélectionner une date 'manuellement'

def getData(source):
	if(source == "WORLDOMETERS"):
		WorldometersAPI = requests.get("https://coronavirus-19-api.herokuapp.com/countries/France")
		WorldometersData = WorldometersAPI.json()

		'''
		print("\nDonnées de WORLDOMETERS:")
		print(WorldometersData)
		print("\n")
		'''

		with open(directory + 'data/todayWorldometersData.json', 'w') as data:
			json.dump(WorldometersData, data)

		return(WorldometersData)

	elif(source == "GOUVERNEMENT"):
		GouvData = requests.get("https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.json") 
		GouvData = GouvData.json()
		lineCount = len(GouvData)

		for i in range(lineCount):
			if(GouvData[i]['sourceType'] == "ministere-sante"):
				if(GouvData[i]['date'] == dateSelected):

					try:
						if(int(getConfig("CustomData", "casConfirmes")) > 0):
							casConfirmes = int(getConfig("CustomData", "casConfirmes"))
							print("[ATTENTION] Chiffres 'casConfirmes' modifiés manuellements")
					except:
						casConfirmes = GouvData[i]['casConfirmes']

					try:
						if(int(getConfig("CustomData", "decesHopital")) > 0):
							decesHopital = int(getConfig("CustomData", "decesHopital"))
							print("[ATTENTION] Chiffres 'decesHopital' modifiés manuellements")
					except:
						decesHopital = GouvData[i]['deces']

					try:
						if(int(getConfig("CustomData", "decesEhpad")) > 0):
							decesEhpad = int(getConfig("CustomData", "decesEhpad"))
							print("[ATTENTION] Chiffres 'decesEhpad' modifiés manuellements")
					except:
						decesEhpad = GouvData[i]['decesEhpad']

					try:
						if(int(getConfig("CustomData", "casReanimation")) > 0):
							casReanimation = int(getConfig("CustomData", "casReanimation"))
							print("[ATTENTION] Chiffres 'casReanimation' modifiés manuellements")
					except:
						casReanimation = GouvData[i]['reanimation']


					try:
						if(int(getConfig("CustomData", "casHopital")) > 0):
							casHopital = int(getConfig("CustomData", "casHopital"))
							print("[ATTENTION] Chiffres 'casHopital' modifiés manuellements")
					except:
						casHopital = GouvData[i]['hospitalises']

					try:
						if(int(getConfig("CustomData", "casGueris")) > 0):
							casGueris = int(getConfig("CustomData", "casGueris"))
							print("[ATTENTION] Chiffres 'casGueris' modifiés manuellements")
					except:
						casGueris = GouvData[i]['gueris']

					try:
						if(int(getConfig("CustomData", "casEhpad")) > 0):
							casEhpad = int(getConfig("CustomData", "casEhpad"))
							print("[ATTENTION] Chiffres 'casEhpad' modifiés manuellements")
					except:
						casEhpad = GouvData[i]['casEhpad']

					try:
						if(int(getConfig("CustomData", "totalDeces")) > 0):
							totalDeces = int(getConfig("CustomData", "totalDeces"))
							print("[ATTENTION] Chiffres 'totalDeces' modifiés manuellements")
					except:
						totalDeces = decesHopital + decesEhpad

					try:
						if(int(getConfig("CustomData", "casMalades")) > 0):
							casMalades = int(getConfig("CustomData", "casMalades"))
							print("[ATTENTION] Chiffres 'casMalades' modifiés manuellements")
					except:
						casMalades = casConfirmes - (totalDeces + casGueris)

					gouvData = {
					    'casConfirmes': casConfirmes,
					    'decesHopital': decesHopital,
					    'decesEhpad': decesEhpad,
					    'totalDeces': totalDeces,
					    'casReanimation': casReanimation,
					    'casHopital': casHopital,
					    'casGueris': casGueris,
					    'casMalades': casMalades,
						'casEhpad': casEhpad
					}

					'''
					print("Données du GOUVERNEMENT:")
					print(gouvData)
					print("\n")
					'''
					
					with open(directory + 'data/todayGouvData.json', 'w') as data:
						json.dump(gouvData, data)
					
					return(gouvData)