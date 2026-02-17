from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import choice


class Deck():
    def __init__(self, name: str):
        self.name = name
        self.cards_list: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards_list.append(card)

    def remove_card(self, card_name: str) -> None:
        print(card_name)
        for card in self.cards_list:
            if card_name is card.name:
                card_to_remove: Card = card
        self.cards_list.remove(card_to_remove)

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        drew_card = choice(self.cards_list)
        self.remove_card(drew_card.name)
        return drew_card

    def get_deck_stats(self) -> dict:
        cards_number: int = len(self.cards_list)
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        avg_cost: float = 0
        for card in self.cards_list:
            if isinstance(card, CreatureCard):
                creatures += 1
            if isinstance(card, ArtifactCard):
                artifacts += 1
            if isinstance(card, SpellCard):
                spells += 1
            avg_cost += card.cost
        avg_cost /= cards_number
        return {
            'total_cards': cards_number,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
