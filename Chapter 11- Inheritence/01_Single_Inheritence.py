class Employee:
    Company = "JP Morgan & Chase"
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

class Programmer(Employee): # Instrad of writing same code many times, just use this
    Company = "Morgan Stanly"
    def showLanguage(self):
        print(f"The name of the programmer is {self.name} and he is good with {self.language} language")
a = Employee()
b = Programmer()
print(a.Company, b.Company)        