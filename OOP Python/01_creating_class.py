class Employee:
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    pass

#creating two different instances of the above class
emp_1 = Employee("Harsh", "Verma", 25000)

print(emp_1.email)