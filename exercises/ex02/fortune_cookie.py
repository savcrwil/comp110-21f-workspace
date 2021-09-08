"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730393320"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
number: int = int(randint(1, 4))

if number == 1:
    print("You are reaching your goals.")
else:
    if number == 2:
        print("Good news is on its way.")
    else:  
        if number == 3:
            print("Your hard work is paying off.")
        else:
            if number == 4:
                print("The future is promising.")

print("Now, go spread positive vibes!")