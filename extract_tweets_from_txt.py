from bs4 import BeautifulSoup
import lxml
import json
import os

screen_name = 'realDonaldTrump'
count = 0
lis = []

def get_html_from_1(screen_name):
    html = ''
    filename = '{}_tweets_1.txt'.format(screen_name)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                html += line
    return html

def get_htmls_from_2(screen_name):
    htmls = []
    filename = '{}_tweets_2.txt'.format(screen_name)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            j = json.loads(line.strip())
            htmls.append(j['items_html'])
    return htmls

def get_replies(html):
    global count
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    # p_class = ['TweetTextSize', 'js-tweet-text', 'tweet-text']

    # ps = soup.find_all('p', attrs={'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
    # for p in ps:
    #     print(p.text)
    #     count += 1

    lis.extend(soup.find_all('li', attrs={'class': 'js-stream-item stream-item stream-item js-pinned '}))
    lis.extend(soup.find_all('li', attrs={'class': 'js-stream-item stream-item stream-item '}))


def fileter(lis):
    new_lis = []
    for li in lis:
        contexts = []
        contexts.extend(li.find_all('span', attrs={'class': 'js-retweet-text'}))
        contexts.extend(li.find_all('div', attrs={'class': 'ReplyingToContextBelowAuthor'}))
        # print(contexts)
        # 是转发的或者回复的
        if len(contexts) > 0:
            continue
        p = li.find('p', attrs={'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
        text = p.text
        if 'http' in text or '<a href' in text:
            continue
        new_lis.append(li)
    return new_lis




if __name__ == '__main__':

    html = get_html_from_1(screen_name)
    get_replies(html)
    htmls = get_htmls_from_2(screen_name)
    for html in htmls:
        get_replies(html)
    print(len(lis))
    lis = fileter(lis)
    for li in lis:
        print(li.find('p', attrs={'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'}).text)
    print(len(lis))

