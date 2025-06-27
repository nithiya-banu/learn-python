def calculator(a,b,c):
    try:
        if c == "+":
            return a + b
        elif c == "*":
            return a * b
        elif c == "-":
            return a - b
        elif c== "/":
            return a / b
        elif c == "**":
            return a ** b
        elif c == "//":
            return a // b
        elif c == "%":
            return a % b
        else:
            return ("Invalid operator")
    except ZeroDivisionError:
        return ("Cannot divide my zero, Please try again with a different value.")

values = calculator(0,1,"**")
print(f"The result is: {values}")




