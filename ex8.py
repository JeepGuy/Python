# Learn to Code the hard way (Python)
# Excersize 8
# -*- encoding: utf-8 -*-

# create a variable (object) to to hold formatting schema
formatter = "%r %r %r %r"

#print the formatter with the substitutioned numbers in the parentheses
print formatter % (1,2,3,4)
#print the formatter with the substitutioned strings in the parentheses
print formatter % ("one", "two", "three", "four")
#print the formatter with the substitutioned boolean values/variables in the parentheses
print formatter % (True, False, False, True)
#print the formatter with the substitutioned objects in the parentheses
print formatter % (formatter, formatter, formatter, formatter)
#print the formatter with the substitutioned strings in the parentheses on different lines
# after the opening and before the closing parentheses.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"but it didn't sing.",
	"So I said goodnight."
)
