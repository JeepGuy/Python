# Learn Python the hard Way Excersize 7
# Eliminate possible ascii encoding erros due to location
# -*- encoding: utf-8 -*-

# Prints the string in parentheses and quotes
print ("Mary had a little lamb.")

# Prints the string in parentheses and quotes
print ("Its fleece was white as %s." % 'snow')

# Prints the string in parentheses and quotes
print ("And everywhere that Mary went.")

# Prints the string in parentheses and quotes and duplcates (multiplies) the string by the number
print ("." * 10) # what did that do?

# Declares and assignes the variable end1 equal to the string value in parentheses 
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.   try removing it to see what happens

# print (end1 + end2 + end3 + end4 + end5 + end6,) ...wrong format...
# print (end7 + end8 + end9 + end10 + end11 + end12)


# Prints out the cancatenation (addition) of the variables using the plu sign 
# and the comma tells the program intrepreter NOT to break the line (eliminates the carriage return.. 
print (end1 + end2 + end3 + end4 + end5 + end6),
print (end7 + end8 + end9 + end10 + end11 + end12)
