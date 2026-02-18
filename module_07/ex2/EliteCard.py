from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, combat_type: str):
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.damage = damage
        self.combat_type = combat_type
        self.life: int = 10
        self.alive: bool = True

    def play(self, game_state: dict) -> dict:
        print("\nCombat phase:")
        print("Attack result:", self.attack(game_state.get('Ennemy')))
        print("Defense result:", self.defend(game_state.get('Ennemy')))

        print("\nDefense phase:")
        print("Spell cast:", self.cast_spell(game_state.get('spell'),
                                             game_state.get('targets')))
        print("Mana channel:", self.channel_mana(game_state.get('amount')))

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass
    
    def get_magic_stats(self) -> dict:
        pass