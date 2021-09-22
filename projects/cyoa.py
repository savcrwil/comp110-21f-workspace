"""Treasure hunt game!"""
__author__ = "730393320"

points: int = 0
mountain: str = "\U000026F0"
tree: str = "\U0001F333"
billy: str = "\U0001F410"
bobby: str = "\U0001F43B"


def greet() -> None:
    """Greet the player!"""
    global points
    player: str = input("What is your name? ")
    print(f"Welcome {player} to the treasure hunt! Choose paths to make your way to the jackpot.")


def main() -> None:
    greet()
    global points
    print(f"You have three options: Go left to the mountains {mountain}, go right to the forest {tree}, or end the game. What do you want to do?")
    new_location: str = input("Type 'left', 'right' or 'end'. + 100 points for making this really hard decision. ")
    if new_location == "end":
        points = points + 100
        end()
    else:
        if new_location == "left":
            points = points + 100
            mountains(2)
        else:
            points = points + 100
            forest()


def end() -> None:
    """The end message."""
    global points
    print(f"Game over. You have {points} points. From here, you have three choices: go to the mountains, go to the forest, or end the game. What do you want to do?")
    choice: str = input("Type 'mountains', 'forest', or 'end'. ")
    if choice == "end":
        print(f"Thanks for playing. You finished the game with {points} points.")
    else:
        if choice == "mountains":
            print(f"You have {points} points.")
            mountains(2)
        else:
            print(f"You have {points} points.")
            forest()


def mountains(chances: int) -> int:
    """The passcode guess."""
    global points
    print(f"After a long trek, you made it to the mountain. You are greeted by a mountain goat {billy}, Billy, who has some information.")
    print(f"Billy {billy}: You made it to the side of the island with the treasure. Congratulations! To keep going, you'll need to guess the password to the treasure box.")
    print(f"Billy {billy}: I'll give you a hint. It's one of these: 1, 2, or 3. You have two chances to get it right.")
    i = 2
    while i > 0:
        guess: int = int(input(f"Billy {billy}: What is your guess? Type '1', '2', or '3'. "))
        if guess == 3:
            i = 0
            points = points + 1000
            print(f"Billy {billy}: You guessed correctly! You found the treasure. You completed the game. + 1000 points.")
        else:
            print(f"Billy {billy}: Wrong answer. - 50 points.")
            points = points - 50
            i = i - 1
    end()
    return points
# mountains function not returning points - only going through the loop
        

def forest() -> None:
    """The math problem."""
    global points
    from random import randint
    print(f"You've bushwhacked for hours but have finally made your way through the forest {tree}. You're greeted by a magical bear {bobby}, Bobby, who has a riddle.")
    print(f"Bobby {bobby}: Hello! In order for you to pass through to the treasure, I need you to help me. I'm going to give you a random number between 1 and 5.")
    print(f"Your number is {randint(1, 5)}.")
    random_plus_three: int = int(input("Now, add 3 to that number. What is it? "))

    if random_plus_three <= 8:
        print(f"Bobby {bobby}: You got it right! Sorry to disappoint, but that riddle was just a diversion. The treasure is on the other side of the island.")
        print(f"Bobby {bobby}: + 100 points because I just wasted your time.")
        points = points + 100
        end()


if __name__ == "__main__":
    main()