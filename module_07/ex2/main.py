from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    card_methods = [method for method in dir(Card) if callable(
                    getattr(Card, method)) and not method.startswith("__")]
    combatable_methods = [method for method in dir(Combatable) if callable(
                    getattr(Combatable, method)) and not
                    method.startswith("__")]
    magical_methods = [method for method in dir(Magical) if callable(
                    getattr(Magical, method)) and not method.startswith("__")]

    arcane_warrior: EliteCard = EliteCard("Arcane Warrior", 5, "Legendary",
                                          5, "melee")
    enemy: EliteCard = EliteCard("Enemy", 3, "Epic", 2, "melee")
    enemy1: EliteCard = EliteCard("Enemy1", 2, "Rare", 2, "distance")
    enemy2: EliteCard = EliteCard("Enemy2", 2, "Rare", 2, "distance")

    game_state: dict = {
        'Enemy': enemy,
        'spell': 'Fireball',
        'targets': [enemy1, enemy2]
    }
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):")
    arcane_warrior.play(game_state)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
