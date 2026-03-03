myList = [2,5,46,432]

squaredList = []

for item in myList:
    squaredList.append(item*item)

squaredList = [i*i for i in myList]


print(squaredList)    