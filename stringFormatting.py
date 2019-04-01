__author__='jcbrent'

# Str function
print(' String functions')
print(' ------------------------------------------------------------------------------ ')

message = 'Hello everyone'
print(message)

print(len(message))

print(' Slicing')
print(message[10])
# Print a range of chars
print(message[0:5])
#Starts at 0 : thru to char 5

print(message[7:]) # will print from the 7th char to the end.
print(message[:7]) # will print from the beggining to the 7th char.

# a method is a function that belongs to an object.

print(message.lower())
print(message.upper())

# counting
print(message.count('l'))
print(message.count('Hello'))

# Find the location of an item
print(message.find('Hello'))
print(message.find('y'))
print(message.find('universe'))   # will return -1  because it doesn't exist in the var - message

print('')

# replacements.
message.replace('Everyone', 'anyone')
print(message)
# must set a new var to replace the text
new_message = message.replace('everyone', 'anyone')

print(new_message)
# or you set the old var equal to the modified var
message = message.replace('everyone', 'anyone')
print(message)

print('')

print('Concatenating Strings')

greeting = 'Hello'
name = 'Joe'

concat_message = greeting + ' ' + name + '. Welcome.'

print(concat_message)
print('')

message_f_string = f'{greeting}, {name}. Welcome!'
print(message_f_string)
print('')


new_f_string_message = f'{greeting}, {name.upper()}. Welcome!'
print(new_f_string_message)
print('')

# method list
print(dir(name))
print('')

# get help
# print(help(str)) # Too verbose.
print('')

# get help on a specific function/method
print(help(str.lower)) # Too verbose.
print('')

print('')

# print('Hello World')
# print (1 + 2)
# print (7 * 6)
# print ('The End')
# print ("Pythons string are easy to use")
# print ('We can even include "quotes" in string')
# print ("hello" + " world")
#
# greeting = "Hello"
# name = "Bruce"
# print (greeting + name)
# # comments
# print(greeting + ' ' + name)

# greeting = ("Hello")
# name = input("Please enter your name ")
# print(greeting + ' ' + name)

# splitString = "This string has been \nsplit over\n several lines"
# print (splitString)
#
# tabbedString = "1\t2\t\3\t4\t5\t"
# print (tabbedString)

print ('the pet shop owner said "No, no \'e\'s uh... he\'s resting"') #preferred method
print ("the pet shop owner said \"No, no 'e's uh... he\sting\"")

anotherSplitString = """ The pet shop owner 
split
the string 
over several lines."""
print (anotherSplitString)

print (''' The pet shop owner said  "No, no, 'e's uh, ... he's resting"''')

print('')



age = 100
# NOT Correct ---   print("My age is " + age + "years")
# must use str method - a built in method
print("My age is " + str(age) + " years.")

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



# Formatting Strings
print(' String formatting: F method.  ~ Python 3.6 method.')
print(' ------------------------------------------------------------------------------ ')
print('')
print('Note:  % operator now deprecated = pre 3.5 method')
print('')
print('')

# F Strings  Python 3.6          New method.........
# Take the value in the {} and turns it into a string and substitutes it into the {}
x = 10
formatted = f"I've told you {x} times already!"

print(formatted)

print(f"I've told you {x + 1 } times already!")

print('')
print(' ------------------------------------------------------------------------------ ')
print(' String formatting: Format method.  ~ Python 3.5 and before method.')
print(' ------------------------------------------------------------------------------ ')

formatted_old = "I've told you {} times already!".format(12)
print(formatted_old)

# Example
first = "Jim"
last = "B."

formatted = ("{} {}".format(first, last))

print(formatted)


formatted = ("first name: {}, last name: {}".format(first, last))
print(formatted)


print(' ------------------------------------------------------------------------------ ')

print(' ')
print('Replacement fields python3.5')
print(' ---------------------')
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "January", "March", "May", "July", "August", "October", "December"))
print(' ')
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28,30,31))

print(' ')
print('Python 2 deprecated formatting operator')
print(' ---------------------')

print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

print(' ')

for i in range(1,12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is approximately %12f" % ( 22 / 7 ))

print(' ')

print("Pi is approximately %12.50f" % ( 22 / 7 ))
print("50 places = precision")

print('')
print('Replacement syntax')

print("Python3.5 replacement fields formatting of above")
print(' ---------------------')
#Right formatting
for i in range(1,12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

#Left formatting
for i in range(1,12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print(' ---------------------')
print("Pi is approximately {0:12.50f}".format( 22 / 7 ))
print("50 places = precision")

print(' ')
print('For loop using no params in array, just in order')
for i in range(1,12):
    print("No. {} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))

#

