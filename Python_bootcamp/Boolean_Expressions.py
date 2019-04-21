# conditionals   Boolean answer

# if <some condition is True>
#     if Boolean is true then do something and exit the conditional
#        if Boolean is equal to false then go on to the next Boolean test
# elif <some other condition> is True
#     if Boolean is true then do something-else and exit the conditional
#        if Boolean is equal to false then go on to the next Boolean test or the final else in this case./
# else:
#     do something completely different

# single equal = is assignment operator
# double equal == is comparison operator
name = None

print()

if name == "joe":
    print(name + " is the name.")
elif name == None:
    print("name == None")
    print("The name is " + "None") # Doesn't work if name is the data type is None
    print(type(name))
elif name == "ralph":
    print("The name is " + name)
else:
    print("The name was not Joe or Ralph")


name = 'joe'

print()

if name == "joe":
    print(name + " is the name.")   #This is a valid boolean test.

print()
print('---------------  Find odd number ---------------' )
print()

from random import randint
num = randint(1, 100)


if num % 2 != 0:
    print("odd")
    print(num)
else:
    print("even")
    print(num)

print()
print('---------------  Find odd number ---------------' )
print()

from random import randint
num = randint(1, 100)


if num % 2 == 0:
    print("even")
    print(num)
else:
    print("odd")
    print(num)
