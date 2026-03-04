from functools import reduce 
# Map Example:-
l = [23,1,345,666,73921]
square = lambda x: x*x
sqList = map(square, l)
print(list(sqList))

# Filter Example
def even(n):
    if (n%2 == 0):
        return True
    return False
OnlyEven = filter(even, l)
print(list(OnlyEven))

# Reduce Example
def sum (a,b):
    return a+b

mul = lambda x,y:x*y 
print(reduce(sum, l))
print(reduce(mul, l))
