from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        cards_mana: dict = game_state.get('Cards_mana')
        if super().is_playable(cards_mana.get('Lightning Bolt')):
            print("Playable: True")
            return {
                'card_played': self.name,
                'mana_used': self.durability,
                'effect': self.effect
            }

    def activate_ability(self) -> dict:
        pass
