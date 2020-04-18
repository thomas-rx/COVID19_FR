#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
import json
import sys
from ConfigEngine import * 

directory = getConfig('System', 'directory')

def putSign(var):
	if var > 0:
		return '+' + str(var)
	elif var == 0:
		return 'N/A'
	else:
		return str(var)

def checkDataChange():
	with open(directory + 'data/todayGouvData.json') as todayData:
		data = json.load(todayData)
		casConfirmes = data['casConfirmes']
		decesHopital = data['decesHopital']
		decesEhpad = data['decesEhpad']
		totalDeces = data['totalDeces']
		casReanimation = data['casReanimation']
		casHopital = data['casHopital']
		casGueris = data['casGueris']
		casMalades = data['casMalades']
		casEhpad = data['casEhpad']

	with open(directory + 'data/oldGouvData.json') as oldData:
		data = json.load(oldData)
		if data['casConfirmes'] != casConfirmes:
			print("[INFO] Vérification: chiffres modifiés !")
		else:
			print("[ATTENTION] Aucun changement n'a été détecté dans les chiffres.")
			#sys.exit()

def CalcDifference():
	with open(directory + 'data/todayGouvData.json') as todayData:
		data = json.load(todayData)
		casConfirmes = data['casConfirmes']
		decesHopital = data['decesHopital']
		decesEhpad = data['decesEhpad']
		totalDeces = data['totalDeces']
		casReanimation = data['casReanimation']
		casHopital = data['casHopital']
		casGueris = data['casGueris']
		casMalades = data['casMalades']
		casEhpad = data['casEhpad']

	with open(directory + 'data/oldGouvData.json') as oldData:
		data = json.load(oldData)
		old_casConfirmes = data['casConfirmes']
		old_decesHopital = data['decesHopital']
		old_decesEhpad = data['decesEhpad']
		old_totalDeces = data['totalDeces']
		old_casReanimation = data['casReanimation']
		old_casHopital = data['casHopital']
		old_casGueris = data['casGueris']
		old_casMalades = data['casMalades']
		old_casEhpad = data['casEhpad']

	with open(directory + 'data/todayWorldometersData.json') as todayData:
		data = json.load(todayData)
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

	diff_casConfirmes = casConfirmes - old_casConfirmes
	diff_decesHopital = decesHopital - old_decesHopital
	diff_decesEhpad = decesEhpad - old_decesEhpad
	diff_totalDeces = totalDeces - old_totalDeces
	diff_casReanimation = casReanimation - old_casReanimation
	diff_casHopital = casHopital - old_casHopital
	diff_casGueris = casGueris - old_casGueris
	diff_casMalades = casMalades - old_casMalades
	diff_casEhpad = casEhpad - old_casEhpad

	diff_activeCases = active - old_active
	diff_totalTests = totalTests - old_totalTests
	diff_todayCases = todayCases

	diff_casConfirmes = putSign(diff_casConfirmes)

	diff_decesHopital = putSign(diff_decesHopital)

	diff_decesEhpad = putSign(diff_decesEhpad)

	diff_totalDeces = putSign(diff_totalDeces)

	diff_casReanimation = putSign(diff_casReanimation)

	diff_casHopital = putSign(diff_casHopital)

	diff_casGueris = putSign(diff_casGueris)

	diff_casMalades = putSign(diff_casMalades)

	diff_activeCases = putSign(diff_activeCases)

	diff_totalTests = putSign(diff_totalTests)

	diff_todayCases = putSign(diff_todayCases)

	diff_casEhpad = putSign(diff_casEhpad)

	diffData = {
	    'casConfirmes': diff_casConfirmes,
		'casEhpad': diff_casEhpad,
	    'decesHopital': diff_decesHopital,
	    'decesEhpad': diff_decesEhpad,
	    'totalDeces': diff_totalDeces,
	    'casReanimation': diff_casReanimation,
	    'casHopital': diff_casHopital,
	    'casGueris': diff_casGueris,
	    'casMalades_GOUV': diff_casMalades,
	    'casMalades_WORLDOMETERS': diff_activeCases,
	    'todayCases': diff_todayCases,
	    'totalTests': diff_totalTests
	}

	'''
	print("\nDifférences des données:")
	print(diffData)
	print("\n")
	'''
	return (diffData)

def percentageCalc():
	with open(directory + 'data/todayGouvData.json') as todayData:
		data = json.load(todayData)
		totalDeces = data['totalDeces']
		casGueris = data['casGueris']
		totalCases = data['casConfirmes']

		casGueris = str("[" + str(round((float(casGueris) / float(totalCases) * float(100)), 2)) + "%]")
		totalDeces = str("[" + str(round((float(totalDeces) / float(totalCases) * float(100)), 2)) + "%]")

		percentData = {
		    'casGueris': casGueris,
		    'totalDeces': totalDeces
		}

	return percentData

def saveGouvData(data):
	with open(directory + 'data/oldGouvData.json', 'w') as fp:
		json.dump(data, fp)

def saveWorldometersData(data):
	with open(directory + 'data/oldWorldometersData.json', 'w') as fp:
		json.dump(data, fp)