"""This is a numeric operators code."""

__author__ = "730393320"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
L: str = str(left)
R: str = str(right)
print(L + " ** " + R + " is " + str(left ** right))
print(L + " / " + R + " is " + str(left / right))
print(L + " // " + R + " is " + str(left // right))
print(L + " % " + R + " is " + str(left % right))
