# ********************************************************************************

# Import any Libraries Here
import time  # I imported the time library for further use in waiting in code.
import sys  # I imported the system library for further use in controlling the terminal.
import random  # I imported the random library for further use in randomizing.

# ********************************************************************************

# Welcome Message
# Developer: Ranen Allishaw
# Version: 1.5

"""
Our welcome message will start our program letting
the drivers know that the InfoTechCenter OS is loading.
"""

print('\n\033[1;34;48m Welcome to Operation Fury InfoTech Center')

x = 0
a = 0

time.sleep(2)
print('')

while x != 12:
    x += 1
    b = ("\033[1;33;40m Operation Fury OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 12:
        print('\033[1;32;40m Done!')
time.sleep(.75)

# ---------------------------------------------------------------------------------------

# Weather
# Developer: Ranen Allishaw
# Version: 1.3


"""
<<<<<<< HEAD
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using If, Elif, Else statements to
check the condition of the road and print specific message.
"""

"""
This function with choose a random weather condition and have that 
answer stored in its memory with the return function for calling later
"""


def weather():
    weatherForcast = ['\033[1;34;40mRainy', 'Snowy', '\033[1;33;40mSunny', '\033[1;37;40mFoggy',
                      '\033[1;33;48mThunder & Lightning', '\033[1;36;40mIcy', '\033[1;37;40mWindy']
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition


weatherAlert = weather()


def vehicleResponseSystem():
    if weatherAlert == '\033[1;36;40mIcy':
        print(
            '\n\033[3;37;40mVRS has changed your alarm to 30 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 30MPH')
    elif weatherAlert == 'Snowy':
        print(
            '\n\033[3;37;40mVRS has changed your alarm to 15 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 45MPH')
    elif weatherAlert == '\033[1;34;40mRainy':
        print(
            '\n\033[3;37;40mVRS has changed your alarm to 12.5 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 50MPH')
    elif weatherAlert == '\033[1;37;40mWindy':
        print(
            '\n\033[3;37;40mVRS has changed your alarm to 5 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 60MPH')
    elif weatherAlert == '\033[1;37;40mFoggy':
        print(
            '\n\033[3;37;40mVRS has changed your alarm to 10 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 55MPH')
    elif weatherAlert == '\033[1;33;48mThunder & Lightning':
        print(
            '\n\033[3;37;40mVRS has changed your alarm to 25 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 35MPH')
    else:
        print('\n\033[3;37;40mVRS has not changed your alarm based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will allow your car to go at the required speed limit.')


vehicleResponseSystem()

# ---------------------------------------------------------------------------------------

# Gasoline
# Developer: Ranen Allishaw
# Version 1.3

"""
Define a function to check our gas gauge and determine how far we can
go before we need gas based on if, elif, and else conditions.
"""

print('')
time.sleep(.65)

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
    p = 0
    a = 0
    milesToGasStationquarter = round(random.uniform(1, 45), 1)
    if gasLevelIndicator == '\033[3;31;40mEmpty':
        print('\033[3;31;40m***WARNING YOU ARE ON EMPTY***')
        print('\033[3;31;40m**Contacting Emergency Contacts**')
        time.sleep(.5)
        while p != 8:
            p += 1
            b = ('\033[2;31;40m*Calling' + "." * a + '*')
            a = a + 1
            # \r prints a carriage return first, so `b` is printed on top of the previous line.
            sys.stdout.write('\r' + b)
            time.sleep(0.5)
            if a == 4:
                a = 0
            if p == 8:
                print('\033[1;33;40m Your Contacts have been notified.')
    elif gasLevelIndicator == '\033[2;31;40m1/4 Tank':
        print('\033[1;31;40m*Warning!*')
        time.sleep(.5)
        print("\033[2;33;40mYou're at 1/4 of gas left, now checking google maps for the closest gas station.")
        time.sleep(.75)
        print('The closest gas station to your area is; ' + nearestGasStation + ', which is ' + str(
            milesToGasStationquarter) + 'miles away.')
    elif gasLevelIndicator == '\033[2;33;40m1/2 Tank':
        h = [' you will have plenty of gas to get to where you need to go',
             ' you will have to refuel eventually, you will be notified when is the optimal time to refuel']
        hyn = random.choice(h)
        print("\033[2;32;40mYou're at 1/2 of a tank left," + hyn + ".")
    elif gasLevelIndicator == '\033[2;32;40m3/4 Tank':
        h = [' you will have plenty of gas to get to where you need to go',
             ' you will have plenty of gas to get to where you need to go',
             ' you will have to refuel eventually, you will be notified when is the optimal time to refuel']
        hyn = random.choice(h)
        print("\033[2;32;40mYou're at 3/4 of a tank left," + hyn + ".")
    else:
        h = [' you will have plenty of gas to get to where you need to go',
             ' you will have plenty of gas to get to where you need to go',
             ' you will have plenty of gas to get to where you need to go',
             ' you will have to refuel eventually, you will be notified when is the optimal time to refuel']
        hyn = random.choice(h)
        print("\033[2;32;40mYou're at full tank," + hyn + ".")


gasLevelAlert()
