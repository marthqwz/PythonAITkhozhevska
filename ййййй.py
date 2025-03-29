class Grandparent:
    height = 170
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
