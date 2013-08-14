#!/bin/python2
# -*- coding: utf-8 -*-

# ex11: Asking Questions

# input(): Read a value from standard input. Equivalent to eval(raw_input(prompt)).
# raw_input(): Read a string from standard input. The trailing newline is stripped.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "Enter a integer: ",
num = int(raw_input())
print "The number you've input is: %d" % num

print "Enter a name: ",
name = raw_input()
print "What's %s's age?" % name,
age = input()
print "What's %s's height?" % name,
height = input()
print "What's %s's weight?" % name,
weight = input()
print "What's the color of %s's eyes?" % name,
eyes = raw_input() 
print "What's the color of %s's teeth?" % name,
teeth = raw_input() 
print "What's the color of %s's hair?" % name,
hair = raw_input() 

type(name)  # the data type of name will be <type 'str'>
type(age)   # the data type of age will be <type 'int'>

print "Let's talk about %s" % name
print "He's %d years old." % age
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % (teeth)

print 'If I add %d, %d and %d I get %d.' % (age, height, weight, age + height + weight)
