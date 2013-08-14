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
