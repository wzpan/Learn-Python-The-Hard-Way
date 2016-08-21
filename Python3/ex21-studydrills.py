#!/usr/bin/env python3

# ex21: Functions Can Return Something

def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

# my function to test return
def isequal(a, b):
    print("Is %r equal to %r? - " % (a, b), end="")
    return (a == b)

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(92, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# switch the order of multiply and divide
what = add(age, subtract(height, divide(weight, multiply(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# test the return value of isequal()
num1 = 40
num2 = 50
num3 = 50

print(isequal(num1, num2))
print(isequal(num2, num3))


# A new puzzle.
print("Here is a new puzzle.")

# write a simple formula and use the function again
uplen = 50
downlen = 100
height = 80
what_again = divide(multiply(height, add(uplen, downlen)), 2)

print("That become: ", what_again, "Bazinga!")