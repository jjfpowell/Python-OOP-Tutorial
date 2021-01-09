#Python OOP pt.2
"""
Class variables are variables that are shared between ALL instances of a class.
A company gives anual raises each year that is the same for all empolyees.
When you call a class variable, it will first look to see if that instance contains that attribute, if it doesn't it will see if
any class or any class it inherits from.
"""
class Employee:
    raise_amount=1.04 #This is a class variable
    num_of_emps=0 #A second class variable
    """However, for the raises it is nice to be able to have an overarching class value that can be overwritten per instances if needed,
    but for number of employees, create an instance of an employee is only ever going to add 1"""
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@gmail.com"
        Employee.num_of_emps += 1 #For this variable, it would make sense to use self as this number will not change depending on the emp.
    
    def fullname(self):
        return ("{} {}".format(self.first,self.last))
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount) #Changing this to 'Employee' wouldn't allow the class variable to be set per instance.
        
emp_1=Employee("Jeff","Stevens",500)
emp_2=Employee("Test","User",200)

emp_1.raise_amount = 1.05 #Although this instance doesn't contain raise_amount, it can be assigned to its name space (See print below).

print(emp_1.__dict__)

print(Employee.raise_amount) #This will print out the class variable.
print(emp_1.raise_amount) #This instance has a seperate value so will return a different value.
print(emp_2.raise_amount)

print(Employee.num_of_emps)