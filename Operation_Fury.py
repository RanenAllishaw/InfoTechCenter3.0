# Weather
# Developer: Ranen Allishaw
# Version 1.3

"""
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using If, Elif, Else statements to
check the condition of the road and print specific message.
"""

# Import any libraries bellow
import random

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
        print('\nVRS has changed your alarm to 30 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 30MPH')
    elif weatherAlert == 'Snowy':
        print('\nVRS has changed your alarm to 15 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 45MPH')
    elif weatherAlert == '\033[1;34;40mRainy':
        print('\nVRS has changed your alarm to 12.5 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 50MPH')
    elif weatherAlert == '\033[1;37;40mWindy':
        print('\nVRS has changed your alarm to 5 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 60MPH')
    elif weatherAlert == '\033[1;37;40mFoggy':
        print('\nVRS has changed your alarm to 10 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 55MPH')
    elif weatherAlert == '\033[1;33;48mThunder & Lightning':
        print('\nVRS has changed your alarm to 25 minutes earlier based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will only allow your car to go 35MPH')
    else:
        print('\nVRS has not changed your alarm based on the NWS forcast of ' + weatherAlert + '.')
        print('\033[3;37;40mVRS will allow your car to go at the required speed limit.')


vehicleResponseSystem()
