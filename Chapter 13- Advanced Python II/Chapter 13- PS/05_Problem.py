from functools import reduce
l = [34,53,564,53,53,34535,35345,55,24345]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater, l))