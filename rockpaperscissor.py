import random
#always use  import the modules at top 

# we need two variables 
'''
one computer side and 
another user side '''

user_wins=0
computer_wins=0

options=["rock","paper","scissor"]
options[0]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to Quit?:").lower()
    if user_input=='q':
        break
    if user_input not in options:  #list reverse the input 
        continue
    
    random_number=random.randint(0,2)
    #rock:0 ,paper:1 and scissor:2.
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + " . ")

    if user_input == computer_pick:
     print("Draw!")
     continue

    if user_input == "rock" and computer_pick=="scissor":
        print("You won!")
        user_wins +=1
        continue

    elif user_input == "paper" and computer_pick=="rock":
        print("You won!")
        user_wins +=1
        continue

    elif user_input == "scissor" and computer_pick=="paper":
        print("You won!")
        user_wins +=1
        continue
    
    elif user_input == "scissor" and computer_pick=="paper":
        print("Draw !")
        user_wins=computer_wins 
        continue

    else:
        print("You lost!")
        computer_wins +=1


print("You won ",user_wins,"times.")
print("The Computer won ",computer_wins,"times.")
print("goodbye!")



 