__author__='jcbrent'

print('')
print(' Data Types Int and Float')
print('')

num_int = 3

print(type(num_int))  # Returns data type.

num_float = 3.14

print(type(num_int))  # Returns data type.


# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


print('')

decimal_example = 12.5437
print(decimal_example)

int_convert = int(decimal_example)
print(int_convert)

my_list = (1,2,3)
print(my_list)
print('That was a list')

print('This is a string')
my_list_as_a_string = str(my_list)
print(my_list_as_a_string)

print('')

num = 12
print(num)

print(type(num))
print('')

print('Change to float: num = float(num)')
num = float(num)
print(num)
print(type(num))
print('')


print('')
print('Division changes ints to floats implicitly.')
print('1/3')
print(1/3)

print('')
print('Changing a float to an int just chops off the decimals.')
print('int(99.999')
print(int(99.999))

print('')
print(' ===================================================== ')
print('')
# use modulus to find even or add numbers ) is even 1 is odd

print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)


print('')
print(' ===================================================== ')
print('')
print('Order of operations:  PEDMoMAS')
print('')
print(' ===================================================== ')
print('')

print('')
print(' --------------------------------------------------- ')
print('')
print('Incrementing numbers')

num = 1

num = num + 1 # shortcut is:
num +=1

print(num)

number = 2

number = number * 2
print(number)

number_increment = 3
number_increment *= 5

print(number_increment)

print('')
print(' --------------------------------------------------- ')
print('')
print('Absolute Numbers')
print("print(abs(-3))")
print(abs(-3))

print('')
print(' --------------------------------------------------- ')
print('')
print('Rounding')
print("print(round(3.14159))")
print(round(3.14159))

print('')
print('Rounding to a specific digit')
print("print(round(3.14159, 3))")
print(round(3.14159, 2))

print('')
print(' --------------------------------------------------- ')
print('')
print('Comparison operators')
print(' single equal sign is assignment, double is comparison')
# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal: 3 <= 2

num_1 = 3
num_2 = 2

print("print(num_1 == num_2)")
print(num_1 == num_2)

print('')
print(' --------------------------------------------------- ')
print('')
print('Casting strings to intergers')
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)



print('')
print(' ===================================================== ')
print('')


print('')# Example
print(' Example of an input, datatype conversion, and round function/method.')
print('')
print("How many kilometers did you run today?")
# one a way to do it.
# kms = float(input())
# kms/1.60934

# one a way to do it.
kms = input()
miles = float(kms)/1.60934
# round( the thing to round, the number of decimal points to round it to

print(f"That is equal to {round(miles,2)} miles.")

print('------ round on two lines.')
miles = round(miles,2)

print(f"Your {kms} kilometer run is equal to {miles} miles.")