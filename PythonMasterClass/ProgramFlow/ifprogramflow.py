__author__ = 'dev'

# name = input("Pleae enter your name: ")
# # STRING style: age = input("How old are you, {0}? ".format(name))
# # To convert string to an int is the int function
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please go to the voting booth")
# else:
#     print("Please come back in {0} years".format(18 - age))
#     print("Thank you")

print("Please guess a number between 1 - 10.")
guess = int(input())

# This has repetitive code so it is not good code:
# if guess < 5:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == 5:
#         print("Correct")
#     else:
#         print("sorry you have guessed incorrectly")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Correct")
#     else:
#         print("You have not guessed correctly")
# else:
#     print("You got it first time")

# Refactor above.

if guess != 5:
    if guess <5:
        print("Please guess higher.")
    else:
        print("Please guess lower")

    guess = int(input())
    if guess == 5:
        print("Correct")
    else:
        print("You have not guessed correctly.")
else:
    print("You got it first time")


