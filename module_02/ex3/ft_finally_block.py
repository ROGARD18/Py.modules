def water_plants(plant_list) -> None:
    try:
        for plant in plant_list:
            print("Watering" + plant)
    except Exception as e:
        print(f"Error: Cannot water {plant} - invalid plant! {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce"])
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
