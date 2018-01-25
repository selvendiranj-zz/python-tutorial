"""
A Python program can handle date and time in several ways.
Converting between date formats is a common chore for computers.
Python's time and calendar modules help track dates and times.
"""
import time      # This is required to include time module.
import calendar  # This is required to include calendar module.

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)


# Getting current time

localtime = time.localtime(time.time())
print("Local current time :", localtime)

# Getting formatted time

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

# Getting calendar for a month

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)
