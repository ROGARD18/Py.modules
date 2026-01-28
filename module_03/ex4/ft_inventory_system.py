import sys


def inventory_system() -> None:
    """Analyze inventory data from command line and categorize items."""

    print("=== Inventory System Analysis ===")
    inventory: dict = {}

    if len(sys.argv) <= 1:
        print("No args given ! Usage: python3 ft_inventory_system.py \
item: unit")
        return

    for arg in sys.argv[1:]:
        try:
            name, unit = arg.split(":")
            if (name in inventory):
                inventory[name] += int(unit)
            else:
                inventory[name] = int(unit)
        except ValueError as e:
            print(f"Error parsing '{arg}': {e}")
            return

    total_items: int = sum(inventory.values())

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===")

    for item, unit in inventory.items():
        percentage = (unit / total_items)
        print(f"{item}: {unit} units ({percentage:.1%})")

    print("\n=== Inventory Statistics ===")
    most_abundant: str = max(inventory, key=inventory.get)
    least_abundant: str = min(inventory, key=inventory.get)
    print(f"Most abundant: {most_abundant} \
({inventory.get(most_abundant)} units)")
    print(f"Least abundant: {least_abundant} \
({inventory.get(least_abundant)} units)")

    categories: dict = {"Moderate": {}, "Scarce": {}}
    for item, unit in inventory.items():
        if unit >= 5:
            categories["Moderate"][item] = unit
        else:
            categories["Scarce"][item] = unit

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    restock: list = []
    for item, unit in inventory.items():
        if unit <= 1:
            restock.append(item)
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary key: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    item_to_find: str = 'sword'
    print(f"Sample lookup - '{item_to_find}' in inventory: \
{item_to_find in inventory}")


if __name__ == "__main__":
    inventory_system()
