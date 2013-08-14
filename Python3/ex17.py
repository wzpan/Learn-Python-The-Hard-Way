#!/bin/python3

# ex17: More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print("Does the output file exists? %r"  % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()

