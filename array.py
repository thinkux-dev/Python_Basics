from array import *

vals = array('i',[5, 9, -8, 4, 2])
char = array('u',['a', 'e', 'i'])

#reverse array manually

for index in range(len(vals), -1, -1):
    print(vals[index])

# newArr = array(vals.typecode, (a for a in vals))
#
# print('buffer_info: ', vals.buffer_info())
# print('typeCode: ', vals.typecode)
# print('length: ', len(vals))
#
# valLen = len(vals)
#
# for val in range(valLen):
#     print(vals[val])
#
# i = 0
#
# while i<valLen:
#     print(vals[i])
#     i+=1
#
# #array from user input
# arr = array('i', [])
# n = int(input("Enter the length of the array"))
#
# for i in range(n):
#     x = int(input('Enter the next value'))
#     arr.append(x)
#
# print(arr)
#
# #search using manually
# num = int(input('Enter the value for search'))
#
# k=0
# for e in arr:
#     if e==num:
#         print(k)
#         break
#     k+=1
#
# #search using functions
# print(arr.index(num))
