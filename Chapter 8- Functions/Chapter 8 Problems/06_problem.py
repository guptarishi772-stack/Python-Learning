# Conversion of inches to cm
def inch_to_cm(inch):
    cm = inch*2.54
    return cm
inch = float(input("Enter inch: "))
cm = inch_to_cm(inch) 
print(f"{inch} inches is equal to {round(cm, 2)} cm")