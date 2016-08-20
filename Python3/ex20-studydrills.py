#!/usr/bin/env python3

# ex20: Functions and Files

# Import argv variables from the sys module
from sys import argv

# Assign the first and the second arguments to the two variables
script, input_file = argv

# Define a function called print_call to print the whole contents of a
# file, with one file object as formal parameter
def print_all(f):
    # print the file contents
    print(f.read())

# Define a function called rewind to make the file reader go back to
# the first byte of the file, with one file object as formal parameter
def rewind(f):
    # make the file reader go back to the first byte of the file
    f.seek(0)

# Define a function called print_a_line to print a line of the file,
# with a integer counter and a file object as formal parameters
def print_a_line(line_count, f):
    # Test whether two variables are carrying the same value
    print("line_count equal to current_line?:", (line_count == current_line))
    # print the number and the contents of a line
    print(line_count, f.readline())

# Open a file
current_file = open(input_file)

# Print "First let's print the whole file:"
print("First let's print the whole file:\n")

# call the print_all function to print the whole file
print_all(current_file)

# Print "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

# Call the rewind function to go back to the beginning of the file
rewind(current_file)

# Now print three lines from the top of the file

# Print "Let's print three lines:"
print("Let's print three lines:")

# Set current line to 1
current_line = 1
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)

# Set current line to 2 by adding 1
current_line += 1
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)

# Set current line to 3 by adding 1
current_line += 1
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)
