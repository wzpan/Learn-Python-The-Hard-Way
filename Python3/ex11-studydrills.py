#!/usr/bin/env python3

# ex11: Asking Questions

# raw_input() was renamed to input() in Python v3.x,
# and the old input() is gone, but you can emulate it with eval(input())

print("How old are you?", end=" ")
age = input()  
print("How tall are you?", end=" ")
height = input()
print("How much do you weight", end=" ")
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

print("Enter a integer: ", end=" ")
num = int(eval(input()))                        # won't work with int(raw_input)), with eval(input()) it would work
print("The number you've input is: %d" % num)
print("Enter a name: ", end=" ")
name = input()
print("What's %s's age?" % name, end=" ")
age = eval(input())
print("What's %s's height?" % name, end=" ")
height = eval(input())
print("What's %s's weight?" % name, end=" ")
weight = eval(input())
print("What's the color of %s's eyes?" % name, end=" ")
eyes = input()
print("What's the color of %s's teeth?" % name, end=" ")
teeth = input()
print("What's the color of %s's hair?" % name, end=" ")
hair = input()

type(name)  # the data type of name will be <class 'str'>
type(age)   # the data type of age will be <class 'int'>

print("Let's talk about %s" % name)
print("He's %d years old." % age)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % (teeth))

print('If I add %d, %d and %d I get %d.' % (age, height, weight, age + height + weight))