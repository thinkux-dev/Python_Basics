def greet():
    print('Hello')
    print('Good Morning')

def add_sub(x, y):
    c = x+y
    d = x-y
    return c, d

greet()
result1, result2 = add_sub(5, 6)
print(result1)
print(result2)

print('=========================================')
def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

lst = [20, 25, 14, 72, 75, 45, 90, 32, 49, 70, 45]

even, odd = count(lst)

print(even)
print(odd)
print("Even : {} and Odd : {}".format(even, odd))