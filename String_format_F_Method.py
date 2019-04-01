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
last = "B."

formatted = ("{} {}".format(first, last))

print(formatted)


formatted = ("first name: {}, last name: {}".format(first, last))
print(formatted)


# String Formatting with the f function is implicit interpolation

# implicitly do by using the name of the function to convert

decimal_example = 12.5437
print(decimal_example)

int_convert = int(decimal_example)
print(int_convert)

my_list = (1,2,3)
print(my_list)
print('That was a list')

print('This is a string')
my_list_as_a_string = str(my_list)
print(my_list_as_a_string)

print('')

num = 12
print(num)

print(type(num))
print('')

print('Change to float: num = float(num)')
num = float(num)
print(num)
print(type(num))
print('')


print('')
print('Division changes ints to floats implicitly.')
print('1/3')
print(1/3)

print('')
print('Changing a float to an int just chops off the decimals.')
print('int(99.999')
print(int(99.999))

print('')
print('String function = str')
num = 12
print(num)

print(type(num))
print(' str(num)')
print(str(num))

print(type(num))
print(str(num) + ' is now a string')