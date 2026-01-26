def check_temperature(arg: str) -> None:
    """
    Fonction who try to convert a string in int and
    check if it succes if the int value is valid

    Args:
        arg (str): string that we are trying to convert
    """
    print(f"Testing temperature: {arg}")
    try:
        int_temp = int(arg)
        if int_temp <= 40 and int_temp >= 0:
            print(f"Temperature {int_temp}°C is perfect for plant!")
        elif int_temp > 40:
            print(f"Error: {int_temp}°C is too hot for plants (max 40°C)")
        elif int_temp < 0:
            print(f"Error: {int_temp}°C is too cold for plants (min 0°C)")
    except Exception:
        print(f"Error: '{arg}' is not a valid number")


def test_temperature_input() -> None:
    """Fonction who test multiple valude or check_temperature
    """
    check_temperature("25")
    print("")
    check_temperature("abc")
    print("")
    check_temperature("100")
    print("")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
