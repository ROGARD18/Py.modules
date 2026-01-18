def print_garden_info() -> None:
    """Declaration of plant's variables"""
    name: str = "Rose"
    height: str = "25cm"
    age: str = "30 days"

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("=== End of Program ===")


if __name__ == "__main__":
    print_garden_info()
