class Plant:
    """New class represents a plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, height and age"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return a string with all plant's infos"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def plant_factory() -> None:
    """Plant's factory to create and add plant in the garden"""
    i = 0
    plant_list = [
        ["Rose", 25, 30],
        ["Sunflower", 80, 45],
        ["Cactus", 15, 120],
        ["Tulip", 10, 5],
        ["Lavender", 20, 15]
    ]
    print("=== Plant Factory Output ===\n")
    garden = []
    for info in plant_list:
        plant = Plant(info[0], info[1], info[2])
        garden.append(plant)
        i += 1

    for plant in garden:
        print(f"Created: {plant.get_info()}")

    print(f"Total plants created: {i}")


if __name__ == "__main__":
    plant_factory()
