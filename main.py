from animals import Animal, Dog, Bird, Fish, Cat

my_dog = Dog("jeffrey", "67", "Woof!", "lab")
my_bird = Bird("john", "117", "Tweet", True)
my_fish = Fish("bubbles", "3", "fresh")
my_cat = Cat("brighton", "44", "Meow", False)
animals = [my_dog, my_bird, my_fish, my_cat]

def main():
    # Create one instance of each animal subclass
    



    
    print(animals)
    # TODO: instantiate your animals and add them to the list

    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        Dog.speak()
        Bird.speak()
        Fish.speak()
        Cat.speak()
        

if __name__ == "__main__":
    main()
