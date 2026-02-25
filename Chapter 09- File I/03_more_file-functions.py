f = open("file.txt")
'''lines = f.readlines()
print(lines, type(lines))'''


''' for reading a one special line:-
line2 = f.readline2()
print(line2, type(line2))
'''

# By loop method:- 
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()






f.close()