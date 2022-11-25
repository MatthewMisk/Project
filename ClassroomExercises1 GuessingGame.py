from random import randint
import colorama
from colorama import Fore

def Main():
    answer = randint(1,10)
    print(Fore.BLUE + "Guess the number game")
    print()
    print(Fore.BLUE + "Ive thought of a number between 1 and 10, you have 3 tries to have a guess what at it is")
    tries = 3
    guessInt = 0
    while tries > 0:
        guess = input(Fore.BLUE + "Enter your guess: ")
        guessInt = int(guess)

        if guessInt == answer:
            print(Fore.GREEN + "Well done you are correct! Your guess was " + str(answer))
            tries = tries - 3
            print(Fore.BLUE + "Do you want to retry? Press Y for Yes and N for No.")
            retry = input()
            if retry == ("Y"):
                Main()
            else:
                print(Fore.BLUE + "Goodbye :(")
            
        elif guessInt < answer:
            print(Fore.RED + "Sorry, your guess was too low.")
            tries = tries - 1
            if tries == 0:
                print(Fore.RED + "Sorry, your guess was too low. The answer was " + str(answer))
                print(Fore.BLUE + "Do you want to retry? Press Y for Yes and N for No.")
                retry = input()
                if retry == ("Y"):
                    Main()
                else:
                    print(Fore.BLUE + "Goodbye :(")
        elif guessInt > answer:
            print(Fore.RED + "Sorry, your guess was too high.")
            tries = tries - 1
            if tries == 0:
                print(Fore.RED + "Sorry, your guess was too low. The answer was " + str(answer))
                print(Fore.BLUE + "Do you want to retry? Press Y for Yes and N for No.")
                retry = input()
                if retry == ("Y"):
                    Main()
                else:
                    print(Fore.BLUE + "Goodbye :(")
                    
Main()