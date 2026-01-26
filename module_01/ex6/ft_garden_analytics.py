class Plant:
    """Class represents a plant with a name, a height and an age."""

    def __init__(self, name: str, height: int):
        """
        Init plant's data with args.

        Args:
            name (str): Plant's name
            height (int): Plant's height
        """

        self.name: str = name
        self.height_start: int = height
        self.new_height: int = height


class FloweringPlant(Plant):
    """Class represents a plant's type with a color.

    Args:
        Plant : class super()
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Init plant's data with args.

        Args:
            name (str): flower's name
            height (int): flower's height
            color (str): flower's color
        """
        super().__init__(name=name, height=height)
        self.color: str = color


class PrizeFlower(FloweringPlant):
    """Class represents a FloweringPlant's type with a prize.

    Args:
        FloweringPlant : class super()
    """
    def __init__(self, name: int, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize: int = prize


class GardenManager:
    """Class use to stock all gardens possibles."""

    garden_numbers: int = 0
    garden_names: list = []

    def __init__(self, name: str) -> None:
        """
        Init garden with a name.

        Args:
            name (str): garden's name
        """
        self.name: str = name
        self.plants_list: list = []
        self.garden_stats = self.GardenStats()
        GardenManager.garden_numbers += 1
        GardenManager.garden_names.append(name)

    def get_plants_in_garden(self) -> None:
        """
        Use to print all plants and their datas.

        Args:
            plants_list (list[Plant]): all plants who will be printed
        """
        print("Plants in garden :")
        for plant in self.plants_list:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name} : {plant.new_height}cm, ", end="")
                print(f"{plant.color} flowers, Prize points: {plant.prize}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.new_height}cm", end="")
                print(f", {plant.color} flowers (bloomig)")
            else:
                print(f"- {plant.name} : {plant.new_height}cm")
        print("")

    class GardenStats:
        """Class use to stock all stats for a garden.
        All garden have his stats independently of others"""

        @staticmethod
        def print_numbers_plant(plants_list: list) -> None:
            """
            Use to print numbers of plants's types.

            Args:
                plants_list (list): all plants
            """
            count_regular: int = 0
            count_flower: int = 0
            count_prize: int = 0
            count_tot: int = 0
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
            print(f" {count_flower} flower, {count_prize} prize")

    @staticmethod
    def check_height(height: int) -> bool:
        """
        Use to check if the height of a plant is correct.

        Args:
            height (int): height that is checked.

        Returns:
            bool: height valide or not
        """
        return height >= 0

    def add_plant(self, plant: Plant) -> None:
        """
        Function used to add a plant in a garden

        Args:
            plant (Plant): plant that is add
        """
        check = GardenManager.check_height(plant.new_height)
        if check:
            self.plants_list.append(plant)
            print(f"---->>> Height validation test: {check}")
            print(f"Added {plant.name} to {self.name}'s garden")
        else:
            print("---->>> Height validation test: False")
            print(f"\nCannot add {plant.name}: {plant.new_height} invalid\n")

    def grow_all_plants(self) -> None:
        """
        Use to grow all plants of a garden.

        Args:
            plants_list (list): all plants that grow
        """
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants_list:
            print(f"{plant.name} grew 1cm")
            plant.new_height += 1
        print("")

    @classmethod
    def create_garden_network(cls) -> int:
        return (cls.garden_numbers)

    @classmethod
    def print_score(cls) -> None:
        print("Garden scores -", end="")
        for i in range(0, len(cls.garden_names)):
            print(f" {cls.garden_names[i]}: 100", end="")
        print("")


def main() -> None:
    """
    Function where we create a garden manager
    and where we test all functionalities of the manager.
    """
    print("=== Garden Management System Demo ===\n")
    oak = Plant("Oak", 101)
    rose = FloweringPlant("Rose", 26, "red")
    sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")
    bob.add_plant(oak)
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print("")
    alice.grow_all_plants()
    print("=== Alice's garden Report ===")
    alice.get_plants_in_garden()
    alice.GardenStats.print_numbers_plant(alice.plants_list)
    print("")
    GardenManager.print_score()
    print("Total gardens managed:", end="")
    print(f" {GardenManager.create_garden_network()}")


if __name__ == "__main__":
    main()
