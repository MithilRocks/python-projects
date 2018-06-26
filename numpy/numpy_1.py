# Learning from https://www.youtube.com/watch?v=8JfDAm9y_7s

# Numpy gives us an advantage to work with multi-dimensional arrays. 
# Better than lists as it uses less memory, faster and convenient

import numpy as np 

# 2-dimensional array
a = np.array([(1,2,3),(4,5,6)])
print(a)

import time 
import sys

S = range(10000)
# memory occupied by list
# print(sys.getsizeof(5)*len(S))

D = np.arange(10000)
# memory occupied by numpy arrays
# print(D.size*D.itemsize)

# when you print those values, you'll see numpy arrays take up a lesser size

# Now to demonstrate time taken

Size = 1000000

l1 = range(Size)
l2 = range(Size)

a1 = np.arange(Size)
a2 = np.arange(Size)

start = time.time()
result = [(x,y) for x,y in zip(l1,l2)]
# time taken for lists
# print((time.time() - start)*1000)

start = time.time()

result = a1 + a2
# time taken for numpy arrays
# print((time.time() - start)*1000)

# upon printing both values, one can see numpy takes lesser time. also, it is really convenient to add two lists


