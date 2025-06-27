books = {"sherlock", "Holmes","Harry","Potter","Percy"}

# Trying to add one duplicate book
books.add("sherlock")
# It just ignored the duplicate sherlock

# adding new book using add()
books.add("Jackson")

# removing a book using discard()
books.discard("Matilda")

print(books)

for i in books:
    print(i)

