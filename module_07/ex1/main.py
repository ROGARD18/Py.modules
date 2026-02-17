from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck: Deck = Deck("Deck one")
    cards_list: list[Card] = [
        SpellCard("Lightning Bolt", 4, "Epic", "dommage"),
        ArtifactCard("Mana Crystal", 2, "Rare", 2,
                     "Permanent: +1 mana per turn"),
        CreatureCard("Fire Dragon", 6, "Legendary", 7, 5)
    ]
    lightning_bolt = cards_list[0]
    mana_crystal = cards_list[1]
    fire_dragon = cards_list[2]
    for card in cards_list:
        deck.add_card(card)
    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")

    game_state: dict = {
        'Cards_list': [fire_dragon, lightning_bolt, mana_crystal],
        'Cards_mana': {
            'Fire Dragon': 8,
            'Lightning Bolt': 4,
            'Mana Crystal': 4
        },
        'creature_effect': 'Creature summoned to battlefield'
    }
    for _ in range(len(deck.cards_list)):
        drew_card: Card = deck.draw_card()
        print(f"\nDrew: {drew_card.name} ({drew_card.__class__.__name__})")
        print("Play result:", drew_card.play(game_state))

    print("\nPolymorphism in action: Same interface, different card"
          "behaviors!")


if __name__ == "__main__":
    main()
