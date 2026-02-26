import random 
n = random.randint(1,50)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("lower number please")
        guesses += 1
    elif(a<n):
        print("higher number please")  
        guesses += 1      
            
print(f"You have guessed {n} in {guesses} attempt")            

input("Press Enter to exit...")
