#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
import json

from modules.ConfigEngine import getConfig

directory = getConfig('System', 'directory')

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
		if (data['casConfirmes'] != casConfirmes):
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

	if (diff_casConfirmes > 0):
	    diff_casConfirmes = "+" + str(diff_casConfirmes)
	elif(diff_casConfirmes == 0):
	    diff_casConfirmes = "N/A"
	elif(diff_casConfirmes < 0):
	    diff_casConfirmes = "" + str(diff_casConfirmes)

	if (diff_decesHopital > 0):
	    diff_decesHopital = "+" + str(diff_decesHopital)
	elif(diff_decesHopital == 0):
	    diff_decesHopital = "N/A"
	elif(diff_decesHopital < 0):
	    diff_decesHopital = "" + str(diff_decesHopital)

	if (diff_decesEhpad > 0):
	    diff_decesEhpad = "+" + str(diff_decesEhpad)
	elif(diff_decesEhpad == 0):
	    diff_decesEhpad = "N/A"
	elif(diff_decesEhpad < 0):
	    diff_decesEhpad = "" + str(diff_decesEhpad)

	if (diff_totalDeces > 0):
	    diff_totalDeces = "+" + str(diff_totalDeces)
	elif(diff_totalDeces == 0):
	    diff_totalDeces = "N/A"
	elif(diff_totalDeces < 0):
	    diff_totalDeces = "" + str(diff_totalDeces)

	if (diff_casReanimation > 0):
	    diff_casReanimation = "+" + str(diff_casReanimation)
	elif(diff_casReanimation == 0):
	    diff_casReanimation = "N/A"
	elif(diff_casReanimation < 0):
	    diff_casReanimation = "" + str(diff_casReanimation)

	if (diff_casHopital > 0):
	    diff_casHopital = "+" + str(diff_casHopital)
	elif(diff_casHopital == 0):
	    diff_casHopital = "N/A"
	elif(diff_casHopital < 0):
	    diff_casHopital = "" + str(diff_casHopital)

	if (diff_casGueris > 0):
	    diff_casGueris = "+" + str(diff_casGueris)
	elif(diff_casGueris == 0):
	    diff_casGueris = "N/A"
	elif(diff_casGueris < 0):
	    diff_casGueris = "" + str(diff_casGueris)

	if (diff_casMalades > 0):
	    diff_casMalades = "+" + str(diff_casMalades)
	elif(diff_casMalades == 0):
	    diff_casMalades = "N/A"
	elif(diff_casMalades < 0):
	    diff_casMalades = "" + str(diff_casMalades)

	if (diff_activeCases > 0):
	    diff_activeCases = "+" + str(diff_activeCases)
	elif(diff_activeCases == 0):
	    diff_activeCases = "N/A"
	elif(diff_activeCases < 0):
	    diff_activeCases = "" + str(diff_activeCases)

	if (diff_totalTests > 0):
	    diff_totalTests = "+" + str(diff_totalTests)
	elif(diff_totalTests == 0):
	    diff_totalTests = ""
	elif(diff_totalTests < 0):
	    diff_totalTests = "" + str(diff_totalTests)

	if (diff_todayCases > 0):
	    diff_todayCases = "+" + str(diff_todayCases)
	elif(diff_todayCases == 0):
	    diff_todayCases = "N/A"
	elif(diff_todayCases < 0):
	    diff_todayCases = "" + str(diff_todayCases)

	if (diff_casEhpad > 0):
	    diff_casEhpad = "+" + str(diff_casEhpad)
	elif(diff_casEhpad == 0):
	    diff_casEhpad = "N/A"
	elif(diff_casEhpad < 0):
	    diff_casEhpad = "" + str(diff_casEhpad)

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

	return (percentData)

def saveGouvData(data):
	with open(directory + 'data/oldGouvData.json', 'w') as fp:
		json.dump(data, fp)

def saveWorldometersData(data):
	with open(directory + 'data/oldWorldometersData.json', 'w') as fp:
		json.dump(data, fp)