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

    def print_plant(self) -> None:
        """
        Fonction use to print plant's data.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """
    Test creation of plant and test to display her infos
    """

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.print_plant()
    sunflower.print_plant()
    cactus.print_plant()


if __name__ == "__main__":
    main()
