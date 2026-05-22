from animals import Animal, Dog, Bird, Fish, Cat

def dog():
    name = input("What is the dog's name. ")
    age = input("What is the dog's age. ")
    breed = input("What breed is the dog. ")
    dog = Dog(name, age, breed)
    return dog


def main():
    # Create one instance of each animal subclass
    

    dog_input = dog()


    animals = [dog_input]
    
    print(animals)
    # TODO: instantiate your animals and add them to the list

    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        pass
        

if __name__ == "__main__":
    main()
