# -*- coding: utf-8 -*-
import threading
__author__ = 'Vermee81'

status = "OFF"

# Remaining time that the fan is kept working.
power_time = 0

# Last tweet number we took.
tweet_num = 0

def another_get_tweets():
    return 5

def get_tweets():
    print("Starting to get tweets")
    t = threading.Timer(30, get_tweets)
    t.start()

def turn_off():
    print("Turn off")
    status = "OFF"

def turn_on():
    print("Turn on")
    status = "ON"

def main():
    # 30秒間隔でツイッターのツイート数を監視する
    # ツイッターを監視するスレッドを生成
    twitter_thread = threading.Thread(target=get_tweets)
    twitter_thread.start()
    # ツイッター監視スレッドにチケットを渡して、ツイート数を受け取る
    #     受け取ったら、最終確認ツイート番号とツイート数を更新
    # 別スレッドで電気信号を送り込むスレッドを生成
    # 信号監視スレッドに何時までONにするか指示する
    # カウンター監視スレッドは1秒間隔で監視してOFFのステータスに変更する

if __name__ == "__main__":
    main()



