marks1 = int(input("Enter your marks1: "))
marks2 = int(input("Enter your marks2: "))
marks3 = int(input("Enter your marks3: "))

total_percentage = (100*(marks1 + marks2 + marks3 ))/300 

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed", total_percentage)

else:
    print("You failed. Better luck next time.", total_percentage)