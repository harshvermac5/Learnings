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
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)


#print(emp_1.__repr__())
#print(emp_1.__str__())

#print(str(emp_1))
#print(repr(emp_1))

print(Employee.__add__(emp_1, emp_2))

print(emp_1.__len__())