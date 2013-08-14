#!/bin/python3

# ex15: Reading Files

# import argv variables from sys submodule
from sys import argv

# get the argv variables
script, filename = argv

# open a file
txt = open(filename)

# print file name
print("Here's your file %r: " % filename)
# print all the contents of the file
print(txt.read())
