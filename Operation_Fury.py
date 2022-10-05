# Welcome Message
# Developer: Ranen Allishaw
# Version: 1.1

"""
Our welcome message will start our program letting
the drivers know that the InfoTechCenter OS is loading.
"""

# Import any Libraries Here
import time  # I imported the time library for further use in code.
import sys  # I imported the system library for further use in code.

print('\n\033[1;34;48m Welcome to Operation Fury InfoTech Center')

x = 0
a = 0

time.sleep(2)
print('')

while x != 20:
    x += 1
    b = ("\033[1;33;40m Operation Fury OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Done!')
