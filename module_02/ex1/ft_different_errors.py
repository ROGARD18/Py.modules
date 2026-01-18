def garden_operations() -> None:
    try:
        int_try = int("abc")
        print("Good Value")
    except ValueError:
        print("Is not a valid number")
    try:
        int_try = 8 / 0
    except ZeroDivisionError:
        print(f"Imposible to divise {int_try} by 0")
    try:
        file = open("nofile.txt")
    except FileNotFoundError:
        print(f"{file} not found")
    dictionnaire = {"nom": "Alice", "age": 30}
    try:
        print(dictionnaire["ville"])
    except KeyError:
        print("'Ville' is not in the dictionnary")
    try:
        int_try = int("20")
        print("Good Value")
    except (ValueError, KeyError):
        print("Invalid number or not in dictionnary")


def test_error_types() -> None:
    garden_operations()
    print("The program continues running after each error")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
