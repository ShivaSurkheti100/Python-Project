'''We all have played snake, water gun game in our childhood.
write a python program capable of playing this game with the user'''
# snake drinks water so snake wins, gun will be drown in water so water wins; gun kills snake so gun wins
# SNAKE WATER GUN JASTAI GAME HUNXA ROCK PAPER SCISSORS 

import random # random module

def gameWin(comp, you):
    if comp == you: # if two values are equal, declare a tie !
        return None 
    elif comp == "s":  # Check for all possibilities when computer chose s
        if you == "w":
            return False
        elif you == "g":
            return True

    elif comp == "w":  # Check for all possibilities when computer chose w
        if you == "g": 
            return False
        elif you == "s":
            return True 

    elif comp == "g":  # Check for all possibilities when computer chose g
        if you == "s":
            return False
        elif you == "w":
            return True
  
print(("Comp Turn: Snake(s) Water(w) or Gun(g)? ")) # computer le tw aafai choose garxa ; no need of input() function

randNo = random.randint(1, 3) #  random module vitra randint() function hunxa which generates random integers between two integers 
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

## print(randNo) # prints random number; sometimes 1; sometimes 2; sometimes 3

you = input("Your Turn: Snake(s) Water(w) or Gun(g)? ") # you can choose 1, 2, 3 for snake, wate and gun resp

a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")







