#!/usr/bin/env python3

# ex17: More Files

from sys import argv

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())