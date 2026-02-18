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
    
    game_state: dict = {
        
    }

    print("\n=== DataDeck Ability System ===\n")

    print(card_methods)
    print("EliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    arcane_warrior: EliteCard = EliteCard("arcane_warrior", 5, "Legendary", 5, "melee")
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    arcane_warrior.play(game_state)


if __name__ == "__main__":
    main()
