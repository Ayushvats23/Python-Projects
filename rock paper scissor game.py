import random
item_list = ['rock', 'paper', 'scissor']

Your_choice = input('Enter your move= rock, paper, scissor :')
comp_choice = random.choice(item_list)

print(f"Your choice={Your_choice}, Computer choice = {comp_choice}")

if Your_choice == comp_choice:
    print(" It's a draw! as you both chose the same ", {Your_choice} and {comp_choice})

elif Your_choice == 'rock':
    if comp_choice == 'scissor':
        print("YOU win as rock breaks scissor ")
    else:
        print("Computer wins as paper covers the rock!")

elif Your_choice == 'scissor':
    if comp_choice == 'rock':
        print("Computer wins as rock breaks scissor")
    else:
        print("You win as scissor cuts the paper! ")

else:
    if comp_choice == 'rock':
        print("You win as paper covers the rock! ")
    else :
        print("Computer wins as scissor cuts the paper!")

