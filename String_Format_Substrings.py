print (' ')
print(' ----------- Strings - and substrings--------------')

print('String are one of Pythons sequence data types')

print (' ')

parrot = "Norwegian Blue"

print(parrot)
print(parrot[0])   # Prints the first character  N
print(parrot[3])
print(parrot[-1])  # # Prints the last character  e - it stated at position [0] which is N and went backwards


print (' ')
print('Slice---------')
print(' Format  #:#:#   = Starts at the FirstChar, [range to] (but not including) index # (e.g. 6 below), skip chars in steps  ')
print(parrot[0:6])         # Prints from the first character  to the six character (up to but not including the seventh character

print()
print ('If first number is omitted it starts at the beginning of the string, if the second is omitted it runs to the end of the string')

print(parrot[:6])          # Prints the same as above
print(parrot[6:])          # Prints from the seventh character (position 6 in the array - which starts at zero) to end of the string
print(parrot[-4:-2])       # Prints from the first character  to the seventh character

print(' Printing in steps   skipping letters in between index positions ')

print(parrot[0:6:2])
print(parrot[0:6:3])

print (' ')

number = ("9,223,272,036,854,775,807")
print(number[1::4]) # prints the commas only
print (' ')
numbers =("1, 2, 3, 4, 5, 6, 7, 8, 9")
print(numbers[0::3])   #Extracts the spaces and numbers 

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