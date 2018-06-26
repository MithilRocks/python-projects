import numpy as np 

a = np.array([(1,2,3,4,5),(6,7,8,9,10)])
# shows the dimension of the array
print(a.ndim)

# shows the number of bytes each data stores
print(a.itemsize)

# shows the data type of the elements
print(a.dtype)

# shows the number of elements in the array
print(a.size)

# shows the shape of the array (rows X columns)
print(a.shape)

# convert rows to columns and columns to rows
print(a.reshape(5,2))

# we can do slicing. This gets third index from first array
print(a[0,3])

# This gets third index from all the rows
print(a[0:,3])

# Get the n number of values between a and b (linspace(a,b,n))
print(np.linspace(1,3,10))