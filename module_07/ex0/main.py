from ex0.CreatureCard import CreatureCard


def main() -> None:
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 3, "Epic", 3, 7)
    game_state: dict = {
        'Cards_list': [fire_dragon, goblin_warrior],
        'Cards_mana': {
            'Fire Dragon': 8,
            'Goblin Warrior': 4
        },
        'effect': 'Creature summoned to battlefield'
    }

    print("\n===DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Play result:", fire_dragon.play(game_state))

    cards_mana: dict = game_state.get('Cards_mana')
    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_dragon.attack_target(goblin_warrior))
    fire_dragon_mana: int = cards_mana.get('Fire Dragon')
    fire_dragon_mana -= fire_dragon.attack - 2

    print(f"\nTesting insufficient mana ({fire_dragon_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(fire_dragon_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
