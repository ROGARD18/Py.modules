def spell_hit(attacker: str, target: str) -> str:
    return (f'{attacker} hits {target}')


def spell_heal(healed: str) -> str:
    return (f'Heals {healed}')


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return


def power_amplifier(base_spell: callable, multiplayer: int) -> callable:
    pass


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    test_values = [12, 9, 7]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    main()

