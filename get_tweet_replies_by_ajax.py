import requests
import json
from bs4 import BeautifulSoup

screen_name = 'MuseBuff'
tid = '1035203068877565953'


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cookie': 'personalization_id="v1_rnJj2MK6g+pN1NxENEdoOg=="; guest_id=v1%3A153541979959731833; kdt=rqKKUguXAAUftBQuTPpAzbg71NRgf7aZAwIkzSRG; dnt=1; auth_token=57a6c70f672ef91e0d11e3787bb8187f4ce96213; csrf_same_site_set=1; csrf_same_site=1; lang=en; external_referer=padhuUp37zjgzgv1mFWxJ1GGR6w5wXXNb61MrkCjQoc%3D|0|8e8t2xd8A2w%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAp0WIBlAToHaWQiJWMz%250AMjFkMTI0MjQzZDM1YzRjYjFhZGQzM2UwOTJlYTEyOgxjc3JmX2lkIiUwYmZh%250AYmZjNTdhNGViZGMyYmVkYjFjZWJlNTQzMmExZA%253D%253D--328e54528e3256768462e8a31c58b567cf6dd561; _ga=GA1.2.1213323274.1535456623; tfw_exp=1; ct0=87805d15b680308c21507519a78cf2af',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Referer': 'https://twitter.com/realDonaldTrump/status/1035209068095434752'
}
# headers['Referer'] = 'https://twitter.com/' + screen_name

first_request_url = 'https://twitter.com/{}/status/{}?conversation_id={}'
not_first_request_url = 'https://twitter.com/i/{}/conversation/{}?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false'

def get_first_request_url(screen_name, tid):
    return first_request_url.format(screen_name, tid, tid)

def get_not_first_request_url(screen_name, tid, max_position):
    return not_first_request_url.format(screen_name, tid, max_position)


def get_next_position(text):
    if (text.startswith('{"descendants')):
        j = json.loads(text)
        return j['descendants']['min_position']

    else:
        soup = BeautifulSoup(text, 'lxml')
        divs = soup.find_all('div', attrs={'class': 'stream-container '})
        div = divs[0]
        data_min_position = div.get('data-min-position')
        if len(data_min_position) != 0:
            return data_min_position
        else:
            buttons = soup.find_all('button', attrs={'class': 'ThreadedConversation-showMoreThreadsButton u-textUserColor'})
            if len(buttons) != 0:
                button = buttons[0]
                return button.get('data-cursor')
            else:
                return None

        # q = text.find('data-min-position')
        # q += 19
        # p = text.find('"', q)
        # return text[q: p]


def save(tid, text):
    if not text.startswith('{"descendants'):
        filename = '{}_replies_{}.txt'.format(tid, '1')
    else:
        filename = '{}_replies_{}.txt'.format(tid, '2')
    with open('./'+filename, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')


if __name__ == '__main__':



    url = get_first_request_url(screen_name, tid)
    headers['Referer'] = 'https://twitter.com/' + screen_name
    q = requests.get(url, headers=headers)
    q.encoding = 'utf-8'
    save(tid, q.text)

    while True:
        max_position = get_next_position(q.text)

        if max_position is None:
            break
        print(max_position)
        url = get_not_first_request_url(screen_name, tid, max_position)
        '''
        注意max_position=null的情况，表示没有了
        '''
        headers['Referer'] = 'https://twitter.com/{}/status/{}'.format(screen_name, tid)
        q = requests.get(url, headers=headers)
        q.encoding = 'utf-8'
        save(tid, q.text)

    # url = 'https://twitter.com/i/realDonaldTrump/conversation/1035209068095434752?include_available_features=1&include_entities=1&max_position=DAACDwABCgAAALgOXndhIhTgAA5dzYWiF4AADl5xhwtUcAAOXc4vitfgAw5eSQWRVGAADl3NeBjXoAAOXqz7H9UAAA5d0PuWl7ABDl3NQ4cX0AUOXoRqjdTgAA5eewXy1uAADl6cpOjU0AEOXm5s6JUAAQ5efUExVsAADl56L6nV4AAOXn-eKdWwAA5edbRdFNAADl6ZxwQV4AAOXsHWI1eAAQ5elAj3lOAADl54geTU8AAOXrQNN1WwAA5ebb_s1rAADl6S7zdW0AEOXo7dT9ewAA5edzkl1sAADl63JUvXsAAOXqglqxfQAA5ec_ePleAADl6GgqeW0AUOXm8DcNbgAQ5etg_FFuAADl60xWEW4AAOXpWQUdbgAA5ex4xtFMAADl5-yC9UcAUOXqNAzVfQAQ5eyte6F3ABDl65GdzU0AAOXrqtxtegAg5d5MgkVMAADl50-yFUUAAOXpSS7hTwAA5eqGbL14AADl65eHQW0AUOXqKbB9bAAA5eeXt0FMABDl6yfyPXoAAOXsYvAtfgAQ5euCVsl3AADl7NUqCXsAAOXoQ6GtfQBQ5ebGydFPABDl5716LU4AIOXs_3_5awAQ5euIdBV6AADl6_Gf_WwAcOXryAFFfQAA5ecphwlPABDl7KPprXcAAOXrTLJ1awBg5eexIzF-ABDl6IZV6XsAEOXm1arReAAQ5eqhg-l4ACDl7K0pgXsAEOXn9B4pdwAA5eyXS91tAFDl7Qu_hX0AAOXrcEXtRQAA5eb2aj1uAADl7Iy7yUUAEOXrfOOFbQAA5evqywluABDl5t1aiXsAUOXnKa8ZRQAQ5esdeF1PABDl60WCLW4AAOXrkpUFRQAA5ef1k31tABDl6Y4mVX4AAOXrWzFReAAg5egln_ltAADl59kG-VsAAOXrZoBNeAAA5etjANl6AADl6So7wW0AAOXps_ANawAA5ecGDTVFACDl6XoceU8AAOXpxwD1RgAA5etlSKFuABDl51FNZXoAcOXmyjRdbgAA5el7X0FGAADl69o7iWwAEOXrtQspTABQ5en9eWVsABDl7JdPwX4AAOXsa4-1egAA5efVQz1-AADl687wQVsAEOXtAUOtewAQ5epjk_1FAADl658BKWwAMOXsuDPVawAA5erYIHF7AADl7NxJuXoAAOXc73N5XgAA5ecfUC16AADl7IUejX0AEOXtIpQxdwAA5ejhEXlNAADl7JKywXsAEOXsdnjtbAAA5ezQfiFtAADl6BrVUVsAAOXsJ__ZewAA5epft11tABDl7MRe0VsAAOXn8HxlWwAA5ejFmjFHAADl7OfUDXoAEOXsmrBFegAA5efonHVPABDl7RteOV4AYOXslKStbgAQ5eeRWxlFAADl58d0_XsAAOXplYzBbQAA5ezWPZF4AADl6wiUhUYAEOXnnPrRTwAA5ei364l9AADl6KTOiVsAAOXow8JxRgAA5e0CzFVtAADl7DaAwU0AAOXtCn0xawAg5efOOWl6ABDl6lubeVsAAOXtGQLhawAA5enGVPFbAADl6_aJ3X0AEOXrp9UlfgAQ5emdOtV9AADl7Ivy7WsAIOXqLYpBfgAQ5ex0Orl-AADl7MwcNWsAAOXr3Jm1UAAA5egs6GFeABDl7H_SvXsAAOXr7aKRfgAA5ecfisFQAADl7NRfcXoAAOXpq-BdRgAA5ejX3Xl7AADl7R26ZW4AAOXsv1KtfgAA5eqWidF9AADl7PyIpW0AAOXraXelfQAA5e0e-ylbAADl6CLTnX0AAOXsKVUxawBQ5exAzm1OABDl3ntBCUYAEOXq5wPlbQAQ5ezQIOlsAFDl67shDX4AEOXn8PJtbgAQ5ex-a61sAADl7ALT9X0AAOXnoTCNawAw5ehkV6V4AADl6WfZDW4AIOXnZoOxawAA5etk8ml3AADl7NNk4XcAAOXsmLURbgAQ5ekhawF-AADl7DchYXgAIOXr5fHlfQAAgAAwAAAAECAAQAAAA&reset_error_state=false'
    # headers['Referer'] = 'https://twitter.com/{}/status/{}'.format(screen_name, tid)
    # q = requests.get(url, headers=headers)
    # print(q.text)




