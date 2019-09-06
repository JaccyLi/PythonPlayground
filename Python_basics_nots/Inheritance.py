class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"A(n) pet called {self.name} is walking.")

class Dog(Mammal):
    def bark(self):
        print(f"A(n) dog called {self.name} is barking.")

class Cat(Mammal):
    def chase_mice(self):
        print(f"A(n) cat called {self.name} is chasing mice.")


dog = Dog("Micci")
dog.walk()
dog2 = Dog("Haulk")
dog2.bark()
