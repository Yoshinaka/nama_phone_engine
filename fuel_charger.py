# -*- coding: utf-8 -*-
import threading
from libs.fuel import fuel
import random
import time

class ChargerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fuel_tank = fuel.Fuel()
        self.interval = 30

    def run(self):
        while 1:
            print "get tweets"
            new_tweets = random.randint(29,31)
            print "New Tweets ", new_tweets
            print self.fuel_tank.fuel
            self.fuel_tank.add_fuel(new_tweets)
            time.sleep(self.interval)


