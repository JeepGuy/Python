# Excersize 4 learn_python_the_hard_way book
#
# Variables
#
# Set variables

cars = 100
space_in_a_car = 4.0 #Remove 4.0 floating point number.
drivers = 30
passengers = 91.0    # adding the floating point number will allow the division to retain the decimals.
cars_driven = drivers
cars_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# Print statements

print "There are" , cars, "cars available."
print "There are only ", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

