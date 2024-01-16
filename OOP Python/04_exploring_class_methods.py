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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last ,pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)

Employee.set_raise_amt(1.06) #updates the values for the whole class

print(Employee.__dict__)

print(emp_1.__dict__)

print(emp_2.__dict__)

emp_3 = Employee.from_str("John-Doe-20000")

print(Employee.__dict__)

print(emp_3.__dict__)

import datetime

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))