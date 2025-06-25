
# Ask the user to enter numbers
# Keep accepting numbers until the user enters 0 (use break)
# Print how many numbers were entered before stopping
count = 0
while True:
    num = int(input("enter the number:"))
    if num ==0:
        break
    count += 1
print(f"You have entered {count} numbers before stopping")