#!/bin/python2
# -*- coding: utf-8 -*-

# ex10: What Was That?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
test = "I will insert a \newline haha."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Assign string value for each variable
intro = "I'll print a week"
mon = "Mon"
tue = "Tue"
wed = "Wed"
thu = "Thu"
fri = "Fri"
sat = "Sat"
sun = "Sun"

print "%s\n%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (intro, mon, tue, wed, thu, fri, sat, sun)

print "%r" % intro
print "%r" % "She said \"I'll print a week\""

print "%s" % intro
print "%s" % "She said \"I'll print a week\""
