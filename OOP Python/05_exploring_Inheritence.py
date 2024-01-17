class Employee:

    raise_amount = 1.04
    no_of_emp = 0

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + "." + last + "@company.com"
        #self.fullname = first + " " + last #this method can be separated using new function
        Employee.no_of_emp += 1
    
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())




#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)
dev_1 = Developer("Harsh", "Verma", 25000, "Python")
dev_2 = Developer("Test", "Experiment", 10000, "Java")
emp_2 = Employee("Test", "Experiment", 10000)
mgr_1 = Manager("Harsh", "Verma", 25000, [emp_1])
#mgr_2 = Manager("Test", "Experiment", 10000, [dev_1])

#print(dev_1.email())
#print(dev_1.pay)

#print(help(Developer)) #shows the message resolution order

#print(Developer.__dict__)

#print(help(Manager))

#mgr_1.print_emps()
#mgr_2.print_emps()

#mgr_1.add_emp(dev_2)

#mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))