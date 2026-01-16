class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name=name, height=height, age=age)
        self.color = self.bloom(color)

    def bloom(self, color) -> None:
        self.color = color
        if self.color == "red":
            print(f"{super().name} is blooming beautifully!")
        elif self.color == "orange":
            print(f"{super().name} is blooming.")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = self.produce_shade(trunk_diameter)

    def produce_shade(self, trunk_diameter) -> None:
        self.trunk_dinameter = trunk_diameter
        print(f"{self.name} ({self.__class__.name__})")


class Vegetables(Plant):
    def __init__(
        self, name: str, height: int, age: int, harvest_season:
        int, nutritional_value
    ):

        super().__init__(name=name, height=height, age=age)

        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main() -> None:
    Oak = Tree("Oak", 500, 1825, 50)
    Oak.produce()


if __name__ == "__main__":
    main()
