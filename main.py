import password_generator
print()
print("     !!! H-E-L-L-O !!!!")
print()
print("WELCOME! It's always great to see new faces around ....\n"
    "Don't worry, here we help you set a new strong and safe password\n"
    "")
while True:
    my_password=password_generator
    user_input=input("Please press enter to generate your password ")
    final_password=my_password.password_generator(user_input)
    print(f' This is your password : {final_password}')