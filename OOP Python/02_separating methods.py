class Employee:
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + "." + last + "@company.com"
        #self.fullname = first + " " + last #this method can be separated using new function
    
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)


print(emp_1.first)

print(emp_1.fullname())

print(emp_2.email())