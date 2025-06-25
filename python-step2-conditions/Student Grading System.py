User_Mark = int(input("Enter your Mark(o-100):"))
if User_Mark > 100 or User_Mark < 0 :
    print("Invalid Mark!Please enter a mark between 0 and 100.")
elif User_Mark >= 90:
    print("You secured Grade A")
elif User_Mark >= 75:
    print("You secured Grade B")
elif User_Mark >= 60:
    print("You secured Grade C")
elif User_Mark >= 40:
    print("You secured Grade D")
else:
    print("You failed, Better Luck Next Time!!")