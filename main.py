#!/usr/bin/env python

import time 
#import getpass

def countdown():
    value = int(input("Set your timer/countdown for ... seconds!"))
    for i in range(0, value-1):
    	time.sleep(1)
    	value -= 1
    	print(str(value))
    time.sleep(1)

countdown()
print("Time is up!!")
