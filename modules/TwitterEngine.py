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


class TwitterEngine:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def is_there_a_last_tweet(self):
        last_tweet = self.api.user_timeline(
            id=get_config('TwitterAPI', 'user_id'), count=1)[0]
        last_tweet_date = datetime.datetime.strptime(
            str(last_tweet.created_at), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

        if todayDate == last_tweet_date and last_tweet.source == get_config('TwitterAPI', 'app_name'):
            return True  # Déjà tweeté

        return False  # On va chercher les données
