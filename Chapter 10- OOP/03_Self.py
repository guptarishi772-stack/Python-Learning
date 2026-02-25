class Employee: 
    language = "Python"
    salary = 150000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod # it allows us to dont give an object (silented Rohan)
    def greet():
        print("Good Moring")
Rohan = Employee()
# Rohan.language = "C++"
Rohan.getInfo()        