import re
from exceptions.exceptions import InvalidPersonDataError, InvalidAnimalDataError


def is_valid_text(value):
    if not isinstance(value, str):
        return False

    value = value.strip()

    if not value or not any(character.isalpha() for character in value):
        return False

    for character in value:
        if not (character.isalpha() or character in " -'"):
            return False

    return True


def validate_animal_name(name):
    if not is_valid_text(name):
        raise InvalidAnimalDataError("Name must contain letters and cannot be empty or only numbers.")
    return name.strip()


def validate_animal_age(age):
    if isinstance(age, bool):
        raise InvalidAnimalDataError("Age must be a positive whole number.")

    try:
        age = int(age)
    except (ValueError, TypeError):
        raise InvalidAnimalDataError("Age must be a positive whole number.")

    if age <= 0:
        raise InvalidAnimalDataError("Age must be greater than zero.")

    return age


def validate_gender(gender):
    if not isinstance(gender, str):
        raise InvalidAnimalDataError("Gender must be Male or Female.")

    gender = gender.strip().lower()

    if gender not in ["male", "female"]:
        raise InvalidAnimalDataError("Gender must be Male or Female.")

    return gender.title()


def validate_breed(breed):
    if not is_valid_text(breed):
        raise InvalidAnimalDataError("Breed cannot be empty or only numbers.")
    return breed.strip()


def validate_phone(phone):
    if not isinstance(phone, str):
        raise InvalidPersonDataError("Phone number must be text.")

    phone = phone.strip()

    if re.fullmatch(r"09[0-9]{9}", phone) is None:
        raise InvalidPersonDataError("Phone number must contain 11 digits and start with 09.")

    return phone


def validate_national_id(national_id):
    if not isinstance(national_id, str):
        raise InvalidPersonDataError("National ID must be text.")

    national_id = national_id.strip()

    if re.fullmatch(r"[0-9]{10}", national_id) is None:
        raise InvalidPersonDataError("National ID must contain exactly 10 digits.")

    if len(set(national_id)) == 1:
        raise InvalidPersonDataError("National ID is not valid.")

    check = int(national_id[9])
    total = 0

    for index in range(9):
        total += int(national_id[index]) * (10 - index)

    remainder = total % 11

    if remainder < 2:
        valid = check == remainder
    else:
        valid = check == 11 - remainder

    if not valid:
        raise InvalidPersonDataError("National ID is not valid.")

    return national_id
