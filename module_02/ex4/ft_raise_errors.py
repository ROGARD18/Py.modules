def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> None:
    """
    checker of plant, test name empty, waterlevel > 10 < 1 and sun > 12 < 2.


    Raises:
        ValueError: Error if a condition is false
    """
    try:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
        if water_level > 10 or water_level < 1:
            raise ValueError(f"Error : Water level {water_level} \
is too high (max 10)")
        if sunlight_hours > 12 or sunlight_hours < 2:
            raise ValueError(f"Error : Sunlight hours {sunlight_hours} \
is too low (min 2)")
        print(f"Plant '{plant_name} is healthy!")
    except Exception as e:
        print(f"{e}")


def test_plant_checks() -> None:
    """Tester function, test check_plant_health.
    """
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    check_plant_health("rose", 5, 5)

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 5)

    print("\nTesting bad water level...")
    check_plant_health("rose", -1, 3)

    print("\nTesting bad sunlight hours...")
    check_plant_health("rose", 1, -1)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
