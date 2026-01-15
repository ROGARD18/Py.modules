def water_plants(plant_list):
    try:
        for plant in plant_list:
            try:
                if plant is None:
                    raise ValueError
                print(f"Watering {plant}")
            except ValueError:
                print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce"])
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])


def main():
    test_watering_system()


if __name__=="__main__":
    main()