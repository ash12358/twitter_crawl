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

screen_name = 'elonmusk'
max_id = None
tweets = []
most = 3

def filter(new_tweets):
    filter_tweets = []
    for tweet in new_tweets:
        # 是回复的别人的
        if tweet.in_reply_to_status_id is not None:
            continue
        # 是转发的
        elif 'retweeted_status' in dir(tweet):
            continue
        # 必须是纯文本
        elif 'http' in tweet.full_text or '<a href' in tweet.full_text:
            continue
        else:
            filter_tweets.append(tweet)
    return filter_tweets


def get_tweets(api, screen_name, max_id):
    if len(tweets) > most:
        return
    new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=max_id, tweet_mode='extended')
    max_id = new_tweets[-1].id - 1
    new_tweets = filter(new_tweets)
    tweets.extend(new_tweets)
    get_tweets(api, screen_name, max_id)


if __name__ == '__main__':
    get_tweets(api, screen_name, max_id)
    for tweet in tweets:
        print(tweet.full_text)
        print(tweet.id)
