from bs4 import BeautifulSoup
import lxml
import json
import os
tid = '1035203068877565953'
count = 0
def get_html_from_1(tid):
    html = ''
    filename = '{}_replies_1.txt'.format(tid)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                html += line
    return html

def get_htmls_from_2(tid):
    htmls = []
    # filename = '{}_replies_2.txt'.format(tid)
    filename = 'to_realDonaldTrump_replies_2.txt'
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            j = json.loads(line.strip())
            htmls.append(j['inner']['items_html'])
    return htmls

d = {}

def get_replies(html):
    global count
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find_all('div', attrs={'class': 'tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet '})
    if len(divs) == 0:
        print('[][]')
    for div in divs:
        data_conversation_id = div.get('data-conversation-id')
        # print(data_conversation_id)
        d[data_conversation_id] = d.get(data_conversation_id, 0) + 1

        # if data_conversation_id == '1036024180087644160':
        p = div.find('p', attrs={'class': 'TweetTextSize js-tweet-text tweet-text'})
        # print(p.text)
        count += 1

    # p_class = ['TweetTextSize', 'js-tweet-text', 'tweet-text']
    # ps = soup.find_all('p')
    # for p in ps:
    #      if p.get('class') == p_class:
    #          print(p.text)
    #          count += 1



if __name__ == '__main__':
    # html = get_html_from_1(tid)
    # get_replies(html)
    htmls = get_htmls_from_2(tid)
    for html in htmls:

        get_replies(html)

    print(len(d))
    for key in d:
        print(key, d[key])
    print('len htmls', len(htmls))
    print('count', count)