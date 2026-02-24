def spell_hit(attacker: str, target: str) -> str:
    return (f'{attacker} hits {target}')


def spell_heal(healed: str) -> str:
    return (f'Heals {healed}')


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return (spell1 + ", " + spell2)


def power_amplifier(base_spell: callable, multiplayer: int) -> callable:
    pass


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass


def main() -> None:
    # test_values = [12, 9, 7]
    test_targets = ['Dragon', 'Fireball', 'Goblin', 'Wizard', 'Knight']
    spell1 = spell_hit(test_targets[1], test_targets[0])
    spell2 = spell_heal(test_targets[0])

    print("\nTesting spell combiner...")
    print(spell_combiner(spell1, spell2))

    print("\nTesting power amplifier...")
    print(power_amplifier)


if __name__ == "__main__":
    main()
