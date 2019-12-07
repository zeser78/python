
# NumPy => is the fundamental package for scientific computing with Python
import numpy as np

demo = np.random.seed(4)
print(demo)

a = np.array([1, 2, 3])
b = np.array((3, 4, 5))

print(a + b)

myList = list(range(10))
print(myList)

ran = np.array([range(i, i + 3) for i in [2, 4, 8]])
ran = np.array([range(1, 4)])
print(ran)

a1 = np.random.randint(10, size=(3, 4, 5))
print(a1)

# one-dimensional slices
np_arange = np.arange(10)

print(np_arange)

print(np_arange[4:8:3])

# Sliding  with Index
print(np_arange[1::2])

print(np_arange[9:1:-1])
inv = np_arange[::-1]
print(inv[1:9:3])
