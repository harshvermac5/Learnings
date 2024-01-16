class Employee:
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        self.fullname = first + " " + last
    pass

#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)


print(emp_1.first)


#printing first and last name manually
print("{} {}".format(emp_2.first, emp_2.last))

print(emp_1.fullname)