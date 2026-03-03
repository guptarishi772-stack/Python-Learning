def main():
    try:
        a = int(input("Enter the number: "))
        print(a)

    except Exception as e:
        print(e)

    finally: # This is used in function to run the below
        print("Hey, im inside finally")

main()                