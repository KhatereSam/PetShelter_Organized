from shelter.shelter import Shelter
from animals.animals import create_animal
from exceptions.exceptions import ShelterError, InvalidAnimalDataError, InvalidPersonDataError
from validation.validation import (
    validate_animal_age,
    validate_gender,
    validate_phone,
    validate_national_id,
)


def get_positive_integer(message):
    while True:
        value = input(message).strip()

        try:
            return validate_animal_age(value)
        except InvalidAnimalDataError as error:
            print(error)


def get_non_empty_text(message):
    while True:
        value = input(message).strip()

        if value and any(character.isalpha() for character in value):
            if all(character.isalpha() or character in " -'" for character in value):
                return value

        print("Please enter valid text using letters. It cannot be empty or only numbers.")


def get_gender():
    while True:
        value = input("Gender (Male/Female): ").strip()
        try:
            return validate_gender(value)
        except InvalidAnimalDataError as error:
            print(error)


def get_valid_phone():
    while True:
        value = input("Phone (11 digits, starts with 09): ").strip()
        try:
            return validate_phone(value)
        except InvalidPersonDataError as error:
            print(error)


def get_valid_national_id(message="National ID (10 digits): "):
    while True:
        value = input(message).strip()
        try:
            return validate_national_id(value)
        except InvalidPersonDataError as error:
            print(error)


def show_animal_list(animals):
    if not animals:
        print("No animals found.")
        return

    for index, animal in enumerate(animals, start=1):
        print("------------------------------")
        print(f"{index}. {animal.name}")
        print(animal.show_info())
        print("Sound:", animal.make_sound())


def add_animal_menu(shelter):
    print("\nChoose animal type:")
    print("1. Dog")
    print("2. Cat")
    print("3. Bird")
    print("4. Dinosaur")

    animal_types = {
        "1": "dog",
        "2": "cat",
        "3": "bird",
        "4": "dinosaur",
    }

    while True:
        choice = input("Enter your choice (1-4): ").strip()
        animal_type = animal_types.get(choice)

        if animal_type is not None:
            break

        print("Invalid choice. Please enter a number from 1 to 4.")

    name = get_non_empty_text("Name: ")
    age = get_positive_integer("Age: ")
    gender = get_gender()
    breed = get_non_empty_text("Breed: ")

    animal = create_animal(animal_type, name, age, gender, breed)
    shelter.add_animal(animal)
    print("Animal added successfully.")


def search_animal_menu(shelter):
    print("1. Search by name")
    print("2. Search by type")
    choice = input("Choose: ").strip()

    if choice == "1":
        animal = shelter.search_by_name(input("Animal name: ").strip())
        print(animal.show_info())
    elif choice == "2":
        animal_type = input("Animal type (Dog/Cat/Bird/Dinosaur): ").strip()
        show_animal_list(shelter.search_by_type(animal_type))
    else:
        print("Invalid choice.")


def adopt_animal_menu(shelter):
    animal_name = get_non_empty_text("Animal name: ")
    adopter_name = get_non_empty_text("Adopter name: ")
    phone = get_valid_phone()
    national_id = get_valid_national_id()

    shelter.adopt_animal(animal_name, adopter_name, phone, national_id)
    print("Animal adopted successfully.")


def return_animal_menu(shelter):
    animal_name = get_non_empty_text("Animal name: ")
    national_id = get_valid_national_id("Adopter national ID: ")

    shelter.return_animal(animal_name, national_id)
    print("Animal returned successfully.")


def main():
    shelter = Shelter()

    while True:
        print("\n========== PET SHELTER ==========")
        print("1. Add Animal")
        print("2. Show Animals")
        print("3. Search Animal")
        print("4. Adopt Animal")
        print("5. Return Animal")
        print("6. Show Available Animals")
        print("7. Show Adopted Animals")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_animal_menu(shelter)
            elif choice == "2":
                show_animal_list(shelter.show_animals())
            elif choice == "3":
                search_animal_menu(shelter)
            elif choice == "4":
                adopt_animal_menu(shelter)
            elif choice == "5":
                return_animal_menu(shelter)
            elif choice == "6":
                show_animal_list(shelter.show_available_animals())
            elif choice == "7":
                show_animal_list(shelter.show_adopted_animals())
            elif choice == "8":
                print("Thank you for using Pet Shelter.")
                break
            else:
                print("Invalid menu choice. Please choose from 1 to 8.")

        except (ShelterError, ValueError, OSError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
