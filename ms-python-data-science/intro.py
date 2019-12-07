# print('Hello, World')

# List => array of items - mutables

import math
square = [1, 4, 5, 7]

# Tuples => array of items - inmutables
t = (1, 4, 5)

# Dictionaries => is a collection whoch is unordered, changeable and indexed
capitals = {'France': ('Paris', 2140000)}


# List comprehensions

numbers = [x for x in range(1, 11)]
print(numbers)

odd_squares = [x*x for x in range(1, 11) if x % 2 != 0]
print(odd_squares)


# importing modules
# import math
# math.factorial
# or
# from math import factorial
factorial = math.factorial(5)
# factorial = factorial(5)
# print(factorial)

num = range(3)
print(num)

sq = [1, 2, 'ss']
print(sq)

# Creating TUples from Lists
l = ['baked', 'beans', 'spam']  # List
l = tuple(l)
print(l)  # Tuple

find = 'spam' in l
find2 = 'spam' not in l
print(find)
print(find2)
