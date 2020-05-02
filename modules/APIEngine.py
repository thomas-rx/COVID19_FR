#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import requests
import json
import datetime
import os
from modules.ConfigEngine import get_config

dateSelected = datetime.datetime.now().strftime("%Y-%m-%d")  # Date du jour pour parse le JSON
directory = os.path.join(os.path.dirname(__file__), '../')

#dateSelected = '2020-04-29' #Permet de sélectionner une date 'manuellement'

def get_data(source):
    if source == "WORLDOMETERS":
        worldometers_api = requests.get("https://coronavirus-19-api.herokuapp.com/countries/France")
        worldometers_data = worldometers_api.json()

        '''
		print("\nDonnées de WORLDOMETERS:")
		print(WorldometersData)
		print("\n")
		'''

        with open(directory + 'data/todayWorldometersData.json', 'w') as data:
            json.dump(worldometers_data, data)

        return worldometers_data

    elif source == "GOUVERNEMENT":
        gouv_data = requests.get("https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.json")
        gouv_data = gouv_data.json()
        line_count = len(gouv_data)

        for i in range(line_count):
            if gouv_data[i]['sourceType'] == "ministere-sante" and gouv_data[i]['date'] == dateSelected:
                try:
                    if int(get_config("CustomData", "casConfirmes")) > 0:
                        cas_confirmes = int(get_config("CustomData", "casConfirmes"))
                        print("[ATTENTION] Chiffres 'casConfirmes' modifiés manuellements")
                except:
                    cas_confirmes = gouv_data[i]['casConfirmes']

                try:
                    if int(get_config("CustomData", "decesHopital")) > 0:
                        deces_hopital = int(get_config("CustomData", "decesHopital"))
                        print("[ATTENTION] Chiffres 'decesHopital' modifiés manuellements")
                except:
                    deces_hopital = gouv_data[i]['deces']

                try:
                    if int(get_config("CustomData", "decesEhpad")) > 0:
                        deces_ehpad = int(get_config("CustomData", "decesEhpad"))
                        print("[ATTENTION] Chiffres 'decesEhpad' modifiés manuellements")
                except:
                    deces_ehpad = gouv_data[i]['decesEhpad']

                try:
                    if int(get_config("CustomData", "casReanimation")) > 0:
                        cas_reanimation = int(get_config("CustomData", "casReanimation"))
                        print("[ATTENTION] Chiffres 'casReanimation' modifiés manuellements")
                except:
                    cas_reanimation = gouv_data[i]['reanimation']

                try:
                    if int(get_config("CustomData", "casHopital")) > 0:
                        cas_hopital = int(get_config("CustomData", "casHopital"))
                        print("[ATTENTION] Chiffres 'casHopital' modifiés manuellements")
                except:
                    cas_hopital = gouv_data[i]['hospitalises']

                try:
                    if int(get_config("CustomData", "casGueris")) > 0:
                        cas_gueris = int(get_config("CustomData", "casGueris"))
                        print("[ATTENTION] Chiffres 'casGueris' modifiés manuellements")
                except:
                    cas_gueris = gouv_data[i]['gueris']

                try:
                    if (int(get_config("CustomData", "casEhpad")) > 0):
                        cas_ehpad = int(get_config("CustomData", "casEhpad"))
                        print("[ATTENTION] Chiffres 'casEhpad' modifiés manuellements")
                except:
                    cas_ehpad = gouv_data[i]['casEhpad']

                try:
                    if (int(get_config("CustomData", "casConfirmesEhpad")) > 0):
                        cas_confirmes_ehpad = int(get_config("CustomData", "casConfirmesEhpad"))
                        print("[ATTENTION] Chiffres 'casConfirmesEhpad' modifiés manuellements")
                except:
                    cas_confirmes_ehpad = gouv_data[i]['casConfirmesEhpad']

                try:
                    if int(get_config("CustomData", "totalDeces")) > 0:
                        total_deces = int(get_config("CustomData", "totalDeces"))
                        print("[ATTENTION] Chiffres 'totalDeces' modifiés manuellements")
                except:
                    total_deces = deces_hopital + deces_ehpad

                try:
                    if int(get_config("CustomData", "casMalades")) > 0:
                        cas_malades = int(get_config("CustomData", "casMalades"))
                        print("[ATTENTION] Chiffres 'casMalades' modifiés manuellements")
                except:
                    cas_malades = cas_confirmes - (total_deces + cas_gueris)

                gouv_data = {
                    'casConfirmes': cas_confirmes,
                    'decesHopital': deces_hopital,
                    'decesEhpad': deces_ehpad,
                    'totalDeces': total_deces,
                    'casReanimation': cas_reanimation,
                    'casHopital': cas_hopital,
                    'casGueris': cas_gueris,
                    'casMalades': cas_malades,
                    'casEhpad': cas_ehpad,
                    'casConfirmesEhpad': cas_confirmes_ehpad
                }

                '''
                print("Données du GOUVERNEMENT:")
                print(gouvData)
                print("\n")
                '''

                with open(directory + 'data/todayGouvData.json', 'w') as data:
                    json.dump(gouv_data, data)

                return gouv_data

get_data("GOUVERNEMENT")