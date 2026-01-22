class Plant:
    """
    New class represents a plant with a name, a height and an age.
    Class with 4 functions:
    - function who can grow the plant with increases the height,
    - function to ages the plant, same way as grow() with the age,
    - function use to return all plant's data to display it after.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Init all plant's data with args:
        Args:
            name (str): Plant's name
            height (int): Plant's height
            age (int): Plant's age
        """

        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth: int) -> None:
        """
        Increase plant's height by the growth value
        """
        self.height += growth

    def ages(self) -> None:
        """
        Increase plant's age by one day
        """
        self.age += 1

    def get_info(self) -> str:
        """
        Return a string with all plant's data
        """

        return f"{self.name}: {self.height}cm, {self.age} days old"

    def week_effect(self, growth: int) -> None:
        """
        function use to simulate a week on a plant to see effects of grow()
        and ages()
        """

        for i in range(1, 8):
            self.grow(growth)
            self.ages()


def main() -> None:
    """
    Test creation of plants, dysplays data, test to grow and ages
    plants and simulate a week on plant
    """

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose_growth = 2
    sunflower_growth = 1
    cactus_growth = 3
    print("=== Day 1 ===")
    print(f"{rose.get_info()}")
    print(f"{sunflower.get_info()}")
    print(f"{cactus.get_info()}")
    rose.week_effect(rose_growth)
    sunflower.week_effect(sunflower_growth)
    cactus.week_effect(cactus_growth)
    print("=== Day 7 ===")
    print(f"{rose.get_info()}")
    print(f"Growth this week: +{rose_growth}cm")
    print(f"{sunflower.get_info()}")
    print(f"Growth this week: +{sunflower_growth}cm")
    print(f"{cactus.get_info()}")
    print(f"Growth this week: +{cactus_growth}cm")


if __name__ == "__main__":
    main()
