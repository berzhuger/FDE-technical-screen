from typing import Union

MAX_VOLUME = 1_000_000
MAX_DIMENSION = 150
HEAVY = 20
STANDARD = "STANDARD"
SPECIAL = "SPECIAL"
REJECT = "REJECT"


def sort(width: Union[float, int], height: Union[float, int], lenght: Union[float, int], mass: Union[float, int]) -> str:
    """
    Sort the given dimensions of a box in ascending order.

    :param width: Width of the box in cm
    :param height: Height of the box in cm
    :param lenght: Length of the box in cm
    :param mass: Mass of the box in kg
    :return: String STANDARD if its not bulky or heavy
             SPECIAL if its bukly or heavy
             REJECT if its bulky and heavy
    """
    for dim in (width, height, lenght, mass):
        if not isinstance(dim, (float, int)):
            raise TypeError("All values must be numbers")
        elif dim <= 0:
            raise ValueError("All values must be positive")

    volume = width * height * lenght
    is_bulky = volume >= MAX_VOLUME or max(width, height, lenght) >= MAX_DIMENSION
    is_heavy = mass >= HEAVY

    if is_bulky and is_heavy:
        return REJECT
    elif is_bulky or is_heavy:
        return SPECIAL
    return STANDARD
