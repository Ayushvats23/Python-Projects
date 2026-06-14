#GUESS THE NUMBER GAME
print("Welcome to guess the number game") 
print( "The number should be between 1 to 50, I hope you may guess it quickly ")
import random
n = random.randint(1,50)
a = -1 
guesses = 0

while (a != n):
    guesses +=1
    a = int(input("Now, Guess a number : "))
    if (a>n):
        print ("guess a lower number")
    else:
        print ("guess a higher number")

print (f"you have guessed the exact number {n} correctly in {guesses} attempt")
