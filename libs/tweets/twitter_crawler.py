# -*- encoding=utf-8 -*-
import threading
import time
import t_key
import oauth2 as oauth
import pprint
import json, urllib2
import random
import ConfigParser
###import ignore_twitter_keys.py


def get_tweets():

    conf = ConfigParser.SafeConfigParser()
    conf.read(ignore_twitter_keys.py)
    print conf.get('twitterkeys', 'CK')
    print conf.get('twitterkeys', 'CS')
    print conf.get('twitterkeys', 'AT')
    print conf.get('twitterkeys', 'AS')

#    CK = t_key.dict['cons_key']
#    CS = t_key.dict['cons_sec']
#    AT = t_key.dict['acc_token']
#    AS = t_key.dict['acc_sec']

    consumer = oauth.Consumer(key=CK, secret=CS)
    token = oauth.Token(key=AT, secret=AS)

    url = 'https://api.twitter.com/1.1/search/tweets.json'
    params = {'q': "@Vermee81"}

    request = oauth.Request.from_consumer_and_token(consumer, token, http_url=url,parameters=params)
    request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
    res = urllib2.urlopen(request.to_url())


    for r in res:
        data = json.loads(r)

    value_list = data['search_metadata']['count']
    for i in range(4):
        print data['statuses'][i+1]['text']

    print value_list

    time.sleep(30)


    #pprint.pprint(data)
    #print data('search_metadata')


class TwitterThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.interval = 30

    def run(self):
        counter = 0
        while 1:
            print "get tweets"
            print counter
            counter += 1
            print random.randint(1, 10)
            time.sleep(self.interval)

    def dummy_tweets(self):
        tweet_num = random.randint(1, 10)
        return tweet_num

if __name__ == '__main__':
    #twitter_thread = threading.Thread(target=get_tweets)
    #twitter_thread = threading.Thread(target=test_print)
    #twitter_thread.start()

    tweet_crawl = TwitterThread()
    tweet_crawl.start()

