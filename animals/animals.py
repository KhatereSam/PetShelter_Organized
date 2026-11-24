from exceptions.exceptions import InvalidAnimalDataError
from validation.validation import (
    validate_animal_name,
    validate_animal_age,
    validate_gender,
    validate_breed,
)


class Animal:
    animal_count = 0

    def __init__(self, name, age, gender, breed):
        self.name = validate_animal_name(name)
        self.age = validate_animal_age(age)
        self.gender = validate_gender(gender)
        self.breed = validate_breed(breed)
        self._adopted = False
        Animal.animal_count += 1

    @property
    def adopted(self):
        return self._adopted

    @adopted.setter
    def adopted(self, value):
        if not isinstance(value, bool):
            raise InvalidAnimalDataError("Adopted status must be True or False.")
        self._adopted = value

    def show_info(self):
        return (
            f"Type: {self.__class__.__name__}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Breed: {self.breed}\n"
            f"Adopted: {self.adopted}"
        )

    def make_sound(self):
        return "The animal makes a sound."

    def to_dict(self):
        return {
            "type": self.__class__.__name__.lower(),
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "breed": self.breed,
            "adopted": self.adopted,
        }

    @classmethod
    def from_dict(cls, data):
        animal = create_animal(
            data["type"],
            data["name"],
            data["age"],
            data["gender"],
            data["breed"],
        )
        animal.adopted = data.get("adopted", False)
        return animal


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Tweet!"


class Dinosaur(Animal):
    def make_sound(self):
        return "Roar!"


def create_animal(animal_type, name, age, gender, breed):
    """Create an animal object based on the selected type."""
    animal_classes = {
        "dog": Dog,
        "cat": Cat,
        "bird": Bird,
        "dinosaur": Dinosaur,
    }

    if not isinstance(animal_type, str):
        raise InvalidAnimalDataError("Animal type must be Dog, Cat, Bird, or Dinosaur.")

    animal_class = animal_classes.get(animal_type.strip().lower())

    if animal_class is None:
        raise InvalidAnimalDataError("Animal type must be Dog, Cat, Bird, or Dinosaur.")

    return animal_class(name, age, gender, breed)
