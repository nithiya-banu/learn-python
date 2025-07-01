# **Mini Task 1: Odd Number Printer**

for i  in range(1,20):
    if i % 2 == 0:
        continue
    else:
        print(i)



# **Mini Task 2: Stars in One Line**

i = 1
while i in range(1,6):
    print("*", end= " ")
    i +=1



# **Mini Task 3: Multiplication Table**

for row in range(1,4):
    for col in range(1,4):
        print(f"{row} x {col} = {row*col}")


# **Mini Task: Number Triangle**

# Using Nested For Loops:

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end= " ")
    print()


# Using Nested While Loops

i = 1 
while i <= 5:
    j =1
    while j in range(1,i+1):
        print(j, end= " ")
        j +=1
    print()
    i +=1

