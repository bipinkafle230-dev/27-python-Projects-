# simple quiz game
print("welcome to Quiz")

playing =input("Do you want to play? ") #ask the user if they want to play

if playing!="yes":  # if the user does not want to play
    quit() # terminate the program
print("Okay! Let's play :)")

answer=input("who is the best footballer in the world ? ") # ask the user a question
# if answer=="Cristiano Ronaldo":
if answer=="cr7" or answer=="ronaldo" or answer=="Cristiano Ronaldo dos Santos Aveiro": # check if the answer is correct
     print("Correct!") # if the answer is correct
     score=1 # give the user a score of 1  
else:
    print("Incorrect!") # if the answer is incorrect
    score=0 # give the user a score of 0
    
print("Your score is "+ str(score)) # print the user's score

answer=input("who is the best basketball player in the world ? ") # ask the user a question
# if answer=="LeBron James":
if answer=="james" or answer=="lebron james":# check if the answer is correct
     print("Correct!") # if the answer is correct
     score+=1 # give the user a score of 1
else:
    print("Incorrect!") # if the answer is incorrect
    score+=0 # give the user a score of 0

print("Your score is "+ str(score)) # print the user's score

answer=input("who is the best tennis player in the world ? ") # ask the user a question
# if answer=="Novak Djokovic":
if answer=='novak' or answer=="novak djikovic":
     # check if the answer is correct
     print("Correct!") # if the answer is correct
     score+=1 # give the user a score of 1
else:
    print("Incorrect!") # if the answer is incorrect
    score+=0 # give the user a score of 0
print("Your score is "+ str(score)) # print the user's score

answer=input("who is the best cricketer in the world ? ") # ask the user a question
# if answer=="Virat Kohli":
if answer=="kohli" or answer=="virat kohli":
     # check if the answer is correct
     print("Correct!") # if the answer is correct
     score+=1 # give the user a score of 1
else:
    print("Incorrect!") # if the answer is incorrect
    score+=0 # give the user a score of 0

print("Your score is "+ str(score)) # print the user's score

print("You got "+ str((score/4)*100) +"%") # print the user's score in percentage
print("Thanks for playing!") # thank the user for playing
print("Developed by Bipin") # print the developer