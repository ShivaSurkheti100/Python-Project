
'''import random 
randNo = random.randint(1, 5)
print(randNo)  # prints random numbers from 1 to 5'''

# THE PERFECT GUESS ; NAME OF PROJECT

import random 
randNumber = random.randint(1, 100)
# print(randNumber) 

userGuess = None # userGuess must be defined before entering the loop first
guesses = 0

while userGuess != randNumber:
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if userGuess == randNumber:
        print("You guessed it right.")
    else:
        if userGuess > randNumber:
            print("You guessed it wrong ! Enter a smaller number:")
        else:
            print("You guessed it wrong! Enter a larger number:")
   
print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", 'r') as f:
    hiscore = int(f.read()) # f.read() string hunxa

if(guesses<hiscore):
    print("You have just broken the high score!")
with open("hiscore.txt", "w") as f:
    f.write(str(guesses))






