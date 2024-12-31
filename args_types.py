
def person(name, age):
    print(name)
    print(age)

#Position
person('Bob', 23)
#Keyword
person(age=23, name='Bob')

#Default
def state(town='Kuje', city='Abuja'):
    print(town)
    print(city)

state()

#Variable Length Argument
def sum(a, *b):
    c = a

    for i in b:
        c = c+i

    print(c)

sum(5, 6, 34, 78)

#Keyword Variable Length Arguments
def human(name, **data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)

human('navin', age=28, city='Abuja', mob=9099427146)