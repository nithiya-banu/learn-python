User_Age = int(input("Enter your age:"))
if User_Age >= 0 and User_Age <= 12:
    print("User is child")
elif User_Age >= 13 and User_Age <= 19:
    print("User is Teen")
elif User_Age >= 20 and User_Age <= 59:
    print("User is Adult") 
else:
    print("User is Senior Citizen")