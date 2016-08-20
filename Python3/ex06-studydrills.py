#!/usr/bin/env python3

# ex6: String and Text

# Assign the string with 10 replacing the formatting character to variable 'x'
x = "There are %d types of people." % 10

# Assign the string with "binary" to variable 'binary'
binary = "binary"

# Assign the string with "don't" to variable 'do_not'
do_not = "don't"

# Assign the string with 'binary' and 'do_not' replacing the
# formatting character to variable 'y'
y = "Those who know %s and those who %s." % (binary, do_not)  # Two strings inside of a string

# Print "There are 10 types of people."
print(x)

# Print "Those who know binary and those who don't."
print(y)

# Print "I said 'There are 10 types of people.'"
print("I said %r." % x)  # One string inside of a string

# Print "I also said: 'Those who know binary and those who don't.'."
print("I also said: '%s'." % y)  # One string inside of a string

# Assign boolean False to variable 'hilarious'
hilarious = False

# Assign the string with an unevaluated formatting character to 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny?! %r" 

# Print "Isn't that joke so funny?! False"
print(joke_evaluation % hilarious)  # One string inside of a string

# Assign string to 'w'
w = "This is the left side of..."

# Assign string to 'e'
e = "a string with a right side."

# Print "This is the left side of...a string with a right side."
print(w + e)  # Concatenate two strings with + operator
