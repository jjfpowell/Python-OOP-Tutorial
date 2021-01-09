#Python OOP pt.6
"""
A property decorator allows the use of functions such as'getter', 'setters' and 'deleters'.
"""
class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property 
    def email(self):
        return ("{}.{}@gmail.com".format(self.first,self.last))
    
    @property # This decorator essentially turns the method into an attribute of the Employee class.
    def fullname(self):
        return ("{} {}".format(self.first,self.last))

    @fullname.setter # This method is called when you use 'self.fullname=xyz' 
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
    
    @fullname.deleter # This method is called when you use 'del self.fullname' 
    def fullname(self):
        print("Deleted Name!")
        self.first=None
        self.last=None

emp_1=Employee("Jeff","Stevens")
emp_1.fullname='Corey Schafer'

# Without the use of property decorators, the print statements below would return:
# Jim Jeff.Stevens@gmail.com Jim Stevens
# This is because the email is not updated when "first" is set again.
# While one soltion would be to use a method like fullname() anyone else in the code using the class would have to go back through
# and change every instance of the email attribute with an email method.

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname