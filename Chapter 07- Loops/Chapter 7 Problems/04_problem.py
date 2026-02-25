n = int(input("Enter the number: "))

for i in range(2, n): 
    if(n%i) == 0:
        print("following number is not prime")
        break


else:
    print("following number is prime")        