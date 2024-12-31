#Duck Typing with Polymorphism
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')

class Laptop:
    def code(self, ide):
        ide.execute()

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)


#Operator Overloading with Polymorphism
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return  s3

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1>s2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(58,69)
s2 = Student(90,34)

s3 = s1+s2
print(s3.m1)
print(s3.m2)

if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')

print(s1.__str__())


#Method Overloading with Polymorphism
class Overloading:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0

        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a


        return s


s1 = Overloading(56,54)

print(s1.sum(5,9))

#Method Overriding with Polymorphism
class A:

    def show(self):
        print('in A show')


class B(A):
    def show(self):
        print('in B show')


a1 = B()
a1.show()