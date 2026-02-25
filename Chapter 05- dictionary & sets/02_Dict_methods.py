marks = {
    "Harry" : 40,
    "Rohan" : 89,
    "Putin" : 100

}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Putin" : 59 , "Roman" : 90})
print(marks)
print(marks.get("Putin")) # If wrong name, gives None
print(marks["Putin"]) # If wrong name, gives error

