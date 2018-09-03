import tweepy
from tweepy import OAuthHandler
import csv
count = 0
import time
consumer_key = 'jQbV18avasn3m1B9JyTsNFBgj'
consumer_secret = '6vkouRGqpB1oZ4scQaTwDPVofz18vMY7Y0lZzCfkMIL1IPfZbE'
access_token = '950374150958284800-fD4YotFzkNcYC2RjPnVGubMnf4W4fHW'
access_secret = 'IMr2yl2GBcjERH8OaQYsH6R7PG06NJkk2wxWTp5pszfyk'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

screen_name = 'realDonaldTrump'
tid = '1030116078125568006'

def save(tweet):
    with open('aaa.txt', 'a', encoding='utf-8') as f:
        f.write(str(tweet))
        f.write('\n')

start = time.time()

'''
1036052758389051392
pass 2018-09-03 01:51:29 1035715271418413056
pass 2018-09-03 01:51:28 1036024180087644160
'''

for tweet in tweepy.Cursor(api.search,
                           q="to:"+screen_name,
                           since_id=1035715271418413056,
                           tweet_mode = 'extended'
                           ).items():
    # save(tweet)
    if tweet.in_reply_to_status_id == int(tid):
        # print(tweet.created_at, tweet.id, tweet.full_text)
        # print(tweet.__dict__)

        save(tweet.__dict__)
        count += 1
        print(count)
        if count > 5000:

            break
    else:
        print('pass', tweet.created_at, tweet.in_reply_to_status_id)

end = time.time()
print('takes', end - start, 's')
