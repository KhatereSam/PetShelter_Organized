class ShelterError(Exception):
    """Base exception for the pet shelter."""


class AnimalNotFoundError(ShelterError):
    pass


class DuplicateAnimalError(ShelterError):
    pass


class AnimalAlreadyAdoptedError(ShelterError):
    pass


class AnimalNotAdoptedError(ShelterError):
    pass


class MaximumAdoptionReachedError(ShelterError):
    pass


class InvalidPersonDataError(ShelterError):
    pass


class InvalidAnimalDataError(ShelterError):
    pass
