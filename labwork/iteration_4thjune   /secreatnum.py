#Wap to implement a Number Guessing Game

#import random module
import random

#generate secret number
secret_number = random.randint(1, 50)

#---------------------------------------------------

#initialize attempts
attempts = 0

#---------------------------------------------------

#accept guesses until correct
while(True):
    
    #input guess
    guess = int(input("Enter your guess: "))
    
    #count attempts
    attempts += 1

    #---------------------------------------------------

    #compare guess with secret number
    if(guess > secret_number):
        print("Too High")

    elif(guess < secret_number):
        print("Too Low")

    else:
        print("Correct Guess")
        break

#---------------------------------------------------

#display total attempts
print("Total Attempts =", attempts)
