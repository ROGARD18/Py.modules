def print_garden_info() -> None:
    """Print all graden data: Plant of the garden and his data."""

    name: str = "Rose"
    height: str = "25cm"
    age: str = "30 days"

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    print_garden_info()
