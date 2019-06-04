"""# a guess the number program that generates a random number
# every time it is loaded and the user has to figure it out only has
# 5 attempts before he dies
"""

import sys
import random

"""Set the GameActive flag to True """
"""Main Game function """
def funGuessnumgame():
    playerlives = 5
    # Generate the random number from a range
    winningnumber = random.randint(1, 21)
    #print(winningnumber)
    while playerlives >0:
        try:
            guess = int(input("\nI'm thinking of a fucking number between " +
                    "1 and 20, see if you can guess the fucking number\n"))

    # Guess the correct answer
            if guess == winningnumber:
                print("\nGood job, holy shit, you got a pickle.  You win")
                gameover()
        # Incorrect answers
            elif (guess<=winningnumber +2 ) and (winningnumber-2<=guess) :
                print("You are burning and damn close, try again\n")
                playerlives -=1
                print("You have: " , playerlives ," left before you die\n")

            elif(guess<=winningnumber+3) and (winningnumber - 3 <= guess):
                print('warm')
                playerlives -=1
                print("You have: ", playerlives," left before you die\n")

            elif(guess<=winningnumber +4) and (winningnumber-4<=guess):
                print('Holy shit you are cold')
                playerlives -=1
                print("You have: " , playerlives ," left before you die\n")
            else:
                print("Cold as ice in a cold freezer on cold Olympus\n")
                playerlives -=1
                print("You have: " , playerlives ," left before you die\n")
            if playerlives == 0:
                print("You and your friends are dead, Game Over.\n")
                print("The winning number was: ", winningnumber)
                gameover()
        except ValueError:
            print("That is not a fucking number try again\n")

def gameover():
    dec=input( "\nWould you like to play again?(q to quit, y to play again.\n")
    if dec == 'q':
        sys.exit()
    elif dec == 'y':
        funGuessnumgame()
    else:
        print("That is not a valid response\n")
        gameover()
"""End of the function declarations """



funGuessnumgame()








