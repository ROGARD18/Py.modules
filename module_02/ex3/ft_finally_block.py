def water_plants(plant_list) -> None:
    """Waters all plants in the list if possible."""
    print("Opening watering system")
    for plant in plant_list:
        print("Watering " + plant)
    print("Watering completed successfully!")


def test_watering_system() -> None:
    """Test water_plants."""
    print("=== Garden Watering System ===\n")
    plants_list: list = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    try:
        print("Testing normal watering...")
        water_plants(plants_list)
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    try:
        print("\nTesting with error...")
        water_plants(["tomato", None, "carrots"])
    except Exception as e:
        print(e, "- invalid plant")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    test_watering_system()
