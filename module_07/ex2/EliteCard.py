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
        self.mana: int = 7

    def get_alive(self) -> bool:
        if self.life < 1:
            self.alive = False
            return False
        return self.alive

    def play(self, game_state: dict) -> dict:
        print("\nCombat phase:")
        Enemy: EliteCard = game_state.get('Enemy')
        print("Attack result:", self.attack(Enemy))
        print("Defense result:", self.defend(Enemy.damage))

        print("\nMagic Phase:")
        print("Spell cast:", self.cast_spell(game_state.get('spell'),
                                             game_state.get('targets')))
        print("Mana channel:", self.channel_mana(game_state.get('amount')))

    def attack(self, target: 'EliteCard') -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'domage_blocked': incoming_damage + 1,
            'still_alive': self.get_alive()
        }

    def get_combat_stats(self) -> dict:
        return {
            'attacker': self.name,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list['EliteCard']) -> dict:
        targets_name: list = []
        for target in targets:
            targets_name.append(target.name)
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets_name,
            'mana_used': self.damage - 1
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': self.mana - self.damage + 1,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'caster': self.name,
            'mana_used': self.damage - 1,
            'channeled': self.mana - self.damage + 1,
            'total_mana': self.mana
        }
