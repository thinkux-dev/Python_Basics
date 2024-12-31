from  numpy import *
arr = array([2, 4, 5, 7, 9], int)

newarr = linspace(0,15, 20)
newarr2 = arange(1, 15, 2)
newarr3 = linspace(1, 40, 5)
newarr4 = logspace(1, 40, 5)
newarr5 = zeros(5)
newarr6 = ones(5, int)

print(arr)
print(newarr)
print(newarr2)
print(newarr3)
print('%.2f' %newarr4[4])
print(newarr5)
print(newarr6)

arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()

print(id(arr1))
print(id(arr2))