#!/bin/python2
# -*- coding: utf-8 -*-

# ex33: While Loops

def createNumbers(max):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

numbers = createNumbers(10)


print "The numbers: "

for num in numbers:
    print num
