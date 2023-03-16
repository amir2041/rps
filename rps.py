import random

choices=["paper","rock","scessors"]

while True:
    player_ch=input("please enter 1 to 3:")
    if(int(player_ch) >3):
        continue

    player_choice=choices[int(player_ch)-1]
    computer_choice=random.choice(choices)
    if(player_choice==computer_choice):
        print(f"you are tie! your choice:{player_choice}\n computer:{computer_choice}")
    elif((player_choice=="paper" and computer_choice=="rock") \
     or (player_choice=="scessors" and computer_choice=="paper")\
     or (player_choice=="rock" and computer_choice=="scessors") ):
     print(f"player is winner \n your choice:{player_choice}\n computer:{computer_choice}")
    else:
        print(f"computer is winner\nyour choice:{player_choice}\n computer:{computer_choice}")
    c1=input("do you want to continue (y/n)?")
    if(c1=="n"):
        break
