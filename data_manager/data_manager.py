import json
import os
from animals.animals import Animal
from people.people import Adopter


class DataManager:
    def __init__(self, file_name="shelter_data.json"):
        project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_folder = os.path.join(project_folder, "data")
        os.makedirs(data_folder, exist_ok=True)
        self.file_name = os.path.join(data_folder, file_name)

    def save_data(self, animals, adopters):
        data = {
            "animals": [animal.to_dict() for animal in animals],
            "adopters": [adopter.to_dict() for adopter in adopters],
        }

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load_data(self):
        if not os.path.exists(self.file_name):
            return [], []

        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)

            animals = [Animal.from_dict(item) for item in data.get("animals", [])]
            adopters = [Adopter.from_dict(item) for item in data.get("adopters", [])]
            return animals, adopters

        except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError) as error:
            print(f"Could not load saved data: {error}")
            return [], []
