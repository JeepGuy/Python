print (' ')

string = "he's "
string1 = "probably "
print(string + string1)
print("he's " "probably " "pinning")    # No reason to do this but it works
print("he's probably pinning")          # Yields the same as above
print (' ')

print('----- Multiplying strings---------')

print("hello " * 5)
print("hello  * 5+4 won't print because  \"hello\"  * 5 evaluatees to a string and the  +4 is an interger")
print("hello  * (5 + 4) will work")
print("hello " * (5 + 4))  # gives is nine copies.
print('')

print("hello "  * 5 + "+ 4" )    # appends the number 4 to the output.

print (' ')




# More complete explanation of below in substring py file...
print('----- Operator to check for substrings   The IN operator  ---------')
today = "friday"
print("day" in today)
print("fri" in today)
print("parrot" in "fjord")
print("thur" in today)
print (' ')

print (' ')
