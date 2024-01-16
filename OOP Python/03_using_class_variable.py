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

#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)


print(emp_1.pay)

emp_1.apply_raise()

print(emp_1.pay)

print(Employee.__dict__)

#to check that emp_1 doesn't contain the raise amount, but inherits it from the parent class
print(emp_1.__dict__)

print(emp_1.raise_amount)

print(emp_2.raise_amount)

print(emp_2.__dict__)

emp_2.raise_amount = 1.05 #raise amount can be tied to a specific employee, and make it available inside of that class

print(emp_2.raise_amount)

print(emp_1.raise_amount)

print(emp_2.__dict__)

Employee.raise_amount = 1.06 #raises the amount for the whole employee at once

print(emp_2.raise_amount)

print(emp_1.raise_amount)