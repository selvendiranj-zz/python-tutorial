# #####################################
# Printing to the Screen
# #####################################


print "Python is really a great language,", "isn't it?"

# #####################################
# Reading Keyboard Input
# #####################################

# reads one line from standard input
# str = raw_input("Enter your input: ")
# print "Received input is : ", str

# equivalent to raw_input, but the input should be valid Python expression
# str = input("Enter your input: ")
# print "Received input is : ", str

# #####################################
# Opening and Closing Files
# #####################################
# file object = open(file_name [, access_mode][, buffering])
# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
# Close opend file
fo.close()

# #####################################
# Reading and Writing Files
# #####################################
# Open a file
fo = open("foo.txt", "wb")
fo.write("Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print "Read String is : ", str
# Close opend file
fo.close()

# #####################################
# File Positions
# #####################################
# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print "Read String is : ", str

# Check current position
position = fo.tell()
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print "Again read String is : ", str
# Close opend file
fo.close()

# #####################################
# Directories in Python and OS module
# #####################################

# The remove() Method
import os

# Delete file test2.txt
os.remove("text2.txt")

# Create a directory "test"
os.mkdir("test")

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

# This would give location of the current directory
os.getcwd()

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )


