class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_age(age: int) -> None:
    if age > 10:
        raise PlantError()
    print(f"{age} this can be a posible age.")


def plant_watter(liters: int) -> None:
    if liters > 2:
        raise WaterError()
    print(f"{liters} it's good for this plant")


def test_error() -> None:
    print("=== Custom Garden Demo ===")
    print("\nTesting PlantError...")
    try:
        plant_age(40)
    except PlantError:
        print("Caught PlantError : age not possible!")
    print("\nTesting WaterError...")
    try:
        plant_watter(4)
    except PlantError:
        print("Caught PlantError : too much water!")


if __name__ == "__main__":
    test_error()
