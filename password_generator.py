import string
import random
 #ascci is use to generate both lower  and uppercase letters

# using function
def password_generator(length=12,character=string.ascii_letters + string.digits + string.punctuation): #Definding function
    return''.join(random.choice(character)for i in range(12))

option=input("Do you want to generate a password (Yes/No) : ")

# using control structure
if option=="Yes":
    # ivoke the function
    password_generator()
elif option=="No":
    print("Program end") 
else:    
    print("Invalid input,please enter (Yes/No) :")  
         