fav_num  =[26,12,3]

fav_num = tuple(fav_num)
print(fav_num)

fruits = {"apple", "orange", "banana", "mango", "guava"}
fruits.add("jack fruit")
print(fruits)

fruits.discard("mango")
print(fruits)

my_profile = {"name" : "Nithiya",
              "skills" : ["Python", "SQL"],
              "is_active" : True}
print(my_profile)

my_profile.update({"skills" : ["Python", "SQL", "Excel"]})
print(my_profile)

for keys, values in my_profile.items():
    print(f" {keys} : {values}")