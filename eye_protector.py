#!/usr/bin/python
'''
we all love our eyes. this code will help you protect your eyes, a lil bit.
The screen goes off for 20 seconds every 20 minutes, something that has worked for me quite well.
happy seeing.. <3


ONLY FOR LINUX
install xbacklight

UBUNTU: sudo apt-get installl xbacklight
'''

import os
import time

while True:

    #set brightness to 7 - normal screen
    os.system('xbacklight -set 7')
    time.sleep(20*60) #20 minutes

    #set brightness to 0 - black screen
    os.system('xbacklight -set 0')
    time.sleep(20) #20 seconds