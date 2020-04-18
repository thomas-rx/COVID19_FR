#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import tweepy
import datetime

from modules.ConfigEngine import get_config

todayDate = datetime.datetime.now().strftime("%Y-%m-%d")  # Date du jour
# todayDate = dateSelected = '2020-04-10'

account_id = get_config('TwitterAPI', 'user_id')
consumer_key = get_config('TwitterAPI', 'consumer_key')
consumer_secret = get_config('TwitterAPI', 'consumer_secret')
access_token = get_config('TwitterAPI', 'access_token')
access_token_secret = get_config('TwitterAPI', 'access_token_secret')


def twitter_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api, auth


def get_last_tweet():
    api, auth = twitter_auth()
    last_tweet = api.user_timeline(id=get_config('TwitterAPI', 'user_id'), count=1)[0]
    last_tweet_date = datetime.datetime.strptime(str(last_tweet.created_at), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

    if todayDate == last_tweet_date and last_tweet.source == get_config('TwitterAPI', 'app_name'):
        return 1  # Déjà tweeté
    else:
        return 0  # On va chercher les données
