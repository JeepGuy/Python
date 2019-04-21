print("How many kilometers did you run today? ")
# one a way to do it.
# kms = float(input())
# kms/1.60934

# one a way to do it.
kms = input()
miles = float(kms)/1.60934
# round( the thing to round, the number of decimal points to round it to

print(f"That is equal to {round(miles,2)} miles.")

print('------ round to two decimals. \n')
miles = round(miles,2)

print(f"Your {kms} kilometer run is equal to {miles} miles. \n")

# Can do it on one line but then you have to add spaces after the input var.
kms0 = input("How many kilometers did you run today?")

print(kms0)


# How many kilometers did you run today?
# 5
# That is equal to 3.11 miles.
# ------ round to two decimals.
# Your 5 kilometer run is equal to 3.11 miles.
# How many kilometers did you run today?3
# 3
