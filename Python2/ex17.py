#!/bin/python2
# -*- coding: utf-8 -*-

# ex17: More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())
