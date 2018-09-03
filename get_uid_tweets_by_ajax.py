import requests
import json
from bs4 import BeautifulSoup

screen_name = 'ladygaga'

url = 'https://twitter.com/{}'
ajax_url = 'https://twitter.com/i/profiles/show/{}/timeline/tweets?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cookie': 'personalization_id="v1_rnJj2MK6g+pN1NxENEdoOg=="; guest_id=v1%3A153541979959731833; kdt=rqKKUguXAAUftBQuTPpAzbg71NRgf7aZAwIkzSRG; dnt=1; auth_token=57a6c70f672ef91e0d11e3787bb8187f4ce96213; csrf_same_site_set=1; csrf_same_site=1; lang=en; external_referer=padhuUp37zjgzgv1mFWxJ1GGR6w5wXXNb61MrkCjQoc%3D|0|8e8t2xd8A2w%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAp0WIBlAToHaWQiJWMz%250AMjFkMTI0MjQzZDM1YzRjYjFhZGQzM2UwOTJlYTEyOgxjc3JmX2lkIiUwYmZh%250AYmZjNTdhNGViZGMyYmVkYjFjZWJlNTQzMmExZA%253D%253D--328e54528e3256768462e8a31c58b567cf6dd561; _ga=GA1.2.1213323274.1535456623; tfw_exp=1; ct0=87805d15b680308c21507519a78cf2af',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Referer': 'https://twitter.com/realDonaldTrump/status/1035209068095434752'
}


def get_next_position(text):
    if text.startswith('{'):
        j = json.loads(text)
        return j['min_position']
    else:
        soup = BeautifulSoup(text, 'lxml')
        lis = soup.find_all('li', attrs={'class': 'js-stream-item stream-item stream-item '})
        li = lis[-1]
        data_item_id = li.get('data-item-id')
        return data_item_id

def save(screen_name, text):
    if not text.startswith('{'):
        filename = '{}_tweets_{}.txt'.format(screen_name, '1')
    else:
        filename = '{}_tweets_{}.txt'.format(screen_name, '2')
    with open('./'+filename, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')

if __name__ == '__main__':
    init_url = url.format(screen_name)
    q = requests.get(init_url, headers=headers)
    # print(q.text)
    save(screen_name, q.text)

    for _ in range(100):
        max_position = get_next_position(q.text)
        print(max_position)
        if max_position is None:
            break
        headers['Referer'] = init_url
        url = ajax_url.format(screen_name, max_position)
        # print(url)
        q = requests.get(url, headers=headers)
        print(q.text)
        save(screen_name, q.text)
