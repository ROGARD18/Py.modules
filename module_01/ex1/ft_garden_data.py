class Plant:
    """Class represents a plant with a name, a height and an age.
    Within a fonction:
    - print_plant(): use to print plant's datas.
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

    def __repr__(self) -> None:
        """The special __repr__ method allows you to specify a character
        string that serves as a representation of a class"""
        return (f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """
    Test creation of plant and test to display her infos
    """

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(rose)
    print(sunflower)
    print(cactus)


if __name__ == "__main__":
    main()
