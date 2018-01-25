"""
Python Numbers
Number data types store numeric values. Number objects are created when you assign a value to them.
"""

# For example −
var1 = 1
var2 = 10
varN = 'N'

# You can also delete the reference to a number object by using the del statement.
# The syntax of the del statement is −
del var1, var2, varN

# You can delete a single object or multiple objects by using the del statement.
# For example −
var = 'var'
var_a, var_b = 'var_a', 'var_b'
del var
del var_a, var_b

# Python supports four different numerical types −
"""
int     (signed integers)
long    (long integers, they can also be represented in octal and hexadecimal)
float   (floating point real values)
complex (complex numbers)
"""

# Examples
# Here are some examples of numbers −
"""
int	    long	                float	    complex
10	    51924361L	            0.0	        3.14j
100	    -0x19323L	            15.20	    45.j
-786	0122L	                -21.9	    9.322e-36j
080	    0xDEFABCECBDAECBFBAEl	32.3+e18	.876j
-0490	535633629843L	        -90.	    -.6545+0J
-0x260	-052318172735L	        -32.54e100	3e+26J
0x69	-4721885298529L	        70.2-E12	4.53e-7j
"""

# Python allows you to use a lowercase l with long, but it is recommended
# that you use only an uppercase L to avoid confusion with the number 1. 
# Python displays long integers with an uppercase L.

# A complex number consists of an ordered pair of real floating-point numbers 
# denoted by x + yj, where x and y are the real numbers and j is the imaginary unit.
