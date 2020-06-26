#!/usr/bin/env python
# coding: utf-8

# Twitter: @xrths
# www.xrths.fr

# Importation des librairies.
import tweepy
import datetime

from modules.ConfigEngine import TwitterAPIConfig

todayDate = datetime.datetime.now().strftime("%Y-%m-%d")  # Date du jour
# todayDate = dateSelected = '2020-04-10'


class TwitterEngine:
    def __init__(self, twitter_conf):
        self.twitter_conf = twitter_conf
        self.auth = tweepy.OAuthHandler(
            twitter_conf.consumer_key, twitter_conf.consumer_secret)
        self.auth.set_access_token(
            twitter_conf.access_token, twitter_conf.access_token_secret)
        self.api = tweepy.API(self.auth)

    def is_there_a_last_tweet(self):
        last_tweet = self.api.user_timeline(
            id=self.twitter_conf.user_id, count=1)[0]
        last_tweet_date = datetime.datetime.strptime(
            str(last_tweet.created_at), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

        if todayDate == last_tweet_date and last_tweet.source == self.twitter_conf.app_name:
            return True  # Déjà tweeté

        return False  # On va chercher les données
