a = 10
print(id(a))

def something():
    a = 15

    x = globals()['a']
    print(id(x))
    print('in fun ', a)

    globals()['a'] = 15

something()

print('outside', a)