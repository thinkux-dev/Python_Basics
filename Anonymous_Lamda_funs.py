from functools import reduce


f = lambda a,b : a+b

result = f(5,6)
print(result)

print('=======================================')

#filter
is_even = lambda n : n%2==0
nums = [3,1,2,5,4,6,8,9,7]

evens = list(filter(is_even, nums))
print(evens)

print('=======================================')

#Map
update = lambda  n : n*2

doubles = list(map(update, evens))
print(doubles)

print('=======================================')

#Reduce
add_all = lambda a,b : a+b

sum = reduce(add_all, doubles)
print(sum)