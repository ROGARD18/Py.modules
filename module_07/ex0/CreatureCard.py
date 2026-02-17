from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack = attack
        self.health = health
        self.type = 'Creature'

    def play(self, game_state: dict) -> dict:
        cards_mana: dict = game_state.get('Cards_mana')
        if super().is_playable(cards_mana.get('Fire Dragon')):
            print("Playable: True")
            return {
                'card_played': self.name,
                'mana_used': self.attack - 2,
                'creature_effect': {game_state.get('effect')}
            }

    def attack_target(self, target: 'CreatureCard') -> dict:
        return {
            'attacker': {self.name},
            'target': {target.name},
            'damage_dealt': self.attack,
            'combat_resolved': True if target.health <= self.attack else False
        }

    def get_card_info(self) -> dict:
        dict_res: dict = (super().get_card_info())
        dict_res.update({'type': self.type})
        dict_res.update({'attack': self.attack})
        dict_res.update({'health': self.health})
        return dict_res
