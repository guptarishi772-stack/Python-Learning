class Employee:
    a = 1

class Programmer(Employee):
    b = 3

class Manager(Programmer):   
    c = 5

o = Employee()
print(o.a) 

o = Manager()
print(o.a, o.b, o.c)     
