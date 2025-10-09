from cryptography.fernet import Fernet #for encryption and decryption of passwords

# Password manager 
master_pwd=input("What is the master password?")



def view():
   with open("passwords.txt","r") as f: #opening the file in append mode
    for line in f.readlines():
       data = (line.rstrip()) #printing the lines without extra new line
       user,passw=data.split("|") #splitting the name and password using("|") 
    print("Account:",user,"| Password:",passw) #printing the name and password
       

def add(): # adding 
    name=input("Account Name: ")
    pd=input("Password: ") 

    with open("passwords.txt","a") as f: #opening the file in append mode
        f.write(name + "|" + pd + "\n") #writing the name and password in the file


while True:
 mode=input("would you like to add a new password or view existing ones (view/add)? Press q to quit ::")
 if mode=="q":
    break
 if mode=="view":
    view()
    pass
 elif mode=="add":
    add()
    pass
 else:
    print( "Invalid mode")
    continue
 