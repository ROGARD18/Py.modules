class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
            self.__height = -1
            return -1
        else:
            self.__height = value
            return value

    def set_age(self, value):

        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
            self.__height
            return -1
        else:
            self.__age = value
            return value

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


def main() -> None:
    Rose = SecurePlant("Rose", -500, 30)
    if Rose.get_height() >= 0 & Rose.get_age() >= 0:
        print(f"Height updated: {Rose.get_height()}cm [OK]")
        print(f"age updated: {Rose.get_age()} days [OK]")


if __name__ == "__main__":
    main()
