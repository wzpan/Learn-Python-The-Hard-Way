#!/usr/bin/env python3

# ex13: Parameters, Unpacking, Variables
# Write a script that has fewer arguments

from sys import argv

script, first_name, last_name = argv

print("The script is called:", script)
print("Your first name is:", first_name)
print("Your last name is:", last_name)