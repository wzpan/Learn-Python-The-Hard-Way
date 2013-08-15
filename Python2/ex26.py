#!/bin/python2
# -*- coding: utf-8 -*-

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# bug: def print_first_word(words)
def print_first_word(words):
    """Prints the first word after popping it off."""
    # bug: word = words.poop(0)
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    # bug: word = words.pop(-1
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

# warning: it's not five
five = 10 - 2 + 3 - 5
print "This should be five: %s" % five


def secret_formula(started):
    jelly_beans = started * 500
    # bug: jars = jelly_beans \ 1000
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# bug: beans, jars, crates == secret_formula(start-point)
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# bug: print "We'd have %d beans, %d jars, and %d crabapples." %
# secret_formula(start_pont
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)


# bug: sentence = "All god\tthings come to those who weight."
sentence = "All good things come to those who weight."

# bug: words = ex25.break_words(sentence)
words = break_words(sentence)
# bug: sorted_words = ex25.sort_words(words)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
# bug: .print_first_word(sorted_words)
print_first_word(sorted_words)
print_last_word(sorted_words)
# bug: sorted_words = ex25.sort_sentence(sentence)
sorted_words = sort_sentence(sentence)
# bug: prin sorted_words
print sorted_words
# bug: print_irst_and_last(sentence)
print_first_and_last(sentence)

# bug:   print_first_a_last_sorted(senence)
print_first_and_last_sorted(sentence)
