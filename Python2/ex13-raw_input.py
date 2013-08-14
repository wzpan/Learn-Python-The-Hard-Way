#!/bin/python2
# -*- coding: utf-8 -*-

# ex13: Parameters, Unpacking, Variables
# Combine raw_input with argv to make a script that gets more input from a user.

from sys import argv

script, first_name, last_name = argv

middle_name = raw_input("What's your middle name?")

print "Your full name is %s %s %s." % (first_name, middle_name, last_name)