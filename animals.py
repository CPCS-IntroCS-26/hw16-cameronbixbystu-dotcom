class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}. ")

    def move(self):
        print(f"{self.name} moves around. ")

    def describe(self):
        print(f"{self.name} is a {self.age} years old {self.__class__name__}.")


class Dog(Animal):
    def init(self, name, age, sound, breed):
        super.init(name, age)
        self.sound = sound
        self.breed = breed



class Bird(Animal):
    def init(self, name, age, water):
        super.init(name, age)
        self.water = water

    


class Fish(Animal):
    def init(self, name, age, sound):
        super.init(name, age)
        self.sound = sound


class Cat(Animal):
    def init(self, name, age, sound, indoor):
        super.init(name, age)
        self.sound = sound
        self.indoor = indoor
