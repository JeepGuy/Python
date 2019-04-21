# Math: Order of Operations

print('Math: Order of Operations \n')
print()

print(' See URL: ')
print('''
https://docs.python.org/3/reference/expressions.html#operator-precedence 
      ''')
print()

print('P E DM AS \n')
print("e.g.  Modulus and Floor Division have the same precedence as Division and are executed left to right See graph on website above\n")

x = 8 * 12 % 5

y = 8 * (12 % 5)

z = (8 * 12) % 5

print(x, y, z)
# Yields:   1 16 1

print()

a = 8 - 12 + 5
b = 8 + 12 - 5

print(a)
print(b)

print()
c = 8 + 12 * 5
c1 = 12 * 5
c2 = 8 + c1
d = (8 + 12) * 5

print(c, c1, c2, d)

print()
e = 2 + 3 * 5 ** 2


print(e)
