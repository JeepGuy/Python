__author__='dev'
# Str function
age = 24
# WILL CRASH  print("My age is " + age + "years")
# must use str method - a built in method
print("My age is " + str(age) + " years.")

print(' ')
print('Replacement fields python3')
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

print("Python3 replacement fields formatting of above")
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
Print('For loop using no params in array, just in order')
for i in range(1,12):
    print("No. {} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))

#