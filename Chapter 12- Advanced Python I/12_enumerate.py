l = [3, 4, 53, 75, 23]

'''index = 0
for item in l:
    index += 1
    print(f"The item number at index {index} is {item}")
'''


for index, item in enumerate(l):
    print(f"The item number at {index} is {item}")    