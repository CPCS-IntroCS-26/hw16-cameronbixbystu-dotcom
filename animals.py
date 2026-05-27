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
        print(f"{self.name} is a {self.age} years old {self.class_name}.")


class Dog(Animal):
    def init(self, name, age, breed):
        super.init(name, age, "Woof")
        self.breed = breed



class Bird(Animal):
    def init(self, name, age, fly):
        super.init(name, age, "Tweet")
        self.fly = fly

    


class Fish(Animal):
    def init(self, name, age, water):
        super.init(name, age)
        self.water = water


class Cat(Animal):
    def init(self, name, age, indoor):
        super.init(name, age, "Meow")
        self.indoor = indoor
