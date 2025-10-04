name=input("Type your name:")
print(f"Welcome,{name},to this adventure")

answer=input("You are at a dirt road ,ithas come to an end and you can go left or right.Which way do you want to go? ").lower()
if answer=="left":
    answer=input("Youu come to river , you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
    if answer=="swim":
       print('You swam across and were eaten by an alligator. You lose!')
    elif answer=="walk":
         print("You walked for many miles, ran out of water and you lost the game!")
    else:
        print("Not a valid option. You lose.")
        
elif answer=="right":
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer=="back":
        print("You go back and lose.")
    elif answer=="cross":
        answer=input("You cross the bridge and meet a stranger. Do you want to talk to him (yes/no)? ").lower()
        if answer=="yes":
            print("You talk to the stranger and he gives you gold. You win!")
        elif answer=="no":
            print("You ignore the stranger and he is offended and you lose.")
        else:
            print("Not a valid option. You lose.")
else:
  print("Not a valid option. You lose.")
