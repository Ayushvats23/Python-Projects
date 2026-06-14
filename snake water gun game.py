#SNAKE WATER GUN GAME PROJECT 2
print("Welcome Everyone!")
print("This is SNAKE WATER GUN game")
import random
'''
1 for snake 
-1 for water 
0 for gun
'''

print("The Rules of the game is as mentioned below ")
print("Snake drinks water → Snake wins")
print("Gun shoots snake → Gun wins")
print("Water douses gun → Water wins")
print("You have to choose any one character out of s,w,g which stands for respective member of game mentioned above")

computer = random.choice([1,-1,0])
youstr= input("Enter your choice :")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 :"snake", -1 : "water", 0 :"gun"}
you= youDict[youstr]
print(f"You have chose {reverseDict[you]} computer chose {reverseDict[computer]} ")

if (computer == you):
    print("Its a draw!")

else:
    if (computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == -1 and you == 0):
        print("You Lose !")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    elif(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    else: print("Something went wrong !")