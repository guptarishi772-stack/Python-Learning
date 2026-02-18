''' SANKE, WATER AND GUN GAME
RULES:-
Snake- 1, water- -1, gun- 0'''

import random
computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "s", -1: "w", 0: "g"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Game is draw")

else:
    if(computer == 1 and you == -1):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == -1 and you == 1):
        print("You win") 
    elif(computer == -1 and you == 0):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You lose")
    elif(computer == 0 and you == -1):
        print("You win")
    else:
        print("Something went wrong")                           