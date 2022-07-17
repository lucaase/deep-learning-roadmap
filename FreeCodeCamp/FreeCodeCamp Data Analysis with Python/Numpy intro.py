import numpy as np

''' Operations with numpy arrays '''

# create a numpy array
a = np.array([1, 2, 3, 4, 5])

# operations are broadcasted to all elements
print(a*2)

# can also do broadcasting with 2 arrays
b = np.array([1, 2, 3, 4, 5])
print(a*b)

# broadcasting with boolean arrays
c = np.array([True, False, True, False, True])
print(a*c)

# subsetting with boolean arrays
print(a[c])
print(a[a<2])
print(a[a>a.mean()])

# Linear algebra operations in numpy
# dot product
print(a.dot(b))
# matrix transpose
print(a.dot(b.T))
# matrix multiplication
print(a@b)
