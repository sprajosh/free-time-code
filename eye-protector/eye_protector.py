#!/usr/bin/python
import os
import time

while True:

    #set brightness to 7 - normal screen
    os.system('xbacklight -set 7')
    time.sleep(20*60) #20 minutes

    #set brightness to 0 - black screen
    os.system('xbacklight -set 0')
    time.sleep(20) #20 seconds