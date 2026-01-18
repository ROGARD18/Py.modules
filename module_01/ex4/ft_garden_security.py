class SecurePlant:
    """New class represents a plant with infos are secures"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, private height and private age"""
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value) -> None:
        """Initialise the height with valid height"""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value

    def set_age(self, value) -> None:
        """Initialise the age with valid age"""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value

    def get_height(self) -> int:
        """Provide safe access to the private height attribute."""
        return self.__height

    def get_age(self) -> int:
        """Provide safe access to the private age attribute."""
        return self.__age


def main() -> None:
    """Test the security system with both valid and invalid data."""
    rose = SecurePlant("Rose", -500, 30)
    rose.set_height(-5)
    rose.set_height(8)
    rose.__height = 10
    print(
        f"Current plant: {rose.name} ({rose.get_height()}cm, "
        f"{rose.get_age()} days)"
    )


if __name__ == "__main__":
    main()
