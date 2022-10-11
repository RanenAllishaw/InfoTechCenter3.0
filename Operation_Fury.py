# Gasoline
# Developer: Ranen Allishaw
# Version 1.2

"""
Define a function to check our gas gauge and determine how far we can
go before we need gas based on if, elif, and else conditions.
"""

# Import libraries here.
import random
import time
import sys


# Gas level finder function.
def gasLevelGauge():
    gasLevelList = ['\033[3;31;40mEmpty', '\033[2;31;40m1/4 Tank', '\033[2;33;40m1/2 Tank', '\033[2;32;40m3/4 Tank',
                    '\033[1;32;40mFull']
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calling the gasLevelGauge function to store the value once.
gasLevelIndicator = gasLevelGauge()


def gasLevelAlert():
    x = 0
    a = 0
    if gasLevelIndicator == '\033[3;31;40mEmpty':
        print('\033[3;31;40m***WARNING YOU ARE ON EMPTY***')
        print('\033[3;31;40m**Contacting Emergency Contacts**')
        time.sleep(.5)
        while x != 8:
            x += 1
            b = ('\033[2;31;40m*Calling' + "." * a + '*')
            a = a + 1
            # \r prints a carriage return first, so `b` is printed on top of the previous line.
            sys.stdout.write('\r' + b)
            time.sleep(0.5)
            if a == 4:
                a = 0
            if x == 8:
                print('\033[1;33;40m Your Contacts have been notified.')


gasLevelAlert()
