import string
import random

length = int(input("your password length :-"))
 
print('''your password type :
         1. Digits
         2. Letters
         3. Special characters''')
 
characterList = ""

while(True):
    choice = int(input("Select between 1-3 only :-"))
    if(choice == 1):
        characterList += string.digits
        break
    elif(choice == 2):
        characterList += string.ascii_letters
        break
    elif(choice == 3):
        characterList += string.punctuation
        break
    else:
        print("Please select valid option!")
 
password = []
 
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("your random password " + "".join(password))