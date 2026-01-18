class Plant:
    def __init__(self, name: str, height: int):


class GardenManager:

    def __init__(self, name: str):
        self.name: str = name
        self.plants_list: list = []

    class GardenStats:

        def get_plants_number(self) -> int:
            plants_number = 0
            for plant in self.plants_list:
                if isinstance(plant, PrizeFlower):
                    prize_count += 1
                elif isinstance(plant, FloweringPlant):
                    flowering_count += 1
                else:
                    regular_count += 1
                plants_number += 1
            return (plants_number)
        