#!/usr/bin/env python
# coding: utf-8

#Twitter: @xrths
#www.xrths.fr

#Importation des librairies.
from datetime import datetime

import tweepy

from modules.ConfigEngine import getConfig

todayDate = datetime.datetime.now().strftime("%Y-%m-%d") #Date du jour
#todayDate = dateSelected = '2020-04-10'

account_id = getConfig('TwitterAPI', 'user_id')
consumer_key = getConfig('TwitterAPI', 'consumer_key')
consumer_secret = getConfig('TwitterAPI', 'consumer_secret')
access_token = getConfig('TwitterAPI', 'access_token')
access_token_secret = getConfig('TwitterAPI', 'access_token_secret')


def TwitterAuth():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api,auth


def getLastTweet():
	api, auth = TwitterAuth()
	lastTweet = api.user_timeline(id = getConfig('TwitterAPI', 'user_id'), count = 1)[0]
	lastTweetDate = datetime.datetime.strptime(str(lastTweet.created_at), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

	if(todayDate == lastTweetDate and lastTweet.source == getConfig('TwitterAPI', 'app_name')):
   		return 1 #Déjà tweeté
	else:
   		return 0 #On va chercher les données