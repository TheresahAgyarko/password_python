import string
import random
 

# using function
def password_generator(length=12,character=string.ascii_letters + string.digits + string.punctuation): #function
    return''.join(random.choice(character)for i in range(12))

option=input("Do you want to generate a password (Yes/No) : ")

# using control structure
try:
    if option=="Yes":
    
     password_generator()
    elif option=="No":
     print("Program end") 
except ValueError:
    print("invalid input please enter (Yes/No)")
         