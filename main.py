#!/usr/bin/env python

import time 
#import getpass

def sec_countdown():
    value = int(input("Set your timer/countdown for ... seconds!"))
    for i in range(0, value-1):
    	time.sleep(1)
    	value -= 1
    	print(str(value))
    time.sleep(1)

def min_countdown():
    pass

def hours_countdown():
    pass

unit = input("Which unit do you wish to use? ")

try:
    if unit == "s":
        sec_countdown()
    elif unit == "min":
        min_countdown()
    elif unit == "h":
        hours_countdown()
    else:
        print("Not a  valid unit!!")
except:
    print("Not an option!")
    input("Press enter to try again...")

print("Time is up!!")
