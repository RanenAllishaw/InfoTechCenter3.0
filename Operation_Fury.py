#Welcome Message
#Developer: Ranen Allishaw
#Version: 1.0

"""
Our welcome message will start our program letting
the drivers know that the InfoTechCenter OS is loading.
"""

#Import any Libraries Here
import time #I imported the time library for further use in code.
import sys #I have imported the system library for a more advanced code.

print('\nWelcome to Operation Fury InfoTech Center')

x = 0

time.sleep(2)
print('')

while x != 4:
    p = "Operation Fury's Operating System is Booting Up" + '.' * x
    print(p)
    time.sleep(1)
    x += 1
    if x == 4:
        x -= 3
