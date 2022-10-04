#Welcome Message
#Developer: Ranen Allishaw
#Version: 1.0

"""
Our welcome message will start our program letting
the drivers know that the InfoTechCenter OS is loading.
"""

#Import any Libraries Here
import time #I imported the time library for further use in code.

print('\n\033[1;34;48m Welcome to Operation Fury InfoTech Center')

x = 0
t = 1

time.sleep(2)
print('')

while x != 20:
    p = "\033[1;33;40m Operation Fury's Operating System is Booting Up" + '.' * x
    print(p)
    time.sleep(1)
    x += 1
    t += 1
    if t == 10:
        x = 20
        print('\n\033[1;32;40mDone!')
    if x == 4:
        x -= 3