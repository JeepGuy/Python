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

