class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def growing(self, growth: int) -> None:
        self.height += growth

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def week_effect(self, growth: int) -> None:
        for i in range(1, 8):
            self.growing(growth)
            self.aging()


def main() -> None:
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    print("=== Day 1 ===")
    Rose.get_info()
    Rose.week_effect(2)
    Sunflower.get_info()
    Sunflower.week_effect(1)
    Cactus.get_info()
    Cactus.week_effect(3)
    print("=== Day 7 ===")
    Rose.get_info()
    Sunflower.get_info()
    Cactus.get_info()


if __name__ == "__main__":
    main()
