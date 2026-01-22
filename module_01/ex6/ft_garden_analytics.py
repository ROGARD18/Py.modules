class Plant:
    def __init__(self, name: str, height: int):
        self.name: str = name
        self.height_start: int = height
        self.new_height: int = height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name=name, height=height)
        self.color: str = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: int, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize: int = prize


class GardenManager:
    garden_numbers: int = 0

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants_list: list = []
        self.garden_stats = self.GardenStats()

    class GardenStats:

        @staticmethod
        def get_plants_in_garden(plants_list: list[Plant]) -> None:
            print("Plants in garden :")
            for plant in plants_list:
                if isinstance(plant, PrizeFlower):
                    print(f"- {plant.name} : {plant.new_height}cm, ", end="")
                    print(f"{plant.color}, Prize points: {plant.prize}")
                elif isinstance(plant, FloweringPlant):
                    print(f"- {plant.name}: {plant.new_height}cm", end="")
                    print(f", {plant.color} flowers (bloomig)")
                else:
                    print(f"- {plant.name} : {plant.new_height}cm")

        @staticmethod
        def print_numbers_plant(plants_list: list) -> None:
            count_regular: int = 0
            count_flower: int = 0
            count_prize: int = 0
            count_tot: int = 00
            diff_height: int = 0
            for plant in plants_list:
                diff_height += plant.new_height - plant.height_start
                if isinstance(plant, PrizeFlower):
                    count_prize += 1
                elif isinstance(plant, FloweringPlant):
                    count_flower += 1
                else:
                    count_regular += 1
            count_tot = count_prize + count_flower + count_regular
            print(f"Plants added: {count_tot}, Total growth: {diff_height}cm")
            print(f"Plant types: {count_regular} regular", end="")
            print(f" {count_flower} flower, {count_prize} prize", end="")

        @staticmethod
        def all_stats(plants_list: list) -> None:
            GardenManager.GardenStats.get_plants_in_garden(plants_list)
            GardenManager.GardenStats.print_numbers_plant(plants_list)

    @staticmethod
    def check_height(height: int) -> bool:
        return height >= 0

    def add_plant(self, plant: Plant, plants_list: list) -> None:
        if GardenManager.check_height(plant.new_height):
            plants_list.append(plant)
            print(f"Added {plant.name} to {self.name}'s garden")
        else:
            print(f"\nCannot add {plant.name}: {plant.new_height} invalid\n")

    @classmethod
    def grow_all_plants(self, plants_list: list) -> None:
        for plant in plants_list:
            plant.new_height += 1


def main() -> None:
    # create plants
    print("=== Garden Management System Demo ===\n")
    Oak = Plant("Oak", 101)
    Rose = FloweringPlant("Rose", 26, "red")
    Sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    Alice = GardenManager("Alice")
    Alice.add_plant(Oak, Alice.plants_list)
    Alice.add_plant(Rose, Alice.plants_list)
    Alice.add_plant(Sunflower, Alice.plants_list)
    print("")
    Alice.grow_all_plants(Alice.plants_list)
    print("=== Alice's garden Report ===")
    Alice.GardenStats.all_stats(Alice.plants_list)


if __name__ == "__main__":
    main()
