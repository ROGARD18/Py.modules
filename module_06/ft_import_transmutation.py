import alchemy
from alchemy.elements import create_water
from alchemy.elements import create_earth, create_fire
from alchemy.potions import healing_potion as heal
from alchemy.potions import strenght_potion as strength


def transmutation_mastery() -> None:
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())

    print("\nMethod 2 - Specific function import:")
    print("create_water():", create_water())

    print("\nMethod 3 - Aliased import:")
    print("heal():", heal())

    print("\nMethod 4 - Multiple imports:")
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength())

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    transmutation_mastery()
