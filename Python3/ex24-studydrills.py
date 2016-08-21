#!/usr/bin/env python3

# ex24: More Practice

print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------------")
print(poem)
print("--------------------")


five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formala(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
beans, jars, crates = secret_formala(start_point)

print("With a starting point of: %d" % start_point)
# use the tuple as the parameters for the formatter
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
# call the function and use its return values as the parameters for the formatter
print("We'd have %d beans, %d jars, and %d crates." % secret_formala(start_point))
