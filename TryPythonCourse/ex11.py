# Learn to Code the Hard Way (Python)
# Excersize 11 
# Jim Brent 10 Jun 2016
#
# The following is a code hack to eliminate ASCii encoding error if in a foreign country
# -*- coding: utf-8 -*- 

print "How old are you?",
age = raw_input()

print "How tall are you ?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)

print " -------------------------- \n"

print " raw_input() is the prompt argument and is written to standaoutput without a trailing newline."

print " The function reads a line from input, converts it to a string (stripping the training newline),\n  and returns the value that was input"

print " When EOF is read, EOFError is raised. \r  The exception EOF occurs if the input() or raw_input() builtin functions hits End-Of-File without reading any data."


print " -------------------------- \n"

print " this is a join" # another comment


 print " -------------------------- \n"


