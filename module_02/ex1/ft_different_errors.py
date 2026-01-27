def garden_operations(error: int) -> None:
    """Demonstration of multipes Error:
    - ValueError
    - ZeroDivisionError
    - FileNotFoundError
    - KeyError
    - multiple Error in one
    """
    if (error == 1):
        print("\nTesting ValueError...")
        value = int("abc")
        print(value)
    elif (error == 2):
        print("\nTesting ZeroDivisionErro...")
        value = 8 / 0
    elif (error == 3):
        print("\nTesting FileNotFoundError...")
        value = open("nofile.txt")
    elif (error == 4):
        dictionnaire = {"nom": "Alice", "age": 30}
        print("\nTesting KeyError...")
        print(dictionnaire["ville"])


def test_error_types() -> None:
    """Test garden_operations.
    """
    print("=== Garden Error Types Demo ===\n")
    for i in range(5):
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError) as e:
            print(f"Caught {e.__class__.__name__} {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
