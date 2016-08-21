#!/usr/bin/env python3

# ex30: Else and If

# assign 30 to variable people
people = 30
# assign 40 to variable cars
cars = 40
# assign 15 to variable buses
buses = 15

# if cars are more than people
if cars > people:
    # print "We should take the cars."
    print("We should take the cars.")
# if cars are less than people
elif cars < people:
    # print "We should not take the cars"
    print("We should not take the cars")
# if cars are equal to people
else:
    print("We can't decide.")

# if buses are more than cars    
if buses > cars:
    # print "That's too many buses."
    print("That's too many buses.")
# if buses are less than cars    
elif buses < cars:
    # print "Maybe we could take the buses."
    print("Maybe we could take the buses.")
# if buses are equal to cars    
else:
    # print "We still can't decide."
    print("We still can't decide.")

# if people are more than buses
if people > buses:
    # print "Alright, let's just take the buses."
    print("Alright, let's just take the buses.")
# if people are less than buses
else:
    # print "Fine, let's stay home then."
    print("Fine, let's stay home then.")

# if people are more than cars but less than buses
if people > cars and people < buses:
    # print "There are many Busses but few cars."
    print("There are many Busses but few cars.")
# if people are less than cars but more than buses
elif people < cars and people > buses:
    # print "There are many cars but few busses."
    print("There are many cars but few busses.")
# if people are more than cars and buses
elif people > cars and people > buses:
    # print "There are few busses and cars."
    print("There are few busses and cars.")
# if people are less than cars and buses    
else:
    # print "There are many busses and cars."
    print("There are many busses and cars.")