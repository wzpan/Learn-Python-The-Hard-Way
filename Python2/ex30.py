#!/bin/python2
# -*- coding: utf-8 -*-

# ex30: Else and If

people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

if people > cars and people < buses:
    print "There are many Busses but few cars."
elif people < cars and people > buses:
    print "There are many cars but few busses."
elif people > cars and people > buses:
    print "There are few busses and cars."
else:
    print "There are many busses and cars."
