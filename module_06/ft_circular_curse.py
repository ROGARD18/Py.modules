from alchemy.grimoire.validator import validate_ingredients as valid
from alchemy.grimoire.spellbook import record_spell


def circular_curse() -> str:
    print("\n=== Circular Curse Breaking ===")

    print("Testing ingredients validation:")
    print("validate_ingredients('fire air'):", valid("fire air"))
    print("validate_ingredients('dragon scales'):", valid("dragon scales"))

    print("\nTesting spell recording with validation:")
    print("record_spell('Fireball', 'fire air'):",
          record_spell("Fireball", "fire air"))
    print("record_spell('Dark Magic', 'shadow'):",
          record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print("record_spell('Lighting', 'air'):", record_spell("Lightning", "air"))

    print("\nCircular depency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    circular_curse()
