class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 working')


class B:

    def __init__(self):
        print('in B init')

    def feature3(self):
        print('Feature 3 working')

    def feature4(self):
        print('Feature 4 working')


class C(A,B):
    def __init__(self):
        super().__init__()
        print('in C init')

    def feature5(self):
        print('Feature 5 working')


# a1 =A()
# a1.feature1()
# a1.feature2()

# b1 = B()
# b1.feature1()

c1 = C()
# c1.feature2()