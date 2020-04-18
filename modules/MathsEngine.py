#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import json
import os
import sys
from modules.ConfigEngine import get_config

directory = os.path.join(os.path.dirname(__file__), '../')

def put_sign(var):
	if var > 0:
		return '+' + str(var)
	elif var == 0:
		return 'N/A'
	else:
		return str(var)

def check_data_change():
    with open(directory + 'data/todayGouvData.json') as today_data:
        data = json.load(today_data)
        cas_confirmes = data['casConfirmes']
        deces_hopital = data['decesHopital']
        deces_ehpad = data['decesEhpad']
        total_deces = data['totalDeces']
        cas_reanimation = data['casReanimation']
        cas_hopital = data['casHopital']
        cas_gueris = data['casGueris']
        cas_malades = data['casMalades']
        cas_ehpad = data['casEhpad']

    with open(directory + 'data/oldGouvData.json') as oldData:
        data = json.load(oldData)
        if data['casConfirmes'] != cas_confirmes:
            print("[INFO] Vérification: chiffres modifiés !")
        else:
            print("[ATTENTION] Aucun changement n'a été détecté dans les chiffres.")
            sys.exit()


def calc_difference():
    with open(directory + 'data/todayGouvData.json') as today_data:
        data = json.load(today_data)
        cas_confirmes = data['casConfirmes']
        deces_hopital = data['decesHopital']
        deces_ehpad = data['decesEhpad']
        total_deces = data['totalDeces']
        cas_reanimation = data['casReanimation']
        cas_hopital = data['casHopital']
        cas_gueris = data['casGueris']
        cas_malades = data['casMalades']
        cas_ehpad = data['casEhpad']

    with open(directory + 'data/oldGouvData.json') as old_dataData:
        data = json.load(old_dataData)
        old_cas_confirmes = data['casConfirmes']
        old_deces_hopital = data['decesHopital']
        old_deces_ehpad = data['decesEhpad']
        old_total_deces = data['totalDeces']
        old_cas_reanimation = data['casReanimation']
        old_cas_hopital = data['casHopital']
        old_cas_gueris = data['casGueris']
        old_cas_malades = data['casMalades']
        old_cas_ehpad = data['casEhpad']

    with open(directory + 'data/todayWorldometersData.json') as today_data:
        data = json.load(today_data)
        cases = data['cases']
        deaths = data['deaths']
        recovered = data['recovered']
        active = data['active']
        critical = data['critical']
        totalTests = data['totalTests']
        todayCases = data['todayCases']

    with open(directory + 'data/oldWorldometersData.json') as oldData:
        data = json.load(oldData)
        old_cases = data['cases']
        old_deaths = data['deaths']
        old_recovered = data['recovered']
        old_active = data['active']
        old_critical = data['critical']
        old_totalTests = data['totalTests']

    diff_cas_confirmes = cas_confirmes - old_cas_confirmes
    diff_deces_hopital = deces_hopital - old_deces_hopital
    diff_deces_ehpad = deces_ehpad - old_deces_ehpad
    diff_total_deces = total_deces - old_total_deces
    diff_cas_reanimation = cas_reanimation - old_cas_reanimation
    diff_cas_hopital = cas_hopital - old_cas_hopital
    diff_cas_gueris = cas_gueris - old_cas_gueris
    diff_cas_malades = cas_malades - old_cas_malades
    diff_cas_ehpad = cas_ehpad - old_cas_ehpad

    diff_active_cases = active - old_active
    diff_total_tests = totalTests - old_totalTests
    diff_today_cases = todayCases

    diff_cas_confirmes = put_sign(diff_cas_confirmes)
    diff_deces_hopital = put_sign(diff_deces_hopital)
    diff_deces_ehpad = put_sign(diff_deces_ehpad)
    diff_total_deces = put_sign(diff_total_deces)
    diff_cas_reanimation = put_sign(diff_cas_reanimation)
    diff_cas_hopital = put_sign(diff_cas_hopital)
    diff_cas_gueris = put_sign(diff_cas_gueris)
    diff_cas_malades = put_sign(diff_cas_malades)
    diff_active_cases = put_sign(diff_active_cases)
    diff_total_tests = put_sign(diff_total_tests)
    diff_today_cases = put_sign(diff_today_cases)
    diff_cas_ehpad = put_sign(diff_cas_ehpad)

    diff_data = {
        'casConfirmes': diff_cas_confirmes,
        'casEhpad': diff_cas_ehpad,
        'decesHopital': diff_deces_hopital,
        'decesEhpad': diff_deces_ehpad,
        'totalDeces': diff_total_deces,
        'casReanimation': diff_cas_reanimation,
        'casHopital': diff_cas_hopital,
        'casGueris': diff_cas_gueris,
        'casMalades_GOUV': diff_cas_malades,
        'casMalades_WORLDOMETERS': diff_active_cases,
        'todayCases': diff_today_cases,
        'totalTests': diff_total_tests
    }

    '''
	print("\nDifférences des données:")
	print(diffData)
	print("\n")
	'''
    return diff_data


def percentage_calc():
    with open(directory + 'data/todayGouvData.json') as todayData:
        data = json.load(todayData)
        total_deces = data['totalDeces']
        cas_gueris = data['casGueris']
        total_cases = data['casConfirmes']

        cas_gueris = str("[" + str(round((float(cas_gueris) / float(total_cases) * float(100)), 2)) + "%]")
        total_deces = str("[" + str(round((float(total_deces) / float(total_cases) * float(100)), 2)) + "%]")

        percent_data = {
            'casGueris': cas_gueris,
            'totalDeces': total_deces
        }

    return percent_data


def save_gouv_data(data):
    with open(directory + 'data/oldGouvData.json', 'w') as fp:
        json.dump(data, fp)


def save_worldometers_data(data):
    with open(directory + 'data/oldWorldometersData.json', 'w') as fp:
        json.dump(data, fp)
