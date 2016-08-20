#!/usr/bin/env python3

# ex31: Making Decisions

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots you ")

elif door == "3":
    print("You are asked to select one pill from two and take it. One is red, and the other is blue.")
    print("1. take the red one.")
    print("2. take the blue one.")

    pill = input("> ")

    if pill == "1":
        print("You wake up and found this is just a ridiculous dream. Good job!")
    elif pill == "2":
        print("It's poisonous and you died.")
    else:
        print("The man got mad and killed you.")

else:
    print("You wake up and found this is just a ridiculous dream.")
    print("However you feel a great pity haven't entered any room and found out what it will happens!")