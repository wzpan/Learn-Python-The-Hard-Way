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
