import numpy as np 
from array import *
#Padding 
m = np.ones((3,3))
#print("Before ",m)
m = np.pad(m , pad_width=1,  mode="constant" , constant_values=0)
#print("After Padding " ,m)

#Chessboard pattern
import numpy as np
x = np.ones((3,3))
x = np.zeros((11,11),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)

#List into tuple into array
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(type(l), l)
tup = tuple(l)
print(type(tup), tup)
arr = array("i", tup)
print(type(arr), arr)

#appent values at the end of arrays
arr = array("i", [1,5,9,6,5,4,8])
print(arr)
arr = np.append(arr,[55,80])
print(arr)

#intersection of two array
array1 = np.array([1,5,8,9,6,2,4])
array2 = np.array([8,9,45,65])
print(np.intersect1d(array1, array2))

#Differance of two array
array1 = np.array([1,5,8,9,6,2,4])
array2 = np.array([8,9,45,65])
print(np.setdiff1d(array1, array2))

#Unique of two array
array1 = np.array([1,5,8,9,6,2,4])
array2 = np.array([8,9,45,65])
print(np.setxor1d(array1, array2))

#Compair two array
a = [1, 2]
b = [4, 5]
print(np.greater_equal(a, b))
print(np.greater(a, b))
print(np.less_equal(a, b))
print(np.less(a, b))
