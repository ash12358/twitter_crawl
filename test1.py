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
# tweets = []
# tweet=api.get_status("1034616710454624257")
# tweets.append(tweet)
count = 0

for tweet in tweepy.Cursor(api.search,
                           q="@realDonaldTrump",
                           # since="2018-1-1",
                           # until="2018-9-1"

                           ).items():
    count += 1
    if tweet.text.startswith('@realDonaldTrump'):
        print(tweet.id)
        print(tweet.created_at)
        print(tweet.in_reply_to_status_id)
        print(tweet.text)

print(count)

# tid = '998379986603032576'
# uid = '842210883652669440'
# query = 'likely video ms yeah'
#
# for results in tweepy.Cursor(api.search, q=query).items(100):
#     if 'retweeted_status' in dir(results):
#         print(results.retweeted_status.full_text)
#     else:
#         print(results.full_text)
#     print('=========')
    # print(str(results.in_reply_to_status_id_str))
    # if str(results.in_reply_to_status_id_str)=='998379986603032576':
    #     print(results.text)

# 打印其他用户主页上的时间轴里的内容
# tweets = api.user_timeline(screen_name='dNUoBHNbWMcr6EU', count=10, tweet_mode = 'extended')
#
# out_tweets = [[tweet.id, tweet.full_text, tweet.created_at, tweet.lang, tweet.place, tweet.geo, tweet.source,
#                                tweet.truncated, tweet.favorite_count, tweet.favorited, tweet.in_reply_to_screen_name,
#                                tweet.in_reply_to_status_id, tweet.in_reply_to_user_id, tweet.is_quote_status,
#                                tweet.retweet_count, tweet.retweeted, tweet.user.id, tweet.user.name, tweet.user.screen_name,
#                                tweet.user.statuses_count, tweet.user.time_zone, tweet.user.url, tweet.user.notifications,
#                                tweet.user.profile_background_image_url, tweet.user.profile_image_url,
#                                tweet.user.profile_image_url_https, tweet.user.location, tweet.user.contributors_enabled,
#                                tweet.user.created_at, tweet.user.default_profile, tweet.user.default_profile_image,
#                                tweet.user.description, tweet.user.favourites_count, tweet.user.follow_request_sent,
#                                tweet.user.followers_count, tweet.user.following, tweet.user.friends_count,
#                                tweet.user.geo_enabled] for tweet in tweets]
# #
# #
# for tweet in tweets:
#     print('==========================\n')
#     print('tweet.id', tweet.id,
#           '\ntweet.text', tweet.text,
#           '\ntweet.created_at', tweet.created_at,
#           # '\ntweet.lang',tweet.lang,
#           # '\ntweet.place',tweet.place,
#           # '\ntweet.geo',tweet.geo,
#           # '\ntweet.source',tweet.source,
#           # '\ntweet.truncated', tweet.truncated,
#           # '\ntweet.favorite_count', tweet.favorite_count,
#           # '\ntweet.favorited', tweet.favorited,
#           '\ntweet.in_reply_to_screen_name',tweet.in_reply_to_screen_name,
#           '\ntweet.in_reply_to_status_id', tweet.in_reply_to_status_id,
#           '\ntweet.in_reply_to_user_id', tweet.in_reply_to_user_id,
#           '\ntweet.is_quote_status',tweet.is_quote_status,
#           '\ntweet.retweet_count', tweet.retweet_count,
#           '\ntweet.retweeted', tweet.retweeted,
#           '\ntweet.user.id', tweet.user.id,
#           '\ntweet.user.name', tweet.user.name,
#           '\ntweet.user.screen_name',tweet.user.screen_name,
#           '\ntweet.user.statuses_count', tweet.user.statuses_count,
#           # '\ntweet.user.time_zone', tweet.user.time_zone,
#           # '\ntweet.user.url', tweet.user.url,
#           # '\ntweet.user.notifications',tweet.user.notifications,
#           # '\ntweet.user.profile_background_image_url', tweet.user.profile_background_image_url,
#           # '\ntweet.user.profile_image_url',tweet.user.profile_image_url,
#           # '\ntweet.user.profile_image_url_https', tweet.user.profile_image_url_https,
#           # '\ntweet.user.location', tweet.user.location,
#           # '\ntweet.user.contributors_enabled',tweet.user.contributors_enabled,
#           # '\ntweet.user.created_at', tweet.user.created_at,
#           # '\ntweet.user.default_profile', tweet.user.default_profile,
#           # '\ntweet.user.default_profile_image',tweet.user.default_profile_image,
#           # '\ntweet.user.description', tweet.user.description,
#           # '\ntweet.user.favourites_count', tweet.user.favourites_count,
#           # '\ntweet.user.follow_request_sent',tweet.user.follow_request_sent,
#           # '\ntweet.user.followers_count', tweet.user.followers_count,
#           # '\ntweet.user.following', tweet.user.following,
#           # '\ntweet.user.friends_count',tweet.user.friends_count,
#           '\ntweet.user.geo_enabled',tweet.user.geo_enabled)

# user_id = 'LeoDiCaprio'
# with open('./data/%s_tweets.csv' % user_id, 'w', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(out_tweets)
# print('saved data')