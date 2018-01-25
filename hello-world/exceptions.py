"""
Python provides two very important features to handle any unexpected error in your Python programs 
and to add debugging capabilities in them

Exception Handling
Assertions
"""


def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32


print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
# print KelvinToFahrenheit(-5)

# Handling an exception
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: can\'t find file or read data"
else:
    print "Written content in the file successfully"
    fh.close()

# finally block
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print "Error: can\'t find file or read data"


try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print "Going to close the file"
        fh.close()
except IOError:
    print "Error: can\'t find file or read data"


# Argument of an Exception
# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "The argument does not contain numbers\n", Argument


# Call above function here.
temp_convert("xyz")

# Raising an Exceptions.


def functionName(level):
    if level < 1:
        raise "Invalid level!", level

        # The code below to this would not be executed
        # if we raise the exception
try:
    # Business Logic here...
    print("Business Logic here...")
except "Invalid level!":
    # Exception handling here...
    print("Exception handling here...")
else:
    # Rest of the code here...
    print("Rest of the code here...")


# User - Defined Exceptions
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args
