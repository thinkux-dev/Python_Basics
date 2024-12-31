from numpy import *

arr1 = array([
    [1,2,3,6,8,2],
    [4,5,6,7,8,9]
])

arr2 = arr1.flatten()

arr3 = arr2.reshape(2,2,3)

m = matrix(arr1)
mt = matrix('1 2 3; 6 7 3; 4 5 7')

m1 = matrix('1 2 3; 6 7 3; 4 5 7')
m2 = matrix('1 2 3; 6 8 2; 7 5 7')

m3 = m1*m2

print(arr1.ndim)
print('==================================')
print(arr1.shape)
print('==================================')
print(arr1.size)
print('==================================')

print(arr2)
print('==================================')
print(arr3)

print('==================================')
print(m)
print('==================================')
print(diagonal(mt))

print('==================================')
print(m3)