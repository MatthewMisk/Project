import random

def MainGame():
    
    BotChoice = random.randint(1,3)
    
    PlayerInput = str(input("please enter rock, paper, scizzors: "))
    
    if (PlayerInput == "rock"):
        if (BotChoice == 1):
            print("Player Wins!")
            PlayerRepeatInput = str(input("press 'y' to continue and 'n' to stop "))
            if (PlayerRepeatInput == 'y'):
                MainGame()
            else:
                print("goodbye")
        else:
            print("Player Lost!")
            PlayerRepeatInput = str(input("press 'y' to continue and 'n' to stop "))
            if (PlayerRepeatInput == 'y'):
                MainGame()
            else:
                print("goodbye")
                
                
    if (PlayerInput == "paper"):
        if (BotChoice == 2):
            print("Player Wins!")
            PlayerRepeatInput = str(input("press 'y' to continue and 'n' to stop "))
            if (PlayerRepeatInput == 'y'):
                MainGame()
            else:
                print("goodbye")
        else:
            print("Player Lost!")
            PlayerRepeatInput = str(input("press 'y' to continue and 'n' to stop "))
            if (PlayerRepeatInput == 'y'):
                MainGame()
            else:
                print("goodbye")
                
    if (PlayerInput == "scizzors"):
        if (BotChoice == 3):
            print("Player Wins!")
            PlayerRepeatInput = str(input("press 'y' to continue and 'n' to stop "))
            if (PlayerRepeatInput == 'y'):
                MainGame()
            else:
                print("goodbye")
        else:
            print("Player Lost!")
            PlayerRepeatInput = str(input("press 'y' to continue and 'n' to stop "))
            if (PlayerRepeatInput == 'y'):
                MainGame()
            else:
                print("goodbye")
                
    
MainGame()