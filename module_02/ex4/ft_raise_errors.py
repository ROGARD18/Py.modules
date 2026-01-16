def check_plant_health(plant_name, water_level, sunlight_hours) -> None:
    try:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
        if water_level > 10 or water_level < 1:
            raise ValueError("Error : Water level is not valid")
        if sunlight_hours > 12 or sunlight_hours < 2:
            raise ValueError("Error : Sunlight_hours is not valid")
        print("SUCCESS : everything ok")
    except Exception as e:
        print(f"{e}")

def test_plant_checks() -> None:
    check_plant_health("rose", 5, 5)
    check_plant_health("", -1, -1)
    check_plant_health("rose", -1, 3)
    check_plant_health("rose", 1, -1)


def main() -> None:
    test_plant_checks()


if __name__=="__main__":
    main()