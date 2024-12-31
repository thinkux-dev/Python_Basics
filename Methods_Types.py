class Student:

    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #Instance Method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    #Class Method
    @classmethod
    def getSchool(cls):
        return cls.school

    #Static Method
    @staticmethod
    def info():
        print('This is Student class.')


s1 = Student(23, 45, 76)
s2 = Student(43, 56, 32)

print(s2.avg())
print(Student.getSchool())

Student.info()