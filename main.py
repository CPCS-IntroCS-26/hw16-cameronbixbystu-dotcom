from animals import Animal, Dog, Bird, Fish, Cat


def main():
    # Create one instance of each animal subclass
    animals = []
    

    # TODO: instantiate your animals and add them to the list

    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        pass
        

if __name__ == "__main__":
    main()

from animals import Animal, Dog, Bird, Fish, Cat
import pickle




LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


FILENAME = 'pets.dat'


def main():
    mypets = load_pets()


    choice = 0


    while choice != QUIT:
        choice = get_menu_choice()


        if choice == LOOK_UP:
            look_up(mypets)
        elif choice == ADD:
            add(mypets)
        elif choice == CHANGE:
            change(mypets)
        elif choice == DELETE:
            delete(mypets)


    save_pets(mypets)






def load_pets():
    try:
        input_file = open(FILENAME, 'rb')


        pet_dct = pickle.load(input_file)


        input_file.close()
    except IOError:
        pet_dct = {}


    return pet_dct






def get_menu_choice():
    print()
    print("Menu")
    print("---------------------------")
    print('1. Look up a car')
    print('2. Add a new car')
    print('3. Change an existing car')
    print('4. Delete a car')
    print("5. Quite the program")
    print()


    choice = int(input('Enter a valid choice: '))


    return choice








def look_up(mypets):
    make = input("Enter a make: ")
    print(mypets.get(make, 'That make is not found.'))








def add(mypets):
    make = input('Make: ')
    year_model = input('year model: ')
    speed = 0


    entry = animal.Animal(make, year_model, speed)


    if make not in mypets:
        mypets[make] = entry
        print("The entry has been added.")
    else:
        print('That make already exists.')






'''

def change(mypets):
    make = input('Enter a make: ')

    if make in mypets:
        year_model = input('Enter the new year_model: ')
        speed = input('Enter the new speed: ')
        entry = car.Car(make, year_model, speed)
        mypets[make] = entry
        print('Information updated.')
    else:
        print('That make is not found.')
'''




def change(mypets):
    make = input('Enter a make: ')

    if make in mypets:
        speed = mypets[speed] + 5
        entry = car.Car(make, speed)
        mypets[make] = entry
        print('Information updated.')
    else:
        print('That make is not found.')





def delete(mypets):
    make = input('Enter a make: ')
    if make in mypets:
        del mypets[make]
        print('Entry deleted.')
    else:
        print('That make is not found.')








def save_pets(mypets):
    output_file = open(FILENAME, 'wb')


    pickle.dump(mypets, output_file)


    output_file.close()



def acceleration(mypets):
    make = input('Enter a make: ')
    if make in mypets:
        speed = make + 5





if __name__ == '__main__':
    main()
