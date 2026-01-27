class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __repr__(self) -> None:
        """The special __repr__ method allows you to specify a character
        string that serves as a representation of a class"""
        return (f"{self.name} ({self.__class__.__name__}): {self.height}cm, \
{self.age} days old")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            sun: int) -> None:
        super().__init__(name=name, height=height, age=age)
        self.sun = sun

    def __repr__(self) -> str:
        """
        Use to return all plant vegetable data

        Returns:
            _type_: all infos of the vegetable
        """
        return (super().__repr__()
                + (f", sun: {str(self.sun)}"))


class Waterplant(Vegetable):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            sun: int,
            waterlevel: int) -> None:
        super().__init__(name=name, height=height, age=age, sun=sun)
        self.waterlevel = waterlevel

    def __repr__(self) -> str:
        """
        Use to return all plant waterplant data

        Returns:
            _type_: all infos of the waterplant
        """
        return (super().__repr__()
                + (f", sun: {str(self.sun)}")
                + f", waterlevel: {(self.waterlevel)} ")


class GardenManager:
    garden: list = []

    @staticmethod
    def plant_height(height) -> None:
        if (height < 1):
            raise ValueError("Height not valide for the plant!")

    @staticmethod
    def plant_name(name: str) -> None:
        if name == "":
            raise ValueError("Name cannot be empty!")

    @staticmethod
    def plant_age(age: int) -> None:
        if age > 10:
            raise PlantError("Age impossble to attibute: too old")
        elif age < 0:
            raise PlantError("Age impossble to attibute: 0 or negative")

    def add_plants(self, plant: Plant):
        for i in range(3):
            try:
                if (i == 0):
                    self.plant_name(plant.name)
                elif (i == 1):
                    self.plant_age(plant.age)
                elif (i == 2):
                    self.plant_height(plant.height)
            except (ValueError, PlantError) as e:
                print(f"Error adding plant: {e}")
        if (plant.name):
            self.garden.append(plant)
            print(f"Added {plant.name} successfully")

    def plant_watter(self, liters: int) -> None:
        if liters < 2:
            raise WaterError("Not enough water in the tank!")

    def water_plants(self, liters: int) -> None:
        try:
            print("")
            self.plant_watter(liters)
            print("Watering plants...")
            print("Opening watering system")
            for plant in self.garden:
                print(f"Watering {plant.name} - success")
                plant.height += liters / 2
        except WaterError as e:
            print(f"Error cannot open watering system : {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_sun(self, plant) -> None:
        if (plant.sun > 10):
            raise ValueError(f"{plant.name}'s sun: {plant.sun} is too hight (max 10)")

    def check_water_level(self, plant) -> None:
        if (type(plant) is Waterplant):
            if (plant.waterlevel > 15):
                raise ValueError(f"{plant.name}'s waterlevel: \
{plant.waterlevel} is too much (max 15)")

    def plant_health(self) -> None:
        print("\nChecking plant health...")
        for plant in self.garden:
            try:
                self.check_sun(plant)
                self.check_water_level(plant)
                print(plant, "- healthy")
            except ValueError as e:
                print(e)


def init_plants_list(plants_list: list) -> list[Plant]:
    plants_list_final: list[Plant] = []
    for info in plants_list:
        if (len(info) == 3):
            plants_list_final.append(Plant(*info))
        elif (len(info) == 4):
            plants_list_final.append(Vegetable(*info))
        elif (len(info) == 5):
            plants_list_final.append(Waterplant(*info))
    return plants_list_final


def main() -> None:
    print("=== Garden Management System ===\n")
    plant_list: list[list] = [
        ["tomato", 4, 5, 1],
        ["lettuce", 1, 6, 2, 10],
        ["", 5, 4]
    ]
    plants_list: list[Plant] = init_plants_list(plant_list)
    Manager = GardenManager()
    print("Adding plants to garden...")
    for plant in plants_list:
        Manager.add_plants(plant)
    Manager.water_plants(2)
    Manager.plant_health()

    print("\nTesting error recovery...\n")
    plant_list_error: list[list] = [
        ["tomato", 4, 5, 1],
        ["lettuce", 1, 6, 2, 17]
    ]
    plants_list_error: list[Plant] = init_plants_list(plant_list_error)
    Manager_bis = GardenManager()
    for plant in plants_list_error:
        Manager_bis.add_plants(plant)
    Manager_bis.water_plants(1)
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")

if __name__ == "__main__":
    main()
