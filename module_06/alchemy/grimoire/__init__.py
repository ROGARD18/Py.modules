from .spellbook import record_spell
from .validator import validate_ingredients


def main() -> None:
    record_spell()
    validate_ingredients()


if __name__ == "__main__":
    main()
