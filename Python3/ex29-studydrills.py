#!/usr/bin/env python3

# ex29: What If

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

dogs += 5

if (dogs < cats) and (people < cats):
    print("Cats are more than people and dogs. People are scared by cats!")    

if (dogs < cats) and not (people < cats):
    print("Cats are more than dogs. Mice are living a hard life!")
    
if (dogs == cats) or (cats < 10):
    print("Cats are fighting against dogs! Mice are happy!")

if cat != 0: 
    print("Cats are still exist. Mice cannot be too crazy.")  