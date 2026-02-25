# Following code converts the temperature in celcius into fahrenheit and rounds it to 2 decimal places.
def c_to_f(c):
    f = (c * 9/5) + 32
    return round(f, 2)
c = int(input("Enter temperature in Celsius: "))
f = c_to_f(c)
print(f"{c} is equal to {f} °F")