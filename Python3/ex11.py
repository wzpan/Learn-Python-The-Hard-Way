#!/bin/python3

# ex11: Asking Questions

# raw_input() was renamed to input() in Python v3.x,
# and the old input() is gone, but you can emulate it with eval(input())

print("How old are you?", end=" ")
age = input()  
print("How tall are you?", end=" ")
height = input()
print("How much do you weight", end=" ")
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
