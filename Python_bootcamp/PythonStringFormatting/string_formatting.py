# Formatting Strings

# F Strings  Python 3.6
# Take the value in the {} and turns it into a string and substitutes it into the {}
x = 10
formatted = f"I've told you {x} times already!"

print(formatted)

print(f"I've told you {x + 1 } times already!")

# old format = format method.
formatted_old = "I've told you {} times already!".format(12)
print(formatted_old)

# pre 3.5 method = % operator now deprecated.

# Excersize
first = "Jim"
last = "Brent"

formatted = ("{} {}".format(first, last))

print(formatted)


formatted = ("first name: {}, last name: {}".format(first, last))
print(formatted)


