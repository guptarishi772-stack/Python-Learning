class employee:
    language = "Python"
    salary = 200000

    def __init__(self): # dunder method which is automatically called.
        print("i am creating an object")

    def getInfo(self):
        print(f"language is {self.language}. salary is {self.salary}") 


Simon = employee()
print(Simon.language, Simon.salary)