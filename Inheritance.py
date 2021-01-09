#Python OOP pt.4
"""
Inheritance allows us to inherit methods and attributes from a parent class. This allows us to create sub-classes with the same 
functionality and then overwrite or add new functionality without affecting the parent class. In this example we will be creating
different types of staff.
A chain of inheritance is called a 'Method Resolution Order'.
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

class Developer(Employee): # To pass in additional attributes, you must add another __init__ method
    raise_amount=1.10
    def __init__(self,first,last,pay,lang):
        super().__init__(first,last,pay) #Allows the employee to handle first,last,pay
        # Employee.__init__(self,first,last,pay) this is also valid
        self.lang=lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    
    def add_emp(self, emp): # If 
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())
    

dev_1=Developer("Jeff","Stevens",500,"Java")
dev_2=Developer("Test","User",200,"Python")
mgr_1 = Manager("Sue","Smith",900,[dev_1])

print(dev_1.email)
print(dev_1.lang)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager)) # This function will test us if an object is an isntance of a class. Returns Bool.
print(issubclass(Manager, Developer)) # Tells us if a class is a sub-class of another.