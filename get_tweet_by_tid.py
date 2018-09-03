import tweepy
from tweepy import OAuthHandler
import csv

consumer_key = 'f1QZM6slbiVcijq8zw8L4b2gH'
consumer_secret = 'tAosUplXlh58DPUNcx7w20LzCjUNFx0IxqrAQix9sXUQMbAX20'
access_token = '902455573580365825-7fkiGLczuu1EQAoxdRaSmkNhTqg9vQY'
access_secret = 'VhKhro4OWR9zYJUiNNW1PF6F5TP5D1b3m1HYKealq05rX'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

screen_name = 'realDonaldTrump'
tid = '1036225531367178240'

tweet = api.get_status(tid, tweet_mode = 'extended')
print(tweet.full_text)
print(tweet.created_at)
print(tweet.user.screen_name)
