class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is:", self.cpu, self.ram)

com1 = Computer('i5', 16)
com2 = Computer('Ryzen3', 8)

com1.config()
com2.config()

class Person:

    def __init__(self):
        self.name = 'Bob'
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

p1 = Person()
p2 = Person()

p1.name = "Navin"
p1.age = 16

if p1.compare(p2):
    print("They are same")

p1.update()

print(p1.name)
print(p2.name)

class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

c1 = Car()
c2 = Car()

Car.wheels = 5

c1.mil = 8
print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)