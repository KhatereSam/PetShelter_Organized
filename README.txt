PET SHELTER - ORGANIZED VERSION

HOW TO RUN
1. Extract the ZIP file.
2. Open the extracted PetShelter_Organized folder in VS Code.
3. Open the terminal in that folder (the folder containing main.py).
4. Run: python main.py

PROJECT STRUCTURE
- main.py: program menu and user input
- animals/: Animal, Dog, Cat, Bird, Dinosaur and animal creation
- people/: Adopter class
- validation/: input validation and regular expressions
- exceptions/: custom exception classes
- decorators/: log_operation decorator
- data_manager/: JSON save/load operations
- shelter/: shelter operations
- data/: saved JSON data is created here automatically

CHANGES IN THIS VERSION
- Related Python files are grouped into separate packages.
- Imports have been updated for the new folder structure.
- Animal lists use enumerate(start=1) to show a number beside each animal.
- JSON data is saved inside the data folder, not beside the Python files.

NOTES
- Keep the folder structure unchanged so imports continue to work.
- Run main.py from the project root folder.
- The data/shelter_data.json file is created after data is saved for the first time.
