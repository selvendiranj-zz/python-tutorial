"""
Python Strings
Strings in Python are identified as a contiguous set of characters represented in the quotation marks.
Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the 
slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and 
working their way from -1 at the end.

The plus (+) sign is the string concatenation operator
The asterisk (*) is the repetition operator. 
"""

# For example −
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string
