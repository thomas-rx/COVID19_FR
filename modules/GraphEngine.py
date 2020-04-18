#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
import matplotlib

from modules.ConfigEngine import getConfig
# Importation des librairies.
import matplotlib

from modules.ConfigEngine import getConfig

matplotlib.matplotlib_fname()
'/etc/matplotlibrc'
matplotlib.use('Agg')
import csv
import matplotlib.pyplot as plt
import datetime


directory = getConfig('System', 'directory')

def makeGraph():
	days = []
	totalCases = []
	hospitalizationCases = []
	severeCases = []
	deadCases = []
	recoveredCases = []
	sickCases = []

	with open(directory + 'data/graphData.txt','r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			days.append(int(row[0]))
			totalCases.append(int(row[1]))
			hospitalizationCases.append(int(row[2]))
			severeCases.append(int(row[3]))
			deadCases.append(int(row[4]))
			recoveredCases.append(int(row[5]))
			sickCases.append(int(row[1]) - (int(row[4]) + int(row[5])))

	plt.style.use('seaborn-talk')

	#plt.plot(totalCases, label=u'Cas totaux confirmés', marker='o',color = 'darkorange', linewidth = 4)

	plt.plot(sickCases, label=u'Population activement malade',  marker='o', color = 'darkorange', linewidth = 4)

	plt.plot(hospitalizationCases, label=u'Population activement hospitalisée', marker='o',color = 'indianred', linewidth = 4)

	plt.plot(severeCases, label=u"Population en réanimation", marker='o',color = 'maroon', linewidth = 4)

	plt.plot(recoveredCases, label=u'Population guérie',  marker='o', color = 'yellowgreen', linewidth = 4)

	plt.plot(deadCases, label=u"Population décédée",  marker='o',color = 'dimgray', linewidth = 4)

	currentDT = datetime.datetime.now()
	#plt.ylabel(u'Graphique généré le ' + currentDT.strftime("%d-%m-%Y %H:%M:%S") + ' Par @COVID_France', fontsize = 7)
	plt.xlabel(u'Jours à partir du Mardi 17 Mars 2020 - [Confinement]')
	plt.title(u'AVANCÉE DU COVID-19 EN FRANCE\n' + currentDT.strftime("%d") + u' Avril 2020', fontweight='bold')
	plt.legend(prop={'size': 11}, labelspacing=1.1)
	plt.grid(color='black', linestyle='dashed', linewidth=1)

	plt.savefig(directory + 'data/graphIMG.png', format='png', dpi=200)

def saveDataGraph(totalCases, sickCases, severeCases, deadCases, recoveredCases):
	dataGraph = open(directory + 'data/graphData.txt', 'a')
	dataGraph.write("0," + str(totalCases) + "," + str(sickCases) + "," + str(severeCases) + "," + str(deadCases) + "," + str(recoveredCases) + "\n")
	dataGraph.close()