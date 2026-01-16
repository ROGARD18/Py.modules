class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def Print_plant(self) -> None:
    print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    Print_plant(Rose)
    Print_plant(Sunflower)
    Print_plant(Cactus)


if __name__ == "__main__":
    main()
