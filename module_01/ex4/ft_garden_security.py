class SecurePlant:
    """Class represents a plant with secures data"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Init all plant's data with args.

        Args:
            name (str): Plant's name
            height (int): Plant's height
            age (int): Plant's age
        """
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        if (height < 0 or age < 0):
            print(f"Invalid operation. Cannot create the plant {name}", end="")
            print(f", one or two invalid data : ({height}cm, {age})")
            return
        self.height = self.set_height(height)
        self.age = self.set_age(age)
        print(f"Plant created: {name}")
        print(f"Height updated: {self.__height}cm [OK]")
        print(f"Age updated: {self.__age} days [OK]\n")
        return

    def set_height(self, height) -> None:
        """Initialise the height with valid height"""
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def set_age(self, age) -> None:
        """Initialise the age with valid age"""
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def get_height(self) -> int:
        """Provide safe access to the private height attribute."""
        return self.__height

    def get_age(self) -> int:
        """Provide safe access to the private age attribute."""
        return self.__age


def main() -> None:
    """Test the security system with both valid and invalid data."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    # rose.set_height(8)
    rose.__height = 10
    if (rose.get_height() > 0):
        print(
            f"\nCurrent plant: {rose.name} ({rose.get_height()}cm, "
            f"{rose.get_age()} days)"
        )


if __name__ == "__main__":
    main()
