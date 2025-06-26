Username = "nithiya"
Password = "python123"
username_input = input("Please Enter your username:")
password_input = input("Please Enter your password:")
if username_input != Username and password_input == Password:
    print("Invalid Username")
elif username_input == Username and password_input != Password:
    print("Invalid Password")
elif username_input != Username and password_input != Password:
    print("Invalid Username and Password")
else:
    print("Login Successful")
