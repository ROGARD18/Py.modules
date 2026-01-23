class Plant:
    """
    Class represents a plant with a name, a height and an age.
    Within 1 function:
    - function use to return all plant's data to display it after.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Init all plant's data with args.

        Args:
            name (str): Plant's name
            height (int): Plant's height
            age (int): Plant's age
        """

        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """
        Return a string with all plant's data.
        """

        return f"{self.name} ({self.height}cm, {self.age} days)"


def plant_factory() -> None:
    """Plant's factory use to create and add plant in a garden."""
    i = 0
    plant_list = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    garden = []
    for data in plant_list:
        plant = Plant(data[0], data[1], data[2])
        garden.append(plant)
        i += 1

    for plant in garden:
        print(f"Created: {plant.get_data()}")

    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_factory()
