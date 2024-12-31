#Example 1
def topten():

    yield 1
    yield 2
    yield 3
    yield 4

values = topten()

print(next(values))
print(values.__next__())

for i in values:
    print(i)

#Example 2
def toptenPerfectSquare():
    n = 1

    while n<=10:
        sq = n*n
        yield sq
        n += 1


values = toptenPerfectSquare()

for i in values:
    print(i)
