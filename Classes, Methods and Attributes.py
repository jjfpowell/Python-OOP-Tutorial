#Python OOP pt.1
"""In a company, each employee is going to have specific attributes and methods.
They will have a name, email, pay and actions they can perfrom.
A class would be useful to act a bluerpint.
A class is a blueprint for creating an istance.
Each unique employee that we create from the blueprint acts as an instance of a class.
A method is simply a function within a class
An attribute is the variable that a method takes.
"""

class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@gmail.com"
    
    def fullname(self):
        return ("{} {}".format(self.first,self.last))


emp_1=Employee("Jeff","Stevens",500)
emp_2=Employee("Test","User",200)

print(emp_1.email)
print(emp_2.last)

print(emp_1.fullname())
print(emp_2.fullname())