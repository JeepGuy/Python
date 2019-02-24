#
# Excersize 5.py Learn python the hard way.#
# Eliminate possible  ascii encoding errors based on location - set to  UTF-8.
# -*- coding: utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s."  % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight)

# Now do it with the vaiable names changed to eliminate the underscore

print (" -----------------------------------------")
print (" ")
print ("This version eliminates the _ in the variable name.")
print (" -----------------------------------------")
print (" ")

myname = 'Zed A. Shaw'
myage = 35 # not a lie
myheight = 74 # inches
myweight = 180 # lbs
myeyes = 'Blue'
myteeth = 'White'
myhair = 'Brown'

print "Let's talk about %s."  % myname
print "He's %d inches tall." % myheight
print "He's %d pounds heavy." % myweight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (myeyes, myhair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( myage, myheight, myweight, myage + myheight + myweight)


print (" -----------------------------------------")
print (" ")
print ("This version adds parentheses around the string.")
print (" -----------------------------------------")
print (" ")

print ("The name of the author is %s" %my_name)
