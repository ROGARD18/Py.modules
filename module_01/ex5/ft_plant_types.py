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

    def get_info(self, class_n: str) -> str:
        """
        Use to return all plant's data

        Args:
            class_name (str): name of the class
        """
        return (f"{self.name} ({class_n}): {self.height}cm, {self.age} days")


class Flower(Plant):
    """Specialized 'Plant' that can bloom"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with color."""
        super().__init__(name=name, height=height, age=age)
        self.color: str = color

    def get_color(self) -> str:
        """Return the flower's color."""
        return (f", {self.color} color")

    def bloom(self) -> str:
        """Display a blooming message based on color"""
        if self.color == "red":
            return (f"{self.name} is " + "blooming beautifully!\n")
        else:
            return (f"{self.name} ({self.__class__.__name__}) is blooming.\n")

    def get_info(self) -> str:
        """
        Use to return all plant flower data

        Returns:
            _type_: all infos of the flower
        """
        return (super().get_info(self.__class__.__name__)
                + (f" {self.color}\n")
                + f"{self.bloom()}\n")


class Tree(Plant):
    """Specialized 'Plant' type that provides shade"""

    def __init__(
            self,
            name: str,
            height: int,
            age: int, trunk_diameter: int) -> None:
        """Initialize tree with trunk diameter."""
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter: int = trunk_diameter

    def get_diameter(self) -> str:
        """ Use to return trunk_diameter"""
        return (f", {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> str:
        """Display shade info"""
        shade = self.trunk_diameter * 1.5
        return (f"{self.name} provides {shade} square meters of shade\n")

    def get_info(self) -> str:
        """
        Use to return all plant tree data

        Returns:
            _type_: all infos of the tree
        """
        return (super().get_info(self.__class__.__name__)
                + (f" {str(self.trunk_diameter)}cm diameter\n")
                + f"{self.produce_shade()}\n")


class Vegetable(Plant):
    """Specialized plant for food"""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: int,
            nutritional_value: str, ) -> None:
        """Initialise Vegetable(with nutritional_value and a season)"""
        super().__init__(name=name, height=height, age=age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_season(self) -> str:
        """
        Use to return the season

        Returns:
            str: the season
        """
        return (f", {self.harvest_season} harvest")

    def get_nutritional_value(self) -> str:
        """
        Use to return the nutrionnal_value

        Returns:
            str: the nutrionnal_value
        """
        return (f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> str:
        """
        Use to return all plant vegetable data

        Returns:
            _type_: all infos of the vegetable
        """
        return (super().get_info(self.__class__.__name__)
                + f" {self.harvest_season} harvest\n"
                + f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """Create instances of specialized plants as required."""
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print("=== Garden Plant Types ===\n")
    print(f"{rose.get_info()}", end="")
    rose.bloom()

    print(f"{oak.get_info()}", end="")

    print(f"{tomato.get_info()}", end="")


if __name__ == "__main__":
    main()
