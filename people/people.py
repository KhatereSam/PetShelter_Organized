from validation.validation import validate_phone, validate_national_id, is_valid_text
from exceptions.exceptions import InvalidPersonDataError, MaximumAdoptionReachedError


class Adopter:
    MAX_ANIMALS = 9

    def __init__(self, name, phone, national_id):
        if not is_valid_text(name):
            raise InvalidPersonDataError("Adopter name cannot be empty or only numbers.")

        self.name = name.strip()
        self.phone = validate_phone(phone)
        self.national_id = validate_national_id(national_id)
        self.adopted_animals = []

    def add_animal(self, animal):
        if len(self.adopted_animals) >= self.MAX_ANIMALS:
            raise MaximumAdoptionReachedError("One person can adopt a maximum of 9 animals.")

        self.adopted_animals.append(animal.name)

    def remove_animal(self, animal):
        if animal.name in self.adopted_animals:
            self.adopted_animals.remove(animal.name)

    def show_info(self):
        return (
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"National ID: {self.national_id}\n"
            f"Adopted animals: {self.adopted_animals}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "national_id": self.national_id,
            "adopted_animals": self.adopted_animals,
        }

    @classmethod
    def from_dict(cls, data):
        adopter = cls(data["name"], data["phone"], data["national_id"])
        adopter.adopted_animals = data.get("adopted_animals", [])
        if len(adopter.adopted_animals) > adopter.MAX_ANIMALS:
            raise InvalidPersonDataError("Saved adopter data exceeds the 9-animal limit.")
        return adopter
