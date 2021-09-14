"""An exercise in remainders and boolean logic."""

__author__ = "730393320"


integer: int = int(input("Enter an int: "))
int_2: int = integer % 2
int_7: int = integer % 7

if int_2 == 0 and int_7 == 0:
    print("TAR HEELS")
else:
    if int_2 == 0:
        print("TAR")
    else:
        if int_7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
