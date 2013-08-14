#!/bin/python2
# -*- coding: utf-8 -*-

# ex5: More Variables and Printing

name = 'Zed A. Shaw'
age = 35       # not a lie
height = 74   # inches
weight = 180  # lbs
eyes = "Blue"
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d years old." % age
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % (teeth)

# this line is tricky, try to get it exactly right
print 'If I add %d, %d and %d I get %d.' % (age, height, weight, age + height + weight)

# try more format characters
my_greeting = "Hello,\t"
my_first_name = 'Joseph'
my_last_name = 'Pan'
my_age = 24
# Print 'Hello,\t'my name is Joseph Pan, and I'm 24 years old.
print "%rmy name is %s %s, and I'm %d years old." % (my_greeting, my_first_name, my_last_name, my_age)

# Try to write some variables that convert the inches and pounds to centimeters and kilos.
inches_per_centimeters = 2.54
pounds_per_kilo = 0.45359237

print "He's %f centimeters tall." % (height * inches_per_centimeters)
print "He's %f kilos heavy." % (weight * pounds_per_kilo)
