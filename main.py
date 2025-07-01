import password_generator

while True:
    my_password=password_generator
    user_input=input("Please type continue to generate your password : ")
    final_password=my_password.password_generator(user_input)
    print(f' This is your password : {final_password}')