# -*- encoding=utf-8 -*-
import threading
import time
import t_key
import oauth2 as oauth
import pprint
import json, urllib2


# class TwitterCrawler(threading.Thread):
#     
#     def __init__(self):
#         #super().__init__()
#         self.interval = 30
#         self.tweet_point = 0
#        # Keys for twitter oauth2 api
#         self.CK = t_key.dict['cons_key']
#         self.CS = t_key.dict['cons_sec']
#         self.AT = t_key.dict['acc_token']
#         self.AS = t_key.dict['acc_sec']
#         self.twitter_settings()
# 
#     def twitter_settings(self):
#         self.consumer = oauth.Consumer(key=self.CK, secret=self.CS)
#         self.token = oauth.Token(key=self.AT, secret=self.AS)
#         self.url = 'https://api.twitter.com/1.1/search/tweets.json'
#         self.params = {'q': "@Vermee81"}
# 
#     def handle_crawl(self, tweet_point):
#         request = oauth.Request.from_consumer_and_token(self.consumer,
#                 self.token, http_url=self.url,parameters=self.params)
#         request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), self.consumer,
#                 self.token)
#         res = urllib2.urlopen(request.to_url())
#         
#         for r in res:
#             data = json.loads(r)
#             
#         pprint.pprint(data)
#         return 2, 33

def get_tweets():

    t = threading.Timer(5, get_tweets)
    t.start()

    CK = t_key.dict['cons_key']
    CS = t_key.dict['cons_sec']
    AT = t_key.dict['acc_token']
    AS = t_key.dict['acc_sec']

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

    #pprint.pprint(data)
    #print data('search_metadata')


if __name__ == '__main__':
    twitter_thread = threading.Thread(target=get_tweets)
    twitter_thread.start()

