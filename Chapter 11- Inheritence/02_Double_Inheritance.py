class Employee:
    Company = "JP Morgan & Chase"
    name = "Larry Fink"
    def show(self):
        print(f"The name of the employee is {self.name} and company name is {self.Company}")

class coder: 
    language= "Python"
    def printLanguages(self):
        print(f"Out of all languages here is your language: {self.language}")

class Programmer(Employee, coder): # Instrad of writing same code many times, just use this
    Company = "Morgan Stanly"
    def showLanguage(self):
        print(f"The name of the programmer is {self.Company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()   
b.showLanguage()  