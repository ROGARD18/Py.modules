class Plant:
    """Base class for all plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize common plant features."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """Specialized plant that can bloom"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with color."""
        super().__init__(name=name, height=height, age=age)
        self.color: str = color

    def bloom(self) -> None:
        """Display a blooming message based on color"""
        if self.color == "red":
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is blooming.")


class Tree(Plant):
    """Specialized plant that provides shade"""

    def __init__(
            self,
            name: str,
            height: int,
            age: int, trunk_diameter: int) -> None:
        """Initialize tree with trunk diameter."""
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """Display shade info"""
        shade = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetables(Plant):
    """Specialized plant for food"""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: int,
            nutritional_value: str, ) -> None:
        """Initialise Vegetables with nutritional_value"""
        super().__init__(name=name, height=height, age=age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


def main() -> None:
    """Create instances of specialized plants as required."""
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetables("Tomato", 80, 90, "summer", "vitamin C")

    print("Garden Plant Types")
    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age}", end="")
    print(f"days, {rose.color} color")
    rose.bloom()

    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age}", end="")
    print(f"days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    print(f"{tomato.name} (Veget): {tomato.height}cm, {tomato.age}", end="")
    print("days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
