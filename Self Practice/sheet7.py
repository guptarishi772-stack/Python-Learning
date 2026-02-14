# 1. Defining the Function (Chapter 8)
def rate_student(subject_list):
    # Using len() to count items in a List (Chapter 4)
    total = len(subject_list)
    
    print(f"\nYou have {total} subjects in your list.")
    
    # Decision Making Logic (Chapter 6)
    if total > 3:
        print("Status: Heavy Load! Focus on time management.")
    else:
        print("Status: Manageable Load. Keep up the good work.")

# 2. Starting our main program
my_subjects = ["Mathematics", "BEEE", "Physics"]

# 3. Taking User Input (Chapter 2)
new_sub = input("Enter a new subject to add: ")

# 4. Modifying the List (Chapter 4)
my_subjects.append(new_sub)

# 5. Calling the Function (Passing the list as an Argument)
rate_student(my_subjects)