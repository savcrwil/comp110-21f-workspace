"""Repeating a beat in a loop."""

__author__ = "730393320"


beat: str = input("What beat do you want to repeat? ")
i: int = int((input("How many times do you want to repeat it? ")))
string_beat: str = ""

if i > 0:
    while i > 1:
        string_beat = string_beat + beat + " "
        i = i - 1
    print(string_beat + beat)
else:
    print("No beat...")
