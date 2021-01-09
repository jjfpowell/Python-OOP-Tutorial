#Python OOP pt.5
"""
Depedning on the object you are working with, there maybe different results. 1+2=3 and 'a'+'b'= ab.
By defining you own special methods, you are able to change built-in behaviour and operations.
Special methods are always surrounded by __xyz__ 'Dunder'
"""
class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@gmail.com"
    
    def fullname(self):
        return ("{} {}".format(self.first,self.last))
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    
    def __repr__(self): # Unambigous representation of an object. Used for debugging and logging.
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
        # If you wanted to recreate the employee object you could from the output.
    def __str__(self): # More readable representation of an object to be shown to an end user.
        return '{} - {}'.format(self.fullname(),self.email)
    def __add__(self,other): # This function changes the functionality of the '+' operator to allow emp_1+emp_2
        return self.pay+other.pay
    def __len__(self): # Function returns the length of an employees full name.
        return len(self.fullname)

emp_1=Employee("Jeff","Stevens",500)
emp_2=Employee("Test","User",200)

print(emp_1+emp_2)
print(repr(emp_1))
print(str(emp_1))

# print(1+2) # Both provide a result of three. The second is accessing the interger object
# print(int.__add__(1+2))
# print(str.__add__('a'+'b'))

