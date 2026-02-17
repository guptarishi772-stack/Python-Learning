a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))
c = int(input("Enter a number 3: "))

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print("The greatest number is: ", greatest(a,b,c)) 