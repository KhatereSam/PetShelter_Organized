from exceptions.exceptions import (
    AnimalNotFoundError,
    DuplicateAnimalError,
    AnimalAlreadyAdoptedError,
    AnimalNotAdoptedError,
    MaximumAdoptionReachedError,
)
from decorators.decorators import log_operation
from data_manager.data_manager import DataManager
from people.people import Adopter


class Shelter:
    def __init__(self):
        self.animals = []
        self.adopters = []
        self.data_manager = DataManager()
        self.load_data()

    def load_data(self):
        self.animals, self.adopters = self.data_manager.load_data()

    def save_data(self):
        self.data_manager.save_data(self.animals, self.adopters)

    def find_animal(self, animal_name):
        for animal in self.animals:
            if animal.name.lower() == animal_name.strip().lower():
                return animal
        raise AnimalNotFoundError("Animal was not found.")

    def find_adopter(self, national_id):
        for adopter in self.adopters:
            if adopter.national_id == national_id:
                return adopter
        return None

    @log_operation
    def add_animal(self, animal):
        for current_animal in self.animals:
            if current_animal.name.lower() == animal.name.lower():
                raise DuplicateAnimalError("An animal with this name already exists.")

        self.animals.append(animal)
        self.save_data()

    @log_operation
    def remove_animal(self, animal_name):
        animal = self.find_animal(animal_name)

        if animal.adopted:
            raise AnimalAlreadyAdoptedError("An adopted animal cannot be removed.")

        self.animals.remove(animal)
        self.save_data()

    def search_by_name(self, animal_name):
        return self.find_animal(animal_name)

    def search_by_type(self, animal_type):
        result = []

        for animal in self.animals:
            if animal.__class__.__name__.lower() == animal_type.strip().lower():
                result.append(animal)

        return result

    def show_animals(self):
        return self.animals

    def show_available_animals(self):
        return [animal for animal in self.animals if not animal.adopted]

    def show_adopted_animals(self):
        return [animal for animal in self.animals if animal.adopted]

    @log_operation
    def adopt_animal(self, animal_name, adopter_name, phone, national_id):
        animal = self.find_animal(animal_name)

        if animal.adopted:
            raise AnimalAlreadyAdoptedError("This animal has already been adopted.")

        adopter = self.find_adopter(national_id)

        if adopter is None:
            adopter = Adopter(adopter_name, phone, national_id)
            self.adopters.append(adopter)

        if len(adopter.adopted_animals) >= adopter.MAX_ANIMALS:
            raise MaximumAdoptionReachedError("One person can adopt a maximum of 9 animals.")

        adopter.add_animal(animal)
        animal.adopted = True
        self.save_data()
        return adopter

    @log_operation
    def return_animal(self, animal_name, national_id):
        animal = self.find_animal(animal_name)

        if not animal.adopted:
            raise AnimalNotAdoptedError("This animal has not been adopted.")

        adopter = self.find_adopter(national_id)

        if adopter is None or animal.name not in adopter.adopted_animals:
            raise AnimalNotAdoptedError("This animal is not registered to this adopter.")

        adopter.remove_animal(animal)
        animal.adopted = False
        self.save_data()
