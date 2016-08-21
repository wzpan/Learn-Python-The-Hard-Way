#!/usr/bin/env python3

# ex13: Parameters, Unpacking, Variables
# Combine input with argv to make a script that gets more input from a user.

from sys import argv

script, first_name, last_name = argv

middle_name = input("What's your middle name?")

print("Your full name is %s %s %s." % (first_name, middle_name, last_name))