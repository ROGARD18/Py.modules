from typing import Callable


def spell_hit(target: str) -> str:
    return f"hits {target}"


def spell_heal(target: str) -> str:
    return f"Heals {target}"


def damage_calculator(power: int) -> int:
    return power


def is_dragon(target: str) -> bool:
    return target == "Dragon"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return (
        lambda *args, **kwag: (spell1(*args, **kwag), spell2(*args, **kwag))
    )


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return wrapper


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda *args, **kwargs: [s(*args, **kwargs) for s in spells]


def main() -> None:
    print("--- Test du Higher Realm ---")

    combined = spell_combiner(spell_hit, spell_heal)
    print(f"Combiner (Dragon): {combined('dragon')}")

    mega_damage = power_amplifier(damage_calculator, 3)
    print(f"Amplifier (Base 10, x3): {mega_damage(10)}")

    dragon_only_spell = conditional_caster(is_dragon, spell_hit)
    print(f"Conditional (Dragon): {dragon_only_spell('Dragon')}")
    print(f"Conditional (Goblin): {dragon_only_spell('Goblin')}")

    sequence = spell_sequence([spell_hit, spell_heal])
    print(f"Sequence (Knight): {sequence('Knight')}")


if __name__ == "__main__":
    main()
