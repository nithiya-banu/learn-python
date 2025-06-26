student = {"name" : "Nithiya",
           "age" :"23",
           "course" : "Python",
           "grade" : "A"}

print(student["course"])

# adding new key
student.update({"gender" : "F"})

# updating the grade
student.update({"grade" : "A+"})
print(student)

# using .get() to check if marks key exists
student.get["marks"]
# print(student)
# gives  no error 

# printing all keys, values, and items
print(student.keys())
print(student.values())
print(student.items())

# removing age from student
student.pop("age")
# print(student)

# looping through dict to print all values
for keys,values in student.items():
    print(f"{keys} : {values}")

