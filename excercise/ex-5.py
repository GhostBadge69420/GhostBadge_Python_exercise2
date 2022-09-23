#define a new type called person these person object
#should have name attribute as well as a talk method.

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

Canniest = Person("Canniest")
Canniest.talk()

Badger = Person("Badger")
Badger.talk()