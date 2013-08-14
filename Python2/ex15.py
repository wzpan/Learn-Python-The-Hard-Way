#!/bin/python2
# -*- coding: utf-8 -*-

# ex15: Reading Files

# prompt to type the file name
print "Type the filename:"
# input the file name
filename = raw_input("> ")

# open the selected file
txt = open(filename)

# print file name
print "Here's your file %r:" % filename
# print all the contents of the file
print txt.read()
