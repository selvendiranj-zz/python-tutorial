"""
def functionname(parameters):
    "function_docstring"
    function_suite
    return [expression]
"""

# Function definition is here


def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Function definition is here


def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4])
    print "Values inside the function: ", mylist
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print "Values outside the function: ", mylist

# Function definition is here


def changeme(mylist):
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4]  # This would assign new reference in mylist
    print "Values inside the function: ", mylist
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print "Values outside the function: ", mylist

# #####################################
# Required arguments
# #####################################
# To call the function printme(), you definitely need to pass one argument,
# otherwise it gives a syntax error as follows

# Function definition is here


def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


# Now you can call printme function
printme("Hello Python")

# #####################################
# Keyword arguments
# #####################################
# You can also make keyword calls to the printme() function in the following ways

# Function definition is here


def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


# Now you can call printme function
printme(str="My string")


# Function definition is here


def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# Now you can call printinfo function
printinfo(age=50, name="miki")

# #####################################
# Default arguments
# #####################################

# Function definition is here


def printinfo(name, age=35):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age ", age
    return


# Now you can call printinfo function
printinfo(age=50, name="miki")
printinfo(name="miki")

# #####################################
# Variable-length arguments
# #####################################

# Function definition is here


def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print "Output is: "
    print arg1
    for var in vartuple:
        print var
    return


# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50)

# #####################################
# The Anonymous Functions
# #####################################
# Function definition is here


def sum(arg1, arg2): return arg1 + arg2


# Now you can call sum as a function
print "Value of total : ", sum(10, 20)
print "Value of total : ", sum(20, 20)

# #####################################
# The return Statement
# #####################################
# Function definition is here


def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    print "Inside the function : ", total
    return total


# Now you can call sum function
total = sum(10, 20)
print "Outside the function : ", total

# #####################################
# Global vs. Local variables
# #####################################

total = 0  # This is global variable.
# Function definition is here


def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2  # Here total is local variable.
    print "Inside the function local total : ", total
    return total


# Now you can call sum function
sum(10, 20)
print "Outside the function global total : ", total
