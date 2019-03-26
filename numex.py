import numpy as np
# array1 is a 10*10 matrix ranging from 1-100 
a1 = np.arange(100).reshape(10, 10)
a1 = a1 + 1
print(a1)

# array2 is a 10*10 matrix with random numbers
a2 = np.random.randint(100, size = 100).reshape(10,10)
print(a2)

# array3 is a 10*10 matrix, all elements are valued 100
a3 = np.arange(100).reshape(10, 10)
a3 = a3 - a3 + 100
print(a3)

''' Data analysis '''

#dimension for a1
print("a: ", a1.ndim)

#shape for a2
print("b: ", a2.shape)

#the size for array3
print("c: ", a3.size)

#datatype for a1,a2,a3
print("d: ", a1.dtype)
print("d: ", a2.dtype)
print("d: ", a3.dtype)

#total sum for all elements of a1, a2, a3
print("e: ", a1.sum())
print("e: ", a2.sum())
print("e: ", a3.sum())

#row total of all elements for array 1
print("f: ", a1.sum(axis=1))

#Column total of all elements for array 1
print("g: ", a1.sum(axis=0))

#min/max numbers of array2
print("h: ", a2.max())
print("h: ", a2.min()) 

#create an array 4 where a4 = a2-a1
a4 = np.arange(100).reshape(10, 10)
a4 = a1 - a2
print(a4)

#calculuate the min values of each row
print("i: ", a4.min(axis=1))

