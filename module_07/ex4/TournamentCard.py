from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCardAlreadyExists(Exception):
    pass


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, id: str,
                 rating: int, attack: int, hp: int) -> None:
        super().__init__(name, cost, rarity)
        if rating <= 0 or cost <= 0 or attack <= 0 or hp <= 0:
            raise ValueError("rating, cost, attack and hp"
                             "must be greater than 0")
        if not name.isprintable() or not id.isprintable():
            raise ValueError("name and id should be printable")
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = rating
        self.id: str = id
        self.attack_: int = attack
        self.hp: int = hp

    def play(self, game_state: dict) -> dict:
        total_attacks: int = 1
        attack: dict = self.attack(game_state["enemy"])
        while not attack["dead"]:
            attack = self.attack(game_state["enemy"])
            total_attacks += 1
        return {
            "total_attacks": total_attacks
        }

    def calculate_rating(self) -> int:
        self.rating += 16 * self.wins
        self.rating -= 16 * self.losses
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins = wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses = losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating
        }

    def attack(self, target: 'TournamentCard') -> dict:
        defense_res: dict = target.defend(self.attack_)
        return {
            "dead": defense_res["hp"] <= 0,
            "damage": self.attack_,
            "target_hp": defense_res["hp"]
        }

    def defend(self, incoming_damage: int) -> dict:
        old_hp: int = self.hp
        self.hp -= incoming_damage
        return {
            "damage_taken": incoming_damage,
            "old_hp": old_hp,
            "hp": self.hp
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_,
            "hp": self.hp
        }

    def get_tournament_stats(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
