#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
from configparser import SafeConfigParser

def getConfig(section, option):
	parser = SafeConfigParser()
	parser.read('/VotreDirectory/COVID19-France/' + 'config.ini') #Modifier cette ligne.
	return(parser.get(section, option))