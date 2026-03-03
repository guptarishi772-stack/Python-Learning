# This file will be used to write a code and import it into main.py file

def myFunc():
    print("This code has been imported from 11_module.py")


if __name__ == "__main__": # When we are running the code present in file itslef
    print("We are directly running this code")
    myFunc()
    print(__name__)