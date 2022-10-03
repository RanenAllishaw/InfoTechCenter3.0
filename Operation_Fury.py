#Welcome Message
#Developer: Ranen Allishaw
#Version: 1.0

"""
Our welcome message will start our program letting
the drivers know that the InfoTechCenter OS is loading.
"""

print('\nWelcome to Operation Fury InfoTech Center')

x = 0
a = '.'
import time

while x != 3:
    if x == 0:
        print("Operation Fury's Operating System is Booting Up")
    time.sleep(1)
    x += 1
    if x == 1:
        print("Operation Fury's Operating System is Booting Up" + a)
    if x == 2:
        print("Operation Fury's Operating System is Booting Up" + a + a)
    if x == 3:
        print("Operation Fury's Operating System is Booting Up" + a + a + a)
    if x == 3:
        time.sleep(1)
        x -= 3