a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))

if(b == 0):
    raise ZeroDivisionError("Our program cant divide a number by zero")

else:
    print(f"The division of number {a} and {b} is {a/b}")