class Plant:
    """Base class for all plants with name, height and age.."""

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

    def get_info(self, subclass: str) -> str:
        return (f"{self.name} ({subclass}): {self.height}cm, {self.age} days")


class Flower(Plant):
    """Specialized 'Plant' that can bloom"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with color."""
        super().__init__(name=name, height=height, age=age)
        self.color: str = color

    def get_color(self) -> str:
        return (f", {self.color} color")

    def bloom(self) -> None:
        """Display a blooming message based on color"""
        if self.color == "red":
            print(f"{self.name} is ", end="")
            print("blooming beautifully!\n")
        else:
            print(f"{self.name} ({self.__class__.__name__}) is blooming.\n")


class Tree(Plant):
    """Specialized 'Plant' that provides shade"""

    def __init__(
            self,
            name: str,
            height: int,
            age: int, trunk_diameter: int) -> None:
        """Initialize tree with trunk diameter."""
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter: int = trunk_diameter

    def get_diameter(self) -> str:
        return (f", {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Display shade info"""
        shade = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade} square meters of shade\n")


class Vegetable(Plant):
    """Specialized plant for food"""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: int,
            nutritional_value: str, ) -> None:
        """Initialise Vegetable(with nutritional_value"""
        super().__init__(name=name, height=height, age=age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_season(self) -> str:
        return (f", {self.harvest_season} harvest")

    def get_nutritional_value(self) -> str:
        return (f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Create instances of specialized plants as required."""
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print("=== Garden Plant Types ===\n")
    print(f"{rose.get_info(rose.__class__.__name__)}", end="")
    print(f"{rose.color} color")
    rose.bloom()

    print(f"{oak.get_info(oak.__class__.__name__)}", end="")
    print(f"{oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    print(f"{tomato.get_info(tomato.__class__.__name__)}", end="")
    print(f"{tomato.get_season()}")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")


if __name__ == "__main__":
    main()
