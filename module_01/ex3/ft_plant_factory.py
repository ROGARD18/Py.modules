class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def plant_factory() -> None:
    i = 0
    plant_list = [
        ["Rose", 25, 30],
        ["Sunflower", 80, 45],
        ["Cactus", 15, 120],
        ["Tulip", 10, 5],
        ["Lavender", 20, 15]
    ]
    print("=== Plant Factory Output ===")
    garden = []
    for info in plant_list:
        plant = Plant(info[0], info[1], info[2])
        garden.append(plant)
        i += 1

    for plant in garden:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print(f"Total plants created: {i}")


if __name__ == "__main__":
    plant_factory()
