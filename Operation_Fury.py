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


def listOfGasStations():
    gasStations = ['Shell', 'Meijer', 'Circle K', 'Marathon', 'Speedway', "Love's", 'Mobil']
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


# Variable calling the listOfGasStations function to store the value once.
nearestGasStation = listOfGasStations()


def gasLevelAlert():
    x = 0
    a = 0
    milesToGasStation = round(random.uniform(1, 25), 1)
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
    elif gasLevelIndicator == '\033[2;31;40m1/4 Tank':
        print('\033[1;31;40m*Warning!*')
        time.sleep(.5)
        print("\033[2;33;40mYou're at 1/4 of gas left, now checking google maps for the closest gas station.")
        time.sleep(.75)
        print('The closest gas station to your area is; ' + nearestGasStation + ', which is ' + str(milesToGasStation) + '.')
    elif gasLevelIndicator == '\033[2;33;40m1/2 Tank':
        print('hi')
    elif gasLevelIndicator == '\033[2;32;40m3/4 Tank':
        print('hi')
    elif gasLevelIndicator == '\033[1;32;40mFull':
        print('hi')


gasLevelAlert()
