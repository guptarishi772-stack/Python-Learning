def divisible5(n):
    if n%5== 0:
        return True
    return False

a = [34,5465,5,67,43,870]

f = list(filter(divisible5, a))
print(f)