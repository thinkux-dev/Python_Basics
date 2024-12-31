import sys

# sys.setrecursionlimit(2000)
#
# print(sys.getrecursionlimit())
#
# def greet():
#     print('Hello')
#     greet()
#
# greet()

#Factorial using recursion
def fact(n):

    if n==0:
        return 1

    return n * fact(n-1)

result = fact(5)
print(result)