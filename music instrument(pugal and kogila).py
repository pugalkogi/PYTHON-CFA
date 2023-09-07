#python instrument quiz

import random

def main():
    """Start a music instrument guessing game."""
    print("Welcome")
    print("Guess the indian traditional instrument:",
                "udukke",
                "harmonika",   
                "nadeswaram",
                "tabla")

    instrument = [
        "harmonika",
        "tabla",
        "udukke",
        "nadeswaram",
                  ]
   
    x = random.choice(instrument)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What instrument am i thinking of?"))
        if x == guess:
            print("You guessed {}. Congratulations you win!".format(guess)) 
            break
        
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
main()                                                                                  