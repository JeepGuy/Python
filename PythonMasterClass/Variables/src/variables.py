_author_ = 'dev'
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

# print ('the pet shop owner said "No, no \'e\'s uh... he\'s resting"') #preferred method
# print ("the pet shop owner said \"No, no 'e's uh... he\sting\"")
#
# anotherSplitString = """ The pet shop owner
# split
# the string
# over several lines."""
# print (anotherSplitString)
#
# print (''' The pet shop owner said  "No, no, 'e's uh, ... he's resting"''')

# ---------
greeting = "Bruce"
# Vars must start with a letter or an underscore
_myName ="Tim"
Tim45 = "Good"
Tim_was_57 = "Hello"
Greeting = "Vars: Greeting is different than lower case greeting"

print (' ')
print (Tim_was_57 + ' ' + greeting)
print (' ')

age = 24
print (age)
print (' ')

#   print ( greeting + age)
#   print ('Cntrl F1 to get more info in the code view')

print ('greeting + age  will give us an error:  TypeError: must be str, not int')
print (''' Because age is an interger and Python3 
     does not covert an int to a string implicitly.''')
print (' ')

print (''' Data types are classified as:
      Numerics
      Sequences,
      mappings,
      Files,
      Classes,
      Instances,
      Exceptions
''')

print (' ')

print (' ------------- integers -------------')
print (' ')

a = 12
long = 240
float = 0.000001

b = 3

print(a + b)
print(a - b)
print(a * b)

print(a * b)
print(a / b)  # in Python returns as a float unless you use floor division
print(a // b) # Florr division returns a whole number
print(a % b)

print (' ')

for i in range(1, a//b):  #for i in range(1, a/b): gives an error because it returns a float
    print(i)

print (' ')

print(a + b / 3 -4 * 12)
print (' ')

print(8 / 2 * 3)
print(' ')

print(8 *3 /2)
print(' ')

print ((((a + b ) / 3) -4) *12)

print (' ')

print(' ----- user vars to hold intermediate values ---------------')
print (' ')

c = a + b
d = (c / 3)
e = (d - 4)

print(e * 12)

print (' ')
print(' ----------- Strings ---------------')

print('String are one of Pythons sequence data types')

print (' ')

parrot = "Norwegian Blue"

print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])


print (' ')
print('Slice---------')
print(' Format  #:#:#   = Starts at the FirstChar, [range to] (but not including) index #, skipt chars in steps  ')
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])

print ('If first number it starts at the beginning of the string, if the second is omitted it runs to the end of the string')

print(parrot[0:6:2])
print(parrot[0:6:3])

print (' ')

number = ("9,223,272,036,854,775,807")
print(number[1::4])
print (' ')
numbers =("1,2,3,4,5,6,7,8,9")
print(numbers[0::3])

print (' ')

string = "he's "
string1 = "probably "
print(string + string1)
print("he's " "probably " "pinning")
print("he's      probably      pinning")
print (' ')

print('----- Multiplying strings---------')

print("hello " * 5)
print("hello  * 5+4 won't print because  hell * 5 evaluatees to a string and the  +4 is an interger")
print("hello  * (5 + 4) will work")
print("hello " * (5+4))
print('"hello "  * 5 + "+ 4") will work')

print("hello "  * 5 + "+ 4" )

print (' ')

print('----- Operator to check for substrings   The IN operator  ---------')
today = "friday"
print("day" in today)
print("fri" in today)
print("parrot" in "fjord")
print("thur" in today)
print (' ')

print (' ')

print (' ')











