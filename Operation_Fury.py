# Weather
# Developer: Ranen Allishaw
# Version 1.2

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
    weatherForcast = ['\033[1;34;40mRainy', 'Snowy', '\033[1;33;40mSunny', '\033[1;37;40mCloudy', '\033[1;37;40mFoggy',
                      '\033[1;33;48mThunder & Lightning', '\033[1;36;40mIcy', 'Windy']
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition


weatherAlert = weather()


def vehicleResponseSystem():
    if weatherAlert == '\033[1;36;40mIcy':
        print('\nVRS has changed your alarm to 30 minutes earlier based on the NWS forcast of ' + weatherAlert)


vehicleResponseSystem()
