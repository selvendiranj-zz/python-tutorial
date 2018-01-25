"""
Loop Control Statements
Loop control statements change execution from its normal sequence. When execution leaves a scope, 
all automatic objects that were created in that scope are destroyed.

Python supports the following control statements. Click the following links to check their detail.
"""

# break statement
for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print
"Good bye!"

# continue statement
for letter in 'Python':  # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :', var)
print("Good bye!")

# Pass Statement
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)

print("Good bye!")
