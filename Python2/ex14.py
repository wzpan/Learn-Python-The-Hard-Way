#!/bin/python2
# -*- coding: utf-8 -*-

# ex14: Prompting and Passing

from sys import argv

# Add another argument and use it in your script
script, user_name, city = argv
# prompt = '> '
# Change the prompt variable to something else
prompt = 'Please type the answer: '

print "Hi %s from %s, I'm the %s script." % (user_name, city, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "What's the whether like today in %s?" % city
weather = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
The weather in your city is %s. 
But I can't feel it because I'm a robot.
And you have a %r computer.  Nice.
""" % (likes, weather, computer)
