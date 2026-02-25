class Employee:
    language = "python"
    salary = "2,00,000" #200000 if not using upper commas

Sofia = Employee()
Sofia.language = "javaScript" # javascript will be printed as Instance gets priority
print(Sofia.language, Sofia.salary)   