n = int(input("Enter the number: "))

table = [n*i for i in range (1,11)]
with open("Table.txt", "a") as f:
    f.write(f"The table of {n}: {str(table)} \n")