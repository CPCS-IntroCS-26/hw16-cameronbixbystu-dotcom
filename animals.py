class Animal:
    def __init__(self, name, age, sound):
        pass

    def speak(self):
        pass

    def move(self):
        pass

    def describe(self):
        pass

    def __str__(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, breed, sound):
        self.__name = name
        self.__age = age
        self.__breed = breed
        self.__sound = sound


    def set_name(self, name):
        self.__name = name


    def set_age(self, age):
        self.__age = age


    def set_breed(self, breed):
        self.__breed = breed


    def set_sound(self, sound):
        self.__sound = sound


    def get_name(self):
        return self.__name
   
    def get_age(self):
        return self.__age
   
    def get_breed(self):
        return self.__breed
   
    def __str__(self):
        return f'Name: {self.__name}\n' + \
            f'Age: {self.__age}\n' + \
            f'Breed: {self.__breed}'

    def speak(self):
        Animal.speak = f"{name} says Woof."
        pass

    def move(self):
        Animal.move = f"{name} runs on four legs."
        pass


class Bird(Animal):
    def __init__(self, name, age, breed):
        self.__name = name
        self.__age = age
        self.__can_fly = can_fly


    def set_name(self, name):
        self.__name = name


    def set_type(self, age):
        self.__age = age


    def set_age(self, can_fly):
        self.__can_fly = can_fly


    def get_name(self):
        return self.__name
   
    def get_type(self):
        return self.__age
   
    def get_age(self):
        return self.__can_fly
   
    def __str__(self):
        return f'Name: {self.__name}\n' + \
            f'Age: {self.__age}\n' + \
            f'Breed: {self.__can_fly}'

    def speak(self):
        Animal.speak = f"{name} says caw caw."
        pass

    def move(self):
        Animal.move = f"{name} flies through the air."
        pass

    


class Fish(Animal):
    def __init__(self, name, age, water_type):
        pass

    def move(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, indoor):
        pass

    def speak(self):
        pass

    def move(self):
        pass
