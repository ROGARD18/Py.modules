class Plant:
    """New class represents a plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, height and age"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth: int) -> None:
        """Increase plant's height by the growth value"""
        self.height += growth

    def ages(self) -> None:
        """Increase plant's age by one day"""
        self.age += 1

    def get_info(self) -> str:
        """Return a string with all plant's infos"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def week_effect(self, growth: int) -> None:
    """function use to simulate a week on a plant"""
    for i in range(1, 8):
        self.grow(growth)
        self.ages()


def main() -> None:
    """Test creation of plants, dysplays infos, test to grow and ages
    plants and simulate a week on plant"""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Day 1 ===\n")
    print(f"{rose.get_info()}")
    print(f"{sunflower.get_info()}")
    print(f"{cactus.get_info()}")
    week_effect(rose, 2)
    week_effect(sunflower, 1)
    week_effect(cactus, 3)
    print("\n=== Day 7 ===\n")
    print(f"{rose.get_info()}")
    print(f"{sunflower.get_info()}")
    print(f"{cactus.get_info()}")


if __name__ == "__main__":
    main()
