class Employee:
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
       
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted the Name!")
        self.first = None
        self.last = None
    
    
#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)

#adding @property enables the access to email as the attribute of parent class
print(emp_1.email)

emp_1.fullname = "Aman Raj"

print(emp_1.email)

del emp_1.fullname

print(emp_1.fullname)