#######################################
# Accessing Attributes
#######################################


class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
# del emp1.age  # Delete 'age' attribute.

hasattr(emp1, 'age')  # Returns true if 'age' attribute exists
getattr(emp1, 'age')  # Returns value of 'age' attribute
setattr(emp1, 'age', 8)  # Set attribute 'age' at 8
delattr(emp1, 'age')  # Delete attribute 'age'


#######################################
# Built-In Class Attributes
#######################################


class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

#######################################
# Destroying Objects (Garbage Collection)
#######################################
a = 40  # Create object <40>
b = a  # Increase ref. count  of <40>
c = [b]  # Increase ref. count  of <40>

del a  # Decrease ref. count  of <40>
b = 100  # Decrease ref. count  of <40>
c[0] = -1  # Decrease ref. count  of <40>


# class can implement the special method __del__(), called a destructor


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the obejcts
del pt1
del pt2
del pt3


#######################################
# Class Inheritance
#######################################


class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method


# Multiple inheritance


class A:  # define your class A
    """....."""


class B:  # define your class B
    """....."""


class C(A, B):  # subclass of A and B
    """....."""
