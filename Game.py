# name:Steven Russell   
# date:Aug-14-2017
# description: Text-based game

import random
import time 

def displayIntro():
    print("You wake up in a cave with no memory at all.")
    print("It seems as if the cave goes two ways.")
    print("One path will certainly lead to death,")
    print("while the other may lead to civilization.")
    
def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")
        
    return path
    
def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there is a rock formation that looks strange and it starting to glow.")
    time.sleep(2)
    print("All of a sudden you feel light and cant move...")
    print()

    
    correctPath = random.randint(1, 2)
    
    if choosePath == str(correctPath):
        print("The floor slopes beneath you and leads down to a chamber.")
        time.sleep(2)
        print("What could possibly be down here?")
    else:
        print("The floor collapses at your feet.")
        time.sleep(2)
        print("You fall into a deep abyss that never seems to end.....")
        
        
        
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)  # choice is equal to "1" or "2"
    playAgain = input("Do you want to try again?  (yes or y to continue): ")