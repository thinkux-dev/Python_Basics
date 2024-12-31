# # fibonacci 1
# n =50
# a,b = 0, 1
# for i in range(n):
#     print(a, end=' ')
#     a,b = b,a+b

# # fibonacci 2
# n =50
# a,b = 0, 1
# while a<= 50:
#     print(a, end=' ')
#     a,b = b,a+b

def fib(n):

    a = 0
    b = 1

    if n==1:
        print(a)
    elif n<0:
        print('Invalid number')
    else:
        for i in range(n):
            while a<50:
                print(a)
                a, b = b, a+b

fib(100)