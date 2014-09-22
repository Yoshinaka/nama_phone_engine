# -*- coding: utf-8 -*-
import threading
from libs.gpio import gpio
from libs.tweets import twitter_crawler

__author__ = 'Vermee81'

status = "OFF"

# Remaining time that the fan is kept working.
power_time = 0

# Last tweet number we took.
tweet_num = 0

def main():
    # 決まった間隔で動かす燃料を取得する
    # 間隔はFuelStandが作成するオブジェクトにおまかせ
    #fuel_charger = FuelStand()
    #fuel_charger.start()

    # 30秒間隔でツイッターのツイート数を監視する
    # ツイッターを監視するスレッドを生成
    # fuel_chargerに移動予定
    twitter_thread = threading.Thread(target=twitter_crawler.get_tweets)
    twitter_thread.start()

    # ツイッター監視スレッドにチケットを渡して、ツイート数を受け取る
    #     受け取ったら、最終確認ツイート番号とツイート数を更新
    # 別スレッドで電気信号を送り込むスレッドを生成
    # 信号監視スレッドに何時までONにするか指示する
    mygpio = gpio.Gpio()
    print mygpio.state
    # カウンター監視スレッドは1秒間隔で監視してOFFのステータスに変更する

if __name__ == "__main__":
    main()



