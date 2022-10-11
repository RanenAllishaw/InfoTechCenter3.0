# Gasoline
# Developer: Ranen Allishaw
# Version 1.0

"""
Define a function to check our gas gauge and determine how far we can
go before we need gas based on if, elif, and else conditions.
"""

# Import libraries here.
import random


# Gas level finder function.
def gasLevelGauge():
    gasLevelList = ['\033[3;31;40mEmpty', '\033[2;31;40m1/4 Tank', '\033[2;33;40m1/2 Tank', '\033[2;32;40m3/4 Tank',
                    '\033[1;32;40mFull']
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calling the gasLevelGauge function to store the value once.
gasLevelIndicator = gasLevelGauge()


def gasLevelAlert():
    if gasLevelIndicator == '\033[3;31;40mEmpty':
        print('\033[3;31;40m***WARNING YOU ARE ON EMPTY***\n*Calling Emergency Contacts*')


gasLevelAlert()
