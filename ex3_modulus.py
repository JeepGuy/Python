# Learn Python the Hard way Excersize 3 Modulus clarificaiton
# Jim Brent
# Review 17 July 2016
# PEDMAS
# 

# + plus   Addition
# - minus  Subtraction
# / slash  Division
# * asterisk Mulitlication
# % percent  Modulus
# < less-than 
# > greater-than
# <= less-than-equal
# >= greater-than-equal
#
# PEDMAS Parenthesis Exponent Division Multiplication Addition Subtraction
# Where does Modulus go?
# Before or after Division? fter division so it should be PEDMoMAS

# Roosters
# 
#PEDMoMAS Parenthesis Exponent Division MOdulus Multiplication Addition Subtraction
#
print "Roosters", 100 - 25 * 3 % 4
#
# 25 * 3 = 75
# Modulus:  75 / 4 = 18.75 so the modulus is the remainder of 18 * 4 (= 72) therefore 75 - 72 = 3, 
# 100 - 3 = 95
 
################################################
# COUNT THE EGGS Line: Order of Operations practice line
print "Now I will count the eggs:"
print "\n print 3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6 \n "
print 3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6

print " \n "

print "Is it true that 31 % 2 - 7 / 2 = -2 ?"

print "\n   Yes because Division occurs before Modulus"

print " \n  Therefore Order of Operations is: PEDMoMAS \n Parenthesis Exponent Division MOdulus Multiplication Addition Subtraction"

print "\n ", 31 % 2 - 7 / 2

print "What is 7 / 2?  \n ", 7 / 2
print "What is 31 % 2 ?  \n ", 31 % 2

print " What is 1 - 3 ?  \n " , 1 - 3

print "\n"


