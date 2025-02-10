from contextlib import suppress


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print ("Inhale , Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        super().breath()

    def __init__(self):
        print ("Swim into water")

animal = Animal()
nemo   = Fish()
nemo.breath() 