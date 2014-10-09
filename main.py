# -*- coding: utf-8 -*-
import time
# from libs.gpio import gpio
# from libs.tweets import twitter_crawler
# from libs.fuel import fuel
import fuel_charger
from libs.gpio import dummy_gpio

status = "OFF"


def change_gpio_state(my_gpio, power_time):
    if power_time > 0 and my_gpio.state == 'OFF':
        my_gpio.on()
    if power_time == 0 and my_gpio.state == 'ON':
        my_gpio.off()


def main():

    # Raspberry Piをコントロールするオブジェクトを生成
    #my_gpio = gpio.Gpio()
    my_gpio = dummy_gpio.DummyGpio()

    # Remaining time that the fan is kept working.
    power_time = 0

    # Last tweet number we took.
    # tweet_num = 0

    # 別スレッドで30秒間隔でツイッターのツイート数を監視して
    # fuel_tankに燃料を供給する。
    dummy_charger = fuel_charger.ChargerThread()
    dummy_charger.start()

    # 燃料
    fuel_tank = dummy_charger.fuel_tank

    while 1:

        change_gpio_state(my_gpio, power_time)

        # 燃料供給
        power_time += fuel_tank.give_fuel()
        print "燃料供給後", power_time

        # 毎秒燃料は減っていく
        power_time -= 1
        print "燃料減った後", power_time

        time.sleep(1)


    # 30秒間隔でツイッターのツイート数を監視する
    # ツイッターを監視するスレッドを生成
    # fuel_chargerに移動予定
    #twitter_thread = threading.Thread(target=twitter_crawler.get_tweets)
    #twitter_thread.start()

    # while 1:
    #     if power_time > 0 and my_gpio.state == 'OFF':
    #         my_gpio.on()
    #     if power_time == 0 and my_gpio.state == 'ON':
    #         my_gpio.off()
    #
    #     # 燃料供給
    #     power_time += fuel.fuel
    #
    #     # 毎秒燃料は減っていく
    #     power_time -= 1
    #
    #     time.sleep(1)




if __name__ == "__main__":
    main()



