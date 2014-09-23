# -*- coding: utf-8 -*-
import threading
import time
from libs.gpio import gpio
from libs.tweets import twitter_crawler
from libs.fuel import fuel

__author__ = 'Vermee81'

status = "OFF"

# Remaining time that the fan is kept working.
power_time = 0

# Last tweet number we took.
tweet_num = 0

def main():
    # Raspberry Piをコントロールするオブジェクトを生成
    my_gpio = gpio.Gpio()
    fuel_tank = fuel.Fuel()

    # 30秒間隔でツイッターのツイート数を監視する
    # ツイッターを監視するスレッドを生成
    # fuel_chargerに移動予定
    twitter_thread = threading.Thread(target=twitter_crawler.get_tweets)
    twitter_thread.start()

    while 1:
        if power_time > 0 and my_gpio.state == 'OFF':
            my_gpio.on()
        if power_time == 0 and my_gpio.state == 'ON':
            my_gpio.off()

        # 燃料供給
        power_time += fuel.fuel

        # 毎秒燃料は減っていく
        power_time -= 1

        time.sleep(1)

if __name__ == "__main__":
    main()



