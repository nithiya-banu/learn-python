# 🔸 STEP 1: Variables & Data Types
# Question: What will be the type of the output for this?

# python
# Copy code
# age = input("Enter your age:")
# print(type(age))
# Write a program that stores your name, age, and country, then prints a sentence like:

# "Hi, I'm Nithiya, 23 years old from India."
age = input("Enter your age:")
print(type(age))

name = "Nithiya"
age = 23
country = "India"
print(f"Hi, I'm {name}, {age} years old from {country}")

# 🔸 STEP 2: Conditions
# Logic Debug:
# The following code checks if a number is even or odd, but there's a bug. Can you fix it?

# python
# Copy code
# number = int(input("Enter a number:"))
# if number % 2 = 0:
#     print("Even")
# else:
#     print("Odd")
# Write a grading system:

# Marks ≥ 90 → A

# 75-89 → B

# 60-74 → C

# 40-59 → D

# Below 40 → F



number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


mark = int(input("Enter your mark"))
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 40:
    print("Grade D")
else:
    print("Grade F")

# 🔸 STEP 3: Loops & Menu

# Write a loop to print all odd numbers from 1 to 15.

# Write a menu-based system to:

# Greet the user

# Ask for an option (1. Hello 2. Bye 3. Exit)

# Keep looping until the user chooses Exit.



for i in range(1,16):
    if i % 2 == 0:
        continue
    else:
        print(i)

name = input("Enter your name:")

while True:
    print(f"Welcome {name}")
    print("1.Hello")
    print("2.Bye")
    print("3.Exit")
    print("\n")
    user_choice = int(input("Enter the option no."))
    if user_choice == 3:
        break
    else:
        continue

# 🔸 STEP 4: Collections (List, Set, Dictionary, Tuple)

# Write code that:

# Creates a list of your 3 favorite books

# Adds 1 more book

# Removes the second book

# Sorts the list

# Write code using a dictionary to store:

# name

# age

# skills (as a list)

# Then update the skills by adding one more and print everything.

fav_books = ["You can Win","Sherlock Holmes","Psychology of Money"]
print(fav_books)
fav_books.append("Detective Stories")
print(fav_books)
fav_books.remove("Sherlock Holmes")
print(fav_books)
fav_books.sort()
print(fav_books)


my_details = {"name" : "Nithiya", "age" : "23", "skills" : ["SQL", "Python", "Excel"]}
print(my_details)
my_details["skills"].append("PowerBI")
print(my_details)

