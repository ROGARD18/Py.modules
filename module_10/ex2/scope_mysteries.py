from typing import Any


def mage_counter() -> callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator (start with 1)...")
    accumulator = spell_accumulator(1)
    print(f"Call 1 (+5): {accumulator(5)}")
    print(f"Call 2 (+10): {accumulator(10)}")
    print(f"Call 3 (-6): {accumulator(-6)}")

    print("\nTesting enchantment factory...")
    fire_factory = enchantment_factory("Flaming")
    ice_factory = enchantment_factory("Frozen")
    print(fire_factory("Sword"))
    print(ice_factory("Shield"))

    print("\nTesting memory vault...")
    storage = memory_vault()
    storage['store']("password_antoine", "Antoinerogard01578")
    storage['store']("password_pierre", "PierreDupont145632")
    print(f"password_antoine: {storage['recall']('password_antoine')}")
    print(f"password_pierre: {storage['recall']('password_pierre')}")
    print(f"password_emma: {storage['recall']('password_emma')}")


if __name__ == "__main__":
    main()
