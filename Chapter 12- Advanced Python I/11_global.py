a = 60 # Global variable
def fun():
    global a # Changes global variable
    a = 7
    print(a)

fun() 
