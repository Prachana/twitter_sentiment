#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:57:58 2017

@author: Rachana
"""

import tweepy
from textblob import TextBlob
from accesscodes import *

authorization = tweepy.OAuthHandler(consuer_key,consumer_secrect)
authorization.set_access_token(access_token,access_token_screct)

api = tweepy.API(authorization)

def userinput():
    topic = input('Enter a topic: ')
    public_tweet = api.search(topic)
    return public_tweet
   
def analysis():
    pub = userinput()
    for tweets in pub:
        print(tweets.text)
        ana = TextBlob(tweets.text)
        print(ana.sentiment)



analysis()
