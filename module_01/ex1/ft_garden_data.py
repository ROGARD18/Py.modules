class Plant:
    """New class represents a plant"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize the plant with name, height and age"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def print_plant(self) -> None:
        """Print plant's infos"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Test creation of plant and display her infos"""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.print_plant()
    sunflower.print_plant()
    cactus.print_plant()


if __name__ == "__main__":
    main()
