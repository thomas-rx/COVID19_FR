#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
from datetime import datetime
from ConfigEngine import *

def getDays():
	containmentDate = datetime(2020, 3, 17) #Confinement
	todayDate = datetime.today()

	numberOfDays = str(todayDate - containmentDate)
	numberOfDays = str([int(s) for s in numberOfDays.split() if s.isdigit()])
	numberOfDays = numberOfDays.replace('[', '')
	numberOfDays = numberOfDays.replace(']', '')
	numberOfDays = int(numberOfDays) + 1 #Le confinement a débuté à midi.

	return(str(numberOfDays))

def checkTime():
	if(getConfig('System', 'checkTime') == 'True'):
		getTimeNow = datetime.now().strftime("%H:%M")

		startTime = datetime.strptime(getConfig('System', 'startTime'), '%H:%M')
		startTime = startTime.strftime('%H:%M')

		endTime = datetime.strptime(getConfig('System', 'endTime'), '%H:%M')
		endTime = endTime.strftime('%H:%M')

		if(getTimeNow > startTime and getTimeNow < endTime): 
			return(True) 
		else:
			return(False)
	else:
		return(True)