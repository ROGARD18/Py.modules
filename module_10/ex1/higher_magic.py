def fireball(target: str) -> str:
    return (f"fireball hits {target}")


def heal(target: str) -> str:
    return (f"{target} healed")


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return (
        lambda *args, **kwargs:
        (spell1(*args, **kwargs), spell2(*args, **kwargs))
        )


def base_spell(base_level: int) -> int:
    return (base_level)


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return (lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier)


def ft_condition(target: str) -> bool:
    return (True if target == 'dragon' else False)


def conditional_caster(condition: callable, spell: callable) -> callable:
    return (
        lambda *args, **kwargs: spell(*args, **kwargs)
        if condition(*args, **kwargs) else
        "Spell fizzled"
        )


def spell_sequence(spells: list[callable]) -> callable:
    return (
        lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]
    )


def main() -> None:
    print("\nTesting spell combiner...")
    sc = spell_combiner(fireball, heal)
    print(sc('dragon'))

    print("\nTesting power amplifier...")
    pa = power_amplifier(base_spell, 3)
    print(pa(5))

    print("\nTesting conditional caster...")
    ca = conditional_caster(ft_condition, fireball)
    print(ca('dragon'))
    print(ca(''))

    print("\nTesting spell sequence...")
    spell_list: list[callable] = [fireball, heal]
    sq = spell_sequence(spell_list)
    print(sq('dragon'))


if __name__ == '__main__':
    main()
