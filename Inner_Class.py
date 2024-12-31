class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)

s1.show()

lap1 = s1.lap
lap2 = s2.lap

# lap2.show()