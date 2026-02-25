'''f = open("file.txt)
print(f.read())
f.close()
'''
# Above statement can be written using with statement like this:-
with open("file.txt") as f:
    print(f.read())

#Instead of explicitly closin the file    