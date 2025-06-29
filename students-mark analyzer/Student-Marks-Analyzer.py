try:
    name = input("Enter you name:")
    if not name.isalpha():
        print("Please enter alphabetic value as name!")
        exit()
    sub1 = int(input("Enter marks for subject 1:"))
    sub2 = int(input("Enter marks for subject 2:"))
    sub3 = int(input("Enter marks for subject 3:"))
    Total = sub1 +sub2 + sub3
    Average = Total//3
    if Average >= 90:
        Grade = "A"
    elif Average >= 75:
        Grade = "B"
    elif Average >= 60:
        Grade = "C"
    elif Average >=40:
        Grade = "D"
    else:
        Grade = "F"
    print(f"----------Result Summary------------\n"
    f"        {'Name'     :<10}:  {name}                \n" 
    f"        {'Total'    :<10}:  {Total}/300               \n"
    f"        {'Average'  :<10}:  {Average}             \n"
    f"        {'Grade'    :<10}:  {Grade}               ")
except ValueError:
    print("Please use numeric values for marks!")

