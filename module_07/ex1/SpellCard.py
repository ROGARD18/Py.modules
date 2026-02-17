from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.effect_types = effect_type

    def play(self, game_state: dict) -> dict:
        cards_mana: dict = game_state.get('Cards_mana')
        if super().is_playable(cards_mana.get('Mana Crystal')):
            print("Playable: True")
            return {
                'card_played': self.name,
                'mana_used': 3,
                'effect': f'Deal 3 {self.effect_types} to target'
            }

    def resolve_effect(self, targets: list) -> dict:
        pass
