import tweepy

import time
def sendTweet(consumer_key, consumer_secret, access_token, access_token_secret, message):
  client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
  client.create_tweet(text=message, user_auth=True)

  
