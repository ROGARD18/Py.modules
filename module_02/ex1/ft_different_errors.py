def garden_operations() -> None:
    """Demonstration of multipes Error:
    - ValueError
    - ZeroDivisionError
    - FileNotFoundError
    - KeyError
    - multiple Error in one
    """
    print("\nTesting ValueError...")
    try:
        value = int("abc")
        print(value)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("\nTesting ZeroDivisionErro...")
    try:
        value = 8 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("\nTesting FileNotFoundError...")
    try:
        value = open("nofile.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    dictionnaire = {"nom": "Alice", "age": 30}
    print("\nTesting KeyError...")
    try:
        print(dictionnaire["ville"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print("\nTesting multiple errors together...")
    try:
        value = int("ac")
        print(dictionnaire["ville"])
    except (ValueError, KeyError) as e:
        print(f"Caught an error: {e}, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
