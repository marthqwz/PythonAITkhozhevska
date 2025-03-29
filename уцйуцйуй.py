# class Human:
#     height = 180
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
# h = Human()
# s = Student()
# w = Worker()
#
# print(h.height)
# print("*"*20)
# print(s.satiety)
# print(s.height)
# print("*"*20)
# print(w.satiety)
# print(w.height)

class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    age = 1
    def __init__(self):
        print(f"height = {self.height}")
        print(f"age = {self.age}")
        print(f"satiety = {self.satiety}")

nich = Child()


class Hello:
    def __init__(self):
        print('Hello')

class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print('World')

hw = HelloWorld()

class Computer:
    def calculate(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = 128
        self.model = model
        print("Calculating...")


class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = '4k'
    def display(self):
        print("i display the image on the screen...")



class Smartphone(Computer, Display):
    def print_info(self):
        print(self.display())
        print(self.calculate())
        print(self.resolution())
        print(self.model())
        print(self.memory())



sp = Smartphone(model = "Last")
sp.print_info()
