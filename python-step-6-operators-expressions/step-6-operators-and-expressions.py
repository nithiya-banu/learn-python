
while True:
    num1, num2 = map(int,input("enter two numbers separated by comma:").split(",")) 

    while True:
        print("select an operation from the below options:")
        print("+  -  *  /  //   %  ** ")
        user_input = input("Enter your choice of operator:")
        if user_input == "+":
            print(f"Result : {num1 + num2}")
            break
        elif user_input == "-":
            print(f"Result : {num1 - num2}")
            break
        elif user_input == "*":
            print(f"Result : {num1 * num2}")
            break
        elif user_input == "/":
            print(f"Result : {num1 / num2}")
            break
        elif user_input == "//":
            print(f"Result : {num1 // num2}")
            break
        elif user_input == "%":
            print(f"Result : {num1 % num2}")
            break
        elif user_input == "**":
            print(f"Result : {num1 ** num2}")
            break
        else:
            print("Invalid Operator")
        continue

    
    try_again = input("Try Again [Yes/No]:")
    if try_again.lower() == "yes":
        continue
    elif try_again.lower() == "no":
        print("Thank You for using the smart calculator")
        break
    else:
        print("Invalid Input")
        continue
