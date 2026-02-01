# Task-1:
# Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

#ANS:

a = int(input("enter 1 no: "))
b = int(input("enter 2 no: "))

sum = a + b
sub = a - b
mul = a * b
div = a / b

print("The sum of", a, "and", b, "is:", sum)
print("The subtraction of", a, "and", b, "is:", sub)
print("The multiplication of", a, "and", b, "is:", mul)
print("The division of", a, "and", b, "is:", div)

# output:
# enter 1 no:  25
# enter 2 no:  24
# The sum of 25 and 24 is: 49
# The subtraction of 25 and 24 is: 1
# The multiplication of 25 and 24 is: 600
# The division of 25 and 24 is: 1.0416666666666667

