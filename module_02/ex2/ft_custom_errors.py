class GardenError(Exception):
    """Base class for exceptions in this module."""
    pass


class PlantError(GardenError):
    """Exception raised for errors in plant attributes."""
    pass


class WaterError(GardenError):
    """Exception raised for errors in the watering process."""
    pass


def plant_age(age: int) -> None:
    """
    Function use to check the age if it's over than 10.

    Args:
        age (int): age tested

    Raises:
        PlantError: if age > 10
    """
    if age > 10:
        raise PlantError("Age impossible to attibute: too old")
    if age < 0:
        raise PlantError("age impossible to attribute: 0 or negative")
    print(f"{age} this can be a posible age.")


def plant_watter(liters: int) -> None:
    """
    Function use to check the water if it's lower than 2.

    Args:
        liters (int): value tested

    Raises:
        WaterError: Error if liters < 2
    """
    if liters < 2:
        raise WaterError("Not enough water in the tank!")
    print(f"{liters} it's good for the plant")


def test_error() -> None:
    """Tester functions of plant_watter and plant_age.
    """
    print("=== Custom Garden Demo ===\n")
    for i in range(4):
        if (i < 2):
            try:
                if (i == 0):
                    print("Testing PlantError...")
                    plant_age(11)
                elif (i == 1):
                    print("\nTesting WaterError...")
                    plant_watter(1)
            except (GardenError) as e:
                print(f"Caught {e.__class__.__name__} {e}")
        else:
            try:
                if (i < 3):
                    print("\nTesting catching all garden errors...")
                    plant_age(11)
                else:
                    plant_watter(1)
            except GardenError as e:
                print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error()
