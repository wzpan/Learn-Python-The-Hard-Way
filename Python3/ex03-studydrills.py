#!/usr/bin/env python3

# ex3: Numbers and Math

# Print "I will now count my chickens:"
print("I will now count my chickens:")

# Print the number of hens
print("Hens", 25 + 30 / 6)
# Print the number of roosters
print("Roosters, 100 -25 * 3 % 4")

# Print "Now I will count the eggs:"
print("Now I will count the eggs:")

# number of eggs, Notice that '/' operator returns float value in Python3
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Print "Is it true that 3 + 2 < 5 - 7?"
print("Is it true that 3 + 2 < 5 - 7?")

# Print whether 3+2 is smaller than 5-7(True or False)
print(3 + 2 < 5 - 7)

# Calculate 3+2 and print the result
print("What is 3 + 2?", 3 + 2)
# Calculate 5-7 and print the result
print("What is 5 - 7?", 5 - 7)

# Print "Oh, that's why it's False."
print("Oh, that's why it's False.")

# Print "Oh, that's why it's False."
print("How about some more.")

# Print whether 5 is greater than -2(True or False)
print("Is it greater?", 5 > -2)
# Print whether 5 is greater than or equal to -2?(True or False)
print("Is it greater or equal?", 5 >= -2)
# Print whether 5 is less than or equal to -2 (True or False)
print("Is it less or equal?", 5 <= -2)

# Find something you need to calculate and write a new .py file that
# does it.

# integer
print(50 * 2)
print(1/500)
print(4 * 3 - 1)
print(3.14 * 2 * 200)
print(1.0/20)

# The following expressions are more complicated calculations.
# Ignore them if you haven't learned anything about each type.

# decimal: more accurate than float
import decimal
print(decimal.Decimal(9876) + decimal.Decimal("54321.012345678987654321"))

# fraction
import fractions
print(fractions.Fraction(1, 3))
print(fractions.Fraction(4, 6))
print(3 * fractions.Fraction(1, 3))

# complex
print(3-4j)
print(3-4J)
print(complex(3,-4))
print(3 + 1J * 3j)