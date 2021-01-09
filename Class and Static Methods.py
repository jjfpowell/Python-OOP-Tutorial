#Python OOP pt.3
"""
Regular methods in a class, automatically take the instance as the first argument. By convention you call this self.
If we want a method to take the Class as the argument, we use Class methods.
Regular Methods within a class = First arguement passed automatically == 'self'
Class Methods within a class = First arguement passed automatically == 'cls'
Static Methods within a class = Don't pass anything automatically.
"""
import datetime

class Employee:
    raise_amount=1.04
    num_of_emps=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@gmail.com"
        Employee.num_of_emps += 1
    
    def fullname(self):
        return ("{} {}".format(self.first,self.last))
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    
    @classmethod #This is a decorator which defines the method as a class method.
    #This alters the functionality of the method so it now takes the class as the first attribute instead of the instance.
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod #This is an example of an alternative constructor.
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

    #Static Method: Have logical connection to a class. If we wanted to create a function which takes in a date and returns if
    # it is a work day. This is logical in our employee class but doesn't depend on any instance or class variable. So we make it 
    # a Static method.
    
    @staticmethod #If you don't access an instance or the class within the function, it should be a static function.
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

        
emp_1=Employee("Jeff","Stevens",500)
emp_2=Employee("Test","User",200)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# You can use class methods to provide multiple ways of creating your objects. This is useful if you have a specific use cases.
# Eg. If someone is using your class but needs to input using a string with info seperated by hyphens.

emp_str_1="John-Doe-700"
emp_str_2="Steve-Smith-300"
emp_str_3="James-Doe-900"

new_emp_1=Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

my_date=datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))