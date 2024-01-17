class Employee:
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + "." + last + "@company.com"
        #self.fullname = first + " " + last #this method can be separated using new function
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)
emp_2 = Employee("Test", "Experiment", 10000)

#adding @property enables the access to email as the attribute of parent class
print(emp_1.email)

emp_1.fullname = "Aman Rajc"

print(emp_1.email)