import tweepy
from tweepy import OAuthHandler

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

# start = time.time()
#
# '''
# 1036052758389051392
# pass 2018-09-03 01:51:29 1035715271418413056
# pass 2018-09-03 01:51:28 1036024180087644160
# '''
# d = {}
#
# for tweet in tweepy.Cursor(api.search,
#                            q="to:"+screen_name,
#                            tweet_mode = 'extended'
#                            ).items(10):
#     # if tweet.in_reply_to_status_id == int(tid):
#     # d[tweet.in_reply_to_status_id] = d.get(tweet.in_reply_to_status_id, 0) + 1
#
#     if tweet.in_reply_to_status_id is None:
#         j = tweet._json
#         print(j)
#         print(j['in_reply_to_status_id'])
#         # d = tweet.__dict__
#         # for key in d:
#         #     print(key, d[key])
#         break
#     # for key in :
#     #     print(key, tweet[key])
#
# # for key in d:
# #     print(key, d[key])
# #
# # print(len(d))
#
# end = time.time()
# print('takes', end - start, 's')
str = "{'place': None, 'lang': 'en', 'favorited': False, 'id_str': '1036596879256170496', 'source': " \
      "'<a href='http://twitter.com/download/iphone' rel='nofollow'>Twitter for iPhone</a>', 'favorite_count" \
      "': 0, 'in_reply_to_screen_name': None, 'in_reply_to_status_id_str': None, 'id': 103659" \
      "6879256170496, 'entities': {'user_mentions': [{'screen_name': 'krassenstein', 'name': 'Brian Krass" \
      "enstein', 'id': 133938408, 'indices': [3, 16], 'id_str': '133938408'}, {'screen_name': 'realDonaldTrump'" \
      ", 'name': 'Donald J. Trump', 'id': 25073877, 'indices': [18, 34], 'id_str': '25073877'}], 'hashtags': [], 'sym" \
      "bols': [], 'urls': []}, 'display_text_range': [0, 140], 'in_reply_to_user_id_str': None, 'created_at': 'Mon Sep 03 " \
      "12:48:49 +0000 2018', 'is_quote_status': False, 'retweeted_status': {'place': None, 'lang': 'en', 'favorited': Fal" \
      "se, 'id_str': '1036576994924871685', 'retweet_count': 108, 'favorite_count': 839, 'in_reply_to_screen_name': 'real" \
      "DonaldTrump', 'in_reply_to_status_id_str': '1036576599771111424', 'id': 1036576994924871685, 'entities': {'user_menti" \
      "ons': [{'screen_name': 'realDonaldTrump', 'name': 'Donald J. Trump', 'id': 25073877, 'indices': [0, 16], 'id_str': '2" \
      "5073877'}], 'hashtags': [], 'symbols': [], 'urls': []}, 'display_text_range': [17, 166], 'in_reply_to_user_id_str': '25073877', 'created_at': 'Mon Sep 03 11:29:48 +0000 2018', 'is_quote_status': False, 'user': {'url': 'https://t.co/fRbnmnjpsE', 'profile_background_tile': False, 'profile_use_background_image': False, 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/979820353475117057/P1XFvbc2_normal.jpg', 'profile_sidebar_fill_color': '000000', 'id_str': '133938408', 'statuses_count': 42003, 'lang': 'en', 'friends_count': 494669, 'time_zone': None, 'following': False, 'screen_name': 'krassenstein', 'id': 133938408, 'entities': {'url': {'urls': [{'url': 'https://t.co/fRbnmnjpsE', 'display_url': 'about.me/brian_krassens…', 'indices': [0, 23], 'expanded_url': 'https://about.me/brian_krassenstein'}]}, 'description': {'urls': [{'url': 'https://t.co/GrHQUy3bo8', 'display_url': 'HillReporter.com', 'indices': [45, 68], 'expanded_url': 'http://HillReporter.com'}]}}, 'favourites_count': 21896, 'translator_type': 'none', 'profile_link_color': '1B95E0', 'profile_text_color': '000000', 'follow_request_sent': False, 'location': 'Fort Myers, FL', 'profile_image_url': 'http://pbs.twimg.com/profile_images/979820353475117057/P1XFvbc2_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/133938408/1521227193', 'created_at': 'Sat Apr 17 01:43:56 +0000 2010', 'utc_offset': None, 'geo_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url_https': " \
      "'https://abs.twimg.com/images/themes/theme1/bg.png', 'has_extended_profile': True, 'profile_sidebar_border_color': '000000', 'name': 'Brian Krassenstein', 'verified': False, 'followers_count': 518467, 'description': 'Outspoken critic of Donald Trump - Editor at https://t.co/GrHQUy3bo8 ------------------- Follow My Brother: @EdKrassen', 'contributors_enabled': False, 'listed_count': 3734, 'default_profile': False, 'default_profile_image': False, 'protected': False, 'is_translator': False, 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'is_translation_enabled': False, 'notifications': False}, 'in_reply_to_status_id': 1036576599771111424, 'geo': None, 'coordinates': None, 'full_text': '@realDonaldTrump If by progress you mean we are alienating our staunchest allies, while cozying up to our enemies, then yes, this is Progress... With a Capital RUSSIA', 'retweeted': False, 'in_reply_to_user_id': 25073877, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'truncated': False, 'contributors': None, 'source': '<a h" \
      "ref='http://twitter.com' rel='nofollow'>Twitter Web Client</a>'}, 'user': {'url': None, 'profile_background_tile': False, 'profile_use_background_image': True, 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1629104673/image_normal.jpg', 'profile_sidebar_fill_color': 'A0C5C7', 'id_str': '29269883', 'statuses_count': 2346, 'lang': 'en', 'friends_count': 192, 'time_zone': None, 'following': False, 'screen_name': 'Omsok', 'id': 29269883, 'entities': {'description': {'urls': []}}, 'favourites_count': 2469, 'translator_type': 'none', 'profile_link_color': 'FF3300', 'profile_text_color': '333333', 'follow_request_sent': False, 'location': 'Global', 'profile_image_url': 'http://pbs.twimg.com/profile_images/1629104673/image_normal.jpg', 'created_at': 'Mon Apr 06 19:11:20 +0000 2009', 'utc_offset': None, 'geo_enabled': False, 'profile_background_color': '709397', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme6/bg.gif', 'has_extended_profile': False, 'profile_sidebar_border_color': '86A4A6', 'name': 'Kosmo', 'verified': False, 'followers_count': 94, 'description': 'BPM consultant, observer, strategist.', 'contributors_enabled': False, 'listed_count': 5, 'default_profile': False, 'default_profile_image': False, 'protected': False, 'is_translator': False, 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme6/bg.gif', 'is_translation_enabled': False, 'notifications': False}, 'in_reply_to_status_id': None, 'geo': None, 'coordinates': None, 'full_text': 'RT @krassenstein: @realDonaldTrump If by progress you mean we are alienating our staunchest allies, while cozying up to our enemies, then y…', 'retweeted': False, 'in_reply_to_user_id': None, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'truncated': False, 'contributors': None, 'retweet_count': 108}"
str = str.replace('\'', '\"')
import json
j = json.loads(str)
print(j)
'''{"place": "", "lang": "en", "favorited": "", "id_str": "1036596879256170496", "source":
 "<a href='http://twitter.com/download/iphone' rel='nofollow'>Twitter for iPhone</a>", "favorite_count": 0, "in_reply_to_screen_name": "", "in_reply_to_status_id_str": "", "id": 1036596879256170496, "entities": {"user_mentions": [{"screen_name": "krassenstein", "name": "Brian Krassenstein", "id": 133938408, "indices": [3, 16], "id_str": "133938408"}, {"screen_name": "realDonaldTrump", "name": "Donald J. Trump", "id": 
25073877, "indices": [18, 34], "id_str": "25073877"}], "hashtags": [], "symbols": [], "urls": []}, "display_text_range": [0, 140], "in_reply_to_user_id_str": "", "created_at": "Mon Sep 03 12:48:49 +0000 2018", "is_quote_status": "", "retweeted_status": {"place": "", "lang": "en", "favorited": "", "id_str": "1036576994924871685", "retweet_count": 108, "favorite_count": 839, "in_reply_to_screen_name": "realDonaldTrump", "in_reply_to_status_id_str": "1036576599771111424", "id": 1036576994924871685, "entities": {"user_mentions": [{"screen_name": "realDonaldTrump", "name": "Donald J. Trump", "id": 25073877, "indices": [0, 16], "id_str": "25073877"}], "hashtags": [], "symbols": [], "urls": []}, "display_text_range": [17, 166], "in_reply_to_user_id_str": "25073877", "created_at": "Mon Sep 03 11:29:48 +0000 2018", "is_quote_status": "", "user": {"url": "https://t.co/fRbnmnjpsE", "profile_background_tile": "", "profile_use_background_image": "", "profile_image_url_https": "https://pbs.twimg.com/profile_images/979820353475117057/P1XFvbc2_normal.jpg", "profile_sidebar_fill_color": "000000", "id_str": "133938408", "statuses_count": 42003, "lang": "en", "friends_count": 494669, "time_zone": "", "following": "", "screen_name": "krassenstein", "id": 133938408, "entities": {"url": {"urls": [{"url": "https://t.co/fRbnmnjpsE", "display_url": "about.me/brian_krassens…", "indices": [0, 23], "expanded_url": "https://about.me/brian_krassenstein"}]}, "description": {"urls":
 [{"url": "https://t.co/GrHQUy3bo8", "display_url": "HillReporter.com", "indices": [45, 68], "expanded_url": "http://HillReporter.com"}]}}, "favourites_count": 21896, "translator_type": "", "profile_link_color": "1B95E0", "profile_text_color": "000000", "follow_request_sent": "", "location": "Fort Myers, FL", "profile_image_url": "http://pbs.twimg.com/profile_images/979820353475117057/P1XFvbc2_normal.jpg", "profile_banner_url": "https://pbs.twimg.com/profile_banners/133938408/1521227193", "created_at": "Sat Apr 17 01:43:56 +0000 2010", "utc_offset": "", "geo_enabled": "", "profile_background_color": "000000", "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", "has_extended_profile": "", "profile_sidebar_border_color": "000000", "name": "Brian Krassenstein", "verified": "", "followers_count": 518467, "description": "Outspoken critic of Donald Trump - Editor at https://t.co/GrHQUy3bo8 ------------------- Follow My Brother: @EdKrassen", "contributors_enabled": "", "listed_count": 3734, "default_profile": "", "default_profile_image": "", "protected": "", "is_translator": "", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "is_translation_enabled": "", "notifications": ""}, "in_reply_to_status_id": 1036576599771111424, "geo": "", "coordinates": "", "full_text": "@realDonaldTrump If by progress you mean we are alienating our staunchest allies, while cozying up to our enemies, then yes, this is Progress... With a Capital RUSSIA", "retweeted": "", "in_reply_to_user_id": 25073877, "metadata": {"iso_language_code": "en", "result_type": "recent"}, "truncated": "", "contributors": "", "source": "<a href='http://twitter.com' rel='nofollow'>Twitter Web Client</a>"}, "user": {"url": "", "profile_background_tile": "", "profile_use_background_image": "", "profile_image_url_https": "https://pbs.twimg.com/profile_images/1629104673/image_normal.jpg", "profile_sidebar_fill_color": "A0C5C7", "id_str": "29269883", "statuses_count": 2346, "lang": "en", "friends_count": 192, "time_zone": "", "following": "", "screen_name": "Omsok", "id": 29269883, "entities": {"description": {"urls": []}}, "favourites_count": 2469, "translator_type": "", "profile_link_color": "FF3300", "profile_text_color": "333333", "follow_request_sent": "", "location": "Global", "profile_image_url": "http://pbs.twimg.com/profile_images/1629104673/image_normal.jpg", "created_at": "Mon Apr 06 19:11:20 +0000 2009", "utc_offset": "", "geo_enabled": "", "profile_background_color": "709397", "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme6/bg.gif", "has_extended_profile": "", "profile_sidebar_border_color": "86A4A6", "name": "Kosmo", "verified": "", "followers_count": 94, "description": "BPM consultant, observer, strategist.", "contributors_enabled": "", "listed_count": 5, "default_profile": "", "default_profile_image": "", "protected": "", "is_translator": "", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme6/bg.gif", "is_translation_enabled": "", "notifications": ""}, "in_reply_to_status_id": "", "geo": "", "coordinates": "", "full_text": "RT @krassenstein: @realDonaldTrump If by progress you mean we are alienating our staunchest allies, while cozying up to our enemies, then y…", "retweeted": "", "in_reply_to_user_id": "", "metadata": {"iso_language_code": "en", "result_type": "recent"}, "truncated": "", "contributors": "", "retweet_count": 108}

'''