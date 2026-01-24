def inventory_system() -> None:
    inventory: dict = {
        "potion": 5,
        "armor": 3,
        "shield": 2,
        "sword": 1,
        "helmet": 1
    }
    tot_item: int = sum(inventory.values())
    size: int = len(inventory)
    print(f"Total items in inventory: {tot_item}")
    print(f"Unique item: {size}\n")

    print("=== Current Inventory ===")
    for item in inventory:
        pourcent: float = inventory.get(item) / tot_item
        print(f"{item}: {inventory.get(item)} units ({pourcent:.1%})")

    print("\n=== Inventory Statistics ===")
    max_i: int = max(inventory, key=inventory.get)
    min_i: int = min(inventory, key=inventory.get)
    print(f"Most abundant: {max_i} ({max(inventory.values())} units)")
    print(f"Least abundant: {min_i} ({min(inventory.values())} unit)")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory_system()


if __name__ == "__main__":
    main()
