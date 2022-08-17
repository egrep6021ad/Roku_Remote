from time import sleep
from roku import Roku
import random

import os
from datetime import datetime

roku = Roku("your roku's ip adress")
apps = roku.apps

def get_netflix():
    netflix = roku['12']
    netflix.launch()
    sleep(10)
    roku.up()
    sleep(5)
    roku.select()
    for x in range(20):
        roku.volume_down()
    for x in range(8):
        roku.volume_up()

def get_youtube():
    youtube = roku['837']
    youtube.launch()
    sleep(12)
    roku.back()
    sleep(2)
    roku.select()
    for x in range(20):
        roku.volume_down()
    for x in range(8):
        roku.volume_up()

def get_hulu():
    hulu = roku['2285']
    hulu.launch()
    sleep(12)
    roku.up()
    sleep(3)
    roku.left()
    sleep(3)
    roku.down()
    sleep(3)
    roku.literal('Fox News')
    sleep(3)
    for x in range(6):
        roku.right()
    for x in range(3):
        sleep(1)
        roku.select()
    for x in range(20):
        roku.volume_down()
    for x in range(8):
        roku.volume_up()


if __name__ == "__main__":
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == '11:15':
            print("Current Time =", current_time)
            roku.poweroff()
            sleep(10)
            roku.poweron()
            sleep(10)
            channel = random.randrange(2,4)

            if channel == 1:
                get_netflix()
            elif channel == 2:
                get_youtube()
            elif channel == 3:
                get_hulu()
            elif channel == 0:
                break
            sleep(3)
            print(f"\nCurrent Channel: {roku.active_app}\n")
            channel = int(input("1 for Netflix\n2 for Youtube\n3 for Hulu\n0 to Exit\n"))
        else:
            sleep(30)
            print(current_time)
            continue




# https://pypi.org/project/roku/
# https://github.com/jcarbaugh/python-roku/blob/master/roku/core.py
