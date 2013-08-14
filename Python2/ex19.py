#!/bin/python2
# -*- coding: utf-8 -*-

# ex19: Functions and Variables

# Define a function named "cheese_and_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# Print "We can just give the function numbers directly:"
print "We can just give the function numbers directly:"
# Call the function, with 2 numbers as the actual parameters
cheese_and_crackers(20, 30)

# Print "OR, we can use variables from our script:"
print "OR, we can use variables from our script:"
# assign 10 to a variable named amount_of_cheese
amount_of_cheese = 10
# assign 50 to a variable named amount_of_crackers
amount_of_crackers = 50

# Call the function, with 2 variables as the actual parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print "We can even do math inside too:"
print "We can even do math inside too:"
# Call the function, with two math expression as the actual
# parameters. Python will first calculate the expressions and then
# use the results as the actual parameters 
cheese_and_crackers(10 + 20, 5 + 6)

# Print "And we can combine the two, variables and math:"
print "And we can combine the two, variables and math:"
# Call the function, with two expression that consists of variables
# and math as the actual parameters
cheese_and_crackers(amount_of_cheese + 100, amount_of_cheese + 1000)


def print_args(*argv):
    size = len(argv)
    print size
    print "Hello! Welcome to use %r!" % argv[0]
    if size > 1:
        for i in range(1, size):
            print "The param %d is %r" % (i, argv[i])
        return 0
    return -1


# 1. use numbers as actual parameters
print_args(10, 20, 30)

# 2. use string and numbers as actual parameters
print_args("print_args", 10, 20)

# 3. use strings as actual parameters
print_args("print_args", "Joseph", "Pan")

# 4. use variables as actual parameters
first_name = "Joseph"
last_name = "Pan"
print_args("print_args", first_name, last_name)

# 5. contain math expressions
print_args("print_args", 5*4, 2.0/5)

# 6. more complicated calculations
print_args("print_args", '.'*10, '>'*3)

# 7. more parameters
print_args("print_args", 10, 20, 30, 40, 50)

# 8. tuples as parameters
nums1 = (10, 20, 30)
nums2 = (40, 50, 60)
print_args("print_args", nums1, nums2)

# 9. more complicated types
nums3 = [70, 80, 90]
set1 = {"apple", "banana", "orange"}
dict1 = {'id': '0001', 'name': first_name+" "+last_name}
str1 = "Wow, so complicated!"
print_args("print args", nums1, nums2, nums3, set1, dict1, str1)

# 10. function as parameter and return values
if print_args(cheese_and_crackers, print_args) != -1:
    print "You just send more than one parameter. Great!"
