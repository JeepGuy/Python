# Learn Python the Hard Way excersize 6
# Eliminate possible ascii encoding errors due to location
# -*- coding: utf-8 -*-
#

# Set the variable x equal to a string with a format string in it
x = "There %d types of people." %10
# Set a string variable eual to a value
binary = "binary"
# Set a string variable eual to a value
do_not = "don't"
# Set the variable y equal to a string with a format string in it
y = "Those who know %s and those who %s." % (binary, do_not)

# add a carriage return for better formatting
print (".") # add a carriage return for better formatting
print (".")

# perform the print operation/method of the variable x
print (x)
# perform the print operation/method of the variable y
print (y)

# add a carriage return for better formatting
print (".")

# print the formatted string with the debug variable % "r"
print ("I said %r." % x)
# print the formatted string with the string variable  %s with a value of y (set above)
print ("I also said: '%s'." % y)


# add a carriage return for better formatting
print (".")

# Set a boolean vairable equal to False (or True) remember capital letters are used for Booleans.
hilarious = False
# Set a string variable equal to a formatted string.
joke_evaluation = "Isn't that joke so funny?! %r"

# print the formatted string variable and give the value of the debug variable.
print (joke_evaluation % hilarious)


# add a carriage return for better formatting
print (".") # add a carriage return for better formatting
print (".")

# set the variable w equal to a simple string.
w = "This is the left side of ..."
# set the variable e equal to a string.
e = "a string with a right side."

# print the two string vaiables by concatenating (adding) them with the plu sign
print (w + e)

# add a carriage return for better formatting
print (".") 
