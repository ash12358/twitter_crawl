import requests
import json
from bs4 import BeautifulSoup

screen_name = 'realDonaldTrump'

url = 'https://twitter.com/i/search/timeline?vertical=default&q=to%3ArealDonaldTrump%20since%3A2018-08-25%20until%3A2018-08-30&src=typd&include_available_features=1&include_entities=1&max_position={}&reset_error_state=false'
max_position = 'TWEET-1034952835899617280-1034952835899617280-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWACAAAABIEAAggAAACEAAgAABAAAAACAAAAACAAEACAAAAAAAAQAAEAAAAACAQkAABAAAAAogAAAAQAAgQAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAAAAAQAAAQAIAAAAAAAAAAAAAAAQIAAAAEAAAAAAAAAAAAAAAAIggAABAAAIAAAABAAQAAAAAAAAAAAAAAAAIABAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAASEEACAQAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAgAAAAAgAAABACAAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAgAAAAQAAAAAAAAgACAAAAAAAAAAAABAAAAQEACAAAAAAAAAAAAAAAAAAAAIEAAAAgAAAUAAAAAQAgAEAAAIAAAgEAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAEAAAAAAAAAAAlAEQAAAAAAQAABAAAAAEAAAAAAAAAACAAAAgAAAAAAAAAAAAAAAAAAIAgAAAAAAAAAAAAABAAAAAAAAACAAAAAAAgAAAAAEAABACAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAQAAAAAABAAAAABAAAAAAIAAAAAAAAQAAAAAAAAEAgCABAAAAAAAgAAAAAAAAIAAAAAAAAgAAAAAAABAAAggAAAAAAAAAAAAAAIAAAAAAAAAAACAAAAAABAAAAAAAAAAAAAAEAAAwAAAAAAAAAAAAAAACQAAIAAEAAAAAAAAAAAAAAAAAACAAAEAAAAAAAAAAAAAAgAAACAAAAAAAAAAAAAAAAgAQAAAAAAAAAIAAAAAAAABAEAAAAAAAAAAAAAAAAAABAAAAAAAIAAAAAACAAAAAAAAAAAAAAAAABA==-R-0-0'
max_position = max_position.replace('+', '%2B')
max_position = max_position.replace('=', '%3D')
print(max_position)
ajax_url = url.format(max_position)
# ajax_url = url

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cookie': 'kdt=rqKKUguXAAUftBQuTPpAzbg71NRgf7aZAwIkzSRG; dnt=1; csrf_same_site_set=1; csrf_same_site=1; lang=en; _ga=GA1.2.1213323274.1535456623; tfw_exp=0; remember_checked_on=1; personalization_id="v1_VI24wAUaKCVKVcHM2w+mIw=="; guest_id=v1%3A153580874898423511; ads_prefs="HBISAAA="; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAp0WIBlAToHaWQiJWMz%250AMjFkMTI0MjQzZDM1YzRjYjFhZGQzM2UwOTJlYTEyOgxjc3JmX2lkIiUwYmZh%250AYmZjNTdhNGViZGMyYmVkYjFjZWJlNTQzMmExZDoJdXNlcmwrCPjjCh4BAA%253D%253D--bdd1168782f4b9603fe1a1ddf5f2d1a10b56a8eb; twid="u=4798997496"; auth_token=e21625961bc2c1ea1c254647c7f36b5a4c693e86; external_referer=4bfz%2B%2BmebEmxs9tOACw5kbtMrnLo4LI%2F|0|8e8t2xd8A2w%3D; ct0=a27118693117e31e2f72e610686815e2',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Referer': 'https://twitter.com/search?l=&q=to:realDonaldTrump%20since:2018-08-25%20until:2018-08-30&src=typd',
    'X-requested-with': 'XMLHttpRequest',
    'X-twitter-active-user': 'yes'
}


def get_next_position(text):
    j = json.loads(text)
    # if j['inner']['has_more_items'] == False:
    #     return None
    max_position = j['inner']['min_position']
    return max_position


def get_min_position(text):

    positions = []

    j = json.loads(text)
    html = j['inner']['items_html']
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', attrs={'class': 'js-stream-item stream-item stream-item '})
    for li in lis:
        positions.append(li.get('data-item-id'))

    # print(positions)
    positions.sort()
    # print(positions)
    return positions[0]

def save(screen_name, text):
    if not text.startswith('{'):
        filename = 'to_{}_replies_{}.txt'.format(screen_name, '1')
    else:
        filename = 'to_{}_replies_{}.txt'.format(screen_name, '2')
    with open('./'+filename, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')

if __name__ == '__main__':
    uuu = 'https://twitter.com/i/search/timeline?vertical=default&q=to%3ArealDonaldTrump%20since%3A2018-08-25%20until%3A2018-08-30&src=typd&include_available_features=1&include_entities=1&max_position={}&reset_error_state=false'
    max_position_pattern = 'TWEET-{}-1034952835899617280'
    max_position = max_position_pattern.format('1034952835899617280')
    max_position = max_position.replace('+', '%2B')
    max_position = max_position.replace('=', '%3D')
    ajax_url = uuu.format(max_position)
    q = requests.get(ajax_url, headers=headers)
    print(q.text)
    save(screen_name, q.text)


    for i in range(200):
        min_position = get_min_position(q.text)
        # print(min_position)
        max_position = max_position_pattern.format(min_position)
        max_position = max_position.replace('+', '%2B')
        max_position = max_position.replace('=', '%3D')
        print(max_position)
        ajax_url = uuu.format(max_position)
        q = requests.get(ajax_url, headers=headers)
        print(q.text)
        save(screen_name, q.text)


    # save(screen_name, q.text)
    # old_position = max_position
    # for i in range(3000):
    #     max_position = get_next_position(q.text)
    #     if max_position is None:
    #         print(max_position)
    #         break
    #     if max_position == old_position:
    #         break
    #     old_position = max_position
    #     max_position = max_position.replace('+', '%2B')
    #     max_position = max_position.replace('=', '%3D')
    #     print(max_position)
    #     ajax_url = url.format(max_position)
    #     q = requests.get(ajax_url, headers=headers)
    #     print(q.text)
    #     save(screen_name, q.text)
    #     print(i)

    # a = 'TWEET-1035920891866169344-1036040993571663872-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWSbDVRAE4CwAIBkFCQFakEACGVBHDA0YdE0lyEIAQJOJ0yYJkIMTkAR2imBAdVyE6kB0AoYBRMgaMQAgQiAZDABPEALsERVgEDbEFcAAGECUIEKYAQDigEsAQQjD+KAAgLEFg3JAWogsAAgFLwCATAEAQGAQYIEWomAlEPCoAKCIeWmMlPiWimQAEUGoQTmoYKACmHSBhg8bUBTArEqsEyAPpCoBiNkCBSAAAEp4YY2EQShMgOAhB4JdADUEmDiAINFwEvLBAC4wQkXiwYBUE8uBmAIDIAACAEiSRBAAOUACRXAFRyESoAAhM4AaIKWwCgDQZhECgwgeJCgEgBwgBc1EnEBB5BhRDEEQIIGqAAWCKVEgKQJQDQwWJQAnFAhJAlGFAwZTICrBDkssAAEgAikQICMQiMIgAAyoRCKlAFBHDUBCCmhGYDASaRYQB01CEK9ExCYo0AhosCkFgIEoB3WGgyMAeAXQSWA7AaQEQwuAYmckKFFBAyYyZCUQCkQhQogHQhBqQxCyVANEABAQgwjByrIkAETIAtAOImggQVBFAASqIwo4KFAwKgaCRZKIQKbYW0KCIJDgf4QgQEBA1QA7IZAYgYMAAQS00IQDCIESKDIRRAAkMACCwVCCCgAhAGKAAhhYiwGBUCSYCBIPJIJ4AYEPgESFBJyCyIYBiAFUgAgADEZoAACBARUDJBqAEHERUEMiFRoCQAYCJAwEAWEKpBBABUcYiCMAQACRYKAB4aJAIAAsBCYBAKcYCSggMRMAJDiBYMTsQRksCAgONoQecSJAgoAQAQgpzFUKIAEEYCieADQKkCqAAKxhRACgUBM5FMASPAVBXiAmioe8hhecqCLOAQDBNZaQCDMeEGLAICAIKwQAgAyBCBhMUkFGmKEZQIkqAMAEAAKYbGRgSVQ==-T-0-13'
    # b = 'TWEET-1035920891866169344-1036040993571663872-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWSbDVRAE4CwAIBkFCQFakEACGVBHDA0YdE0lyEIAQJOJ0yYJkIMTkAR2imBAdVyE6kB0AoYBRMgaMQAgQiAZDABPEALsERVgEDbEFcAAGECUIEKYAQDigEsAQQjD+KAAgLEFg3JAWogsAAgFLwCATAEAQGAQYIEWomAlEPCoAKCIeWmMlPiWimQAEUGoQTmoYKACmHSBhg8bUBTArEqsEyAPpCoBiNkCBSAAAEp4YY2EQShMgOAhB4JdADUEmDiAINFwEvLBAC4wQkXiwYBUE8uBmAIDIAACAEiSRBAAOUACRXAFRyESoAAhM4AaIKWwCgDQZhECgwgeJCgEgBwgBc1EnEBB5BhRDEEQIIGqAAWCKVEgKQJQDQwWJQAnFAhJAlGFAwZTICrBDkssAAEgAikQICMQiMIgAAyoRCKlAFBHDUBCCmhGYDASaRYQB01CEK9ExCYo0AhosCkFgIEoB3WGgyMAeAXQSWA7AaQEQwuAYmckKFFBAyYyZCUQCkQhQogHQhBqQxCyVANEABAQgwjByrIkAETIAtAOImggQVBFAASqIwo4KFAwKgaCRZKIQKbYW0KCIJDgf4QgQEBA1QA7IZAYgYMAAQS00IQDCIESKDIRRAAkMACCwVCCCgAhAGKAAhhYiwGBUCSYCBIPJIJ4AYEPgESFBJyCyIYBiAFUgAgADEZoAACBARUDJBqAEHERUEMiFRoCQAYCJAwEAWEKpBBABUcYiCMAQACRYKAB4aJAIAAsBCYBAKcYCSggMRMAJDiBYMTsQRksCAgONoQecSJAgoAQAQgpzFUKIAEEYCieADQKkCqAAKxhRACgUBM5FMASPAVBXiAmioe8hhecqCLOAQDBNZaQCDMeEGLAICAIKwQAgAyBCBhMUkFGmKEZQIkqAMAEAAKYbGRgSVQ==-T-0-13'
    # print(a == b)
    # for i in range(len(a)):
    #     if a[i] == b[i]:
    #         pass
    #     else:
    #         print(i)

    '''
    TWEET-1035575429640474627-1036040993571663872-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWSbDVRAE4GwAIBkFCQFakAAHGVBHDA0ZdE8lyEKAQIOJ0T6JgaMTkAR2imBAdVyE6kB0AoYFRMgaMUAgQiAZDABPMALtERVgELbEFcEBHECUMEKYIQDigMoAQQjj%2BKAAhLEFg3JA2og8AAgNLwKATAEAQGAQYIEWomAlFPCoAKCIeWmMlPiWimQAEVGoQTmoYKACmnSAhg4bQBTgrEqsEyAPpAoBqNkCjSAAAEh4YY2EQylMgOAhB4ZdICUEmDiAINFwUvLhAC4wQkXiwYBUE8uBkAIDIAACAEiSRBAAOUACRfAFRyESpQQhM4AaIKWwCwDQZpECg4geJCgEgBwgBc1EnEBh5BhRDUkQIIGqAAWCKVEkKQJQDQy2JQAnFAhIAlGFAwRTIDpBDmssACEggi0QICMQiMIgAAyoRKOlAFBHDUBCLmhWYDASaRYUB01CAK9E1CYokAhosCkFgoEoBzVWgyIQeAXRSWArAaQEQyuBamcmKFFBAyYyZCUQCkQhQogHQhBqQxCyVANEABEQgwjB2rMkAETIAtAOIiggQVBFAAS6Iwo4qFAwKobCRZKIQKbYW2CCINDgf4QgQEBAxYA7IZAYgYMAAQS20cQDCIESKDIRRAAkMACCwVGDCgABAHKAAhhYiwGBVCSYCBIPJMJwBYUPgESFBIyCyIYRiAB0gAgADEZoYACBAR0DJBqAEHERUEMiFRoCYSYDpAwEAWEKpBBABQcYiCMAwAKBYqAR46BAIQAsBCYBAKcZCykAIRMAJzyBYOTsQRksGAgONoSecSJAgowQAQgpzFUIIgEEYCiWRTQKsCqAEKxhVACgUBM9FMASPAUBXiA2ioe8hhecqSLOAQDBNZa0CDMfEHrAISAIKwQAgAyBCBhMUkFG2KEZQIlqAsAEAAKYbGRgSUQ%3D%3D-T-0-33&reset_error_state=false
    TWEET-1035575429640474627-1036040993571663872-BD1UO2FFu9QAAAAAAAAVfAAAAAcAAABWSbDVRAE4GwAIBkFCQFakAAHGVBHDA0ZdE8lyEKAQIOJ0T6JgaMTkAR2imBAdVyE6kB0AoYFRMgaMUAgQiAZDABPMALtERVgELbEFcEBHECUMEKYIQDigMoAQQjj%2BKAAhLEFg3JA2og8AAgNLwKATAEAQGAQYIEWomAlFPCoAKCIeWmMlPiWimQAEVGoQTmoYKACmnSAhg4bQBTgrEqsEyAPpAoBqNkCjSAAAEh4YY2EQylMgOAhB4ZdICUEmDiAINFwUvLhAC4wQkXiwYBUE8uBkAIDIAACAEiSRBAAOUACRfAFRyESpQQhM4AaIKWwCwDQZpECg4geJCgEgBwgBc1EnEBh5BhRDUkQIIGqAAWCKVEkKQJQDQy2JQAnFAhIAlGFAwRTIDpBDmssACEggi0QICMQiMIgAAyoRKOlAFBHDUBCLmhWYDASaRYUB01CAK9E1CYokAhosCkFgoEoBzVWgyIQeAXRSWArAaQEQyuBamcmKFFBAyYyZCUQCkQhQogHQhBqQxCyVANEABEQgwjB2rMkAETIAtAOIiggQVBFAAS6Iwo4qFAwKobCRZKIQKbYW2CCINDgf4QgQEBAxYA7IZAYgYMAAQS20cQDCIESKDIRRAAkMACCwVGDCgABAHKAAhhYiwGBVCSYCBIPJMJwBYUPgESFBIyCyIYRiAB0gAgADEZoYACBAR0DJBqAEHERUEMiFRoCYSYDpAwEAWEKpBBABQcYiCMAwAKBYqAR46BAIQAsBCYBAKcZCykAIRMAJzyBYOTsQRksGAgONoSecSJAgowQAQgpzFUIIgEEYCiWRTQKsCqAEKxhVACgUBM9FMASPAUBXiA2ioe8hhecqSLOAQDBNZa0CDMfEHrAISAIKwQAgAyBCBhMUkFG2KEZQIlqAsAEAAKYbGRgSUQ%3D%3D-T-0-33
    1034939420116484096
    1034940148205539329
    
    1034952835899617280-1034952835899617280
    1034953364944039936
    TWEET-1034952726155874304-1034953364944039936
    TWEET-1034949051459035136-1034953364944039936
    TWEET-1034941943682408448-1034953364944039936
    
    '''