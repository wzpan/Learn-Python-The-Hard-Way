#!/usr/bin/env python3

# ex37: Symbol Review

# and, or, not, if, elif, else

print("#1##############################")

if True and False:
    print("#1 can't be printed")

if False and False:
    print("#2 can't be printed")

if True and True:
    print("#3 can be printed!")

if False or True:
    print("#4 can be printed!")

if True or False:
    print("#5 can be printed!")

if True or No_Matter_What:
    print("#6 can be printed!")

if not(False and No_Matter_What):
    print("#7 can be printed!")

rainy = True
sunny = False
if rainy:
    print("It's rainny today!")
elif sunny:
    print("It's sunny today!")
else:
    print("It's neither rainny nor sunny today!")


# del, try, except, as

print("#2##############################")

x = 10
print(x)

del x
try:
    print(x)
except NameError as er:
    print(er)

    
# from, import

print("#3##############################")

from sys import argv
script = argv
print("The script name is %s " % script)

# for, in
for i in range(0, 10):
    print(i, end=' ')

# assert
try:
    assert True, "\nA True!"
    assert False, "\nA false!"
except AssertionError as er:
    print(er)

# global, def
print("#4##############################")
x = 5

def addone():
    # annouce that x is the global x
    global x
    x += 1

addone()
print("x is %d", x)

# finally

print("#4##############################")

import time
try:
    f = open('sample.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        print(line) 
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    f.close()
    print('(Cleaning up: Closed the file)')
    
# with

print("#5##############################")

with open("sample.txt") as f:
    print(f.read())

# pass, class

print("#6##############################")

class NoneClass:
    ''' Define an empty class. '''
    pass

empty = NoneClass()
print(empty)

class Droid:
    ''' Define a robot with a name. '''
    def __init__(self, name):
        self.name = name
        print("Robot %s initialized." % self.name)
    def __del__(self):
        print("Robot %s destroyed." % self.name)
    def sayHi(self):
        print("Hi, I'm %s." % self.name)

r2d2 = Droid('R2D2')
r2d2.sayHi()
del r2d2

# exec

print("#7##############################")

print("Here I will use exec function to calculate 5 + 2")
exec("print('5 + 2 =', 5 + 2)")

# while, break

print("#8##############################")

while True:
    try:
        num = int(input("Let's guess an integer:"))
        if num > 10:
            print("too big!")
        elif num < 10:
            print("too small!")
        else:
            print("Congrats! You will!")
            break
    except ValueError:
        print("Please insert a value!")

# raise

print("#9##############################")

class ShortInputException(Exception):
    ''' A user-defined exception class. '''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter something long enough --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usal here
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print('ShortInputException: The input was {0} long, expected at least {1}'\
          .format(ex.length, ex.atleast))    
else:
    print('No exception was raised.')

# yield

print("#10##############################")

print("Now we counter from 1 to 99: ")            

def make_counter(max):
    x = 1
    while x < max:
        yield x
        x = x + 1

for i in make_counter(100):
    print(i, end=' ')

print("\n\nNow we calculate fibonacci series: ")          
    
def fib(max):
    ''' A fibonacci secries generator.

    Calculates fibonacci numbers from 0 to max.
     '''
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

for num in fib(100):
    print(num, end=' ')

# lambda

print("\n#11##############################")

def makeDouble():
    ''' double given value '''
    return lambda x:x * 2

adder = makeDouble()
num_list = [5, 10, 15, 'hello']
print('\nNow we multiples each elements in num_list with 2:')
for num in num_list:
    print(adder(num))