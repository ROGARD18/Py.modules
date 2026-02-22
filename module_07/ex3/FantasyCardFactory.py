from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Any
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.__creatures: dict[str, dict] = {
            "dragon": {
                "name": "Fire Dragon",
                "cost": 5,
                "rarity": "Legendary",
                "attack": 7,
                "health": 5
            },
            "goblin": {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": "Common",
                "attack": 2,
                "health": 1
            }
        }
        self.__spells: dict[str, dict] = {
            "fireball": {
                "name": "Fireball",
                "cost": 4,
                "rarity": "Uncommon",
                "effect_type": "damage"
            }
        }
        self.__artifacts: dict[str, dict] = {
            "mana_ring": {
                "name": "Mana Crystal",
                "cost": 2,
                "rarity": "Common",
                "durability": 5,
                "effect": "Permanent: +1 mana per turn"
            }
        }

        self.__supported_types: list[str] = [
            "creatures",
            "spells",
            "artifacts"
        ]

    @staticmethod
    def get_power(card: dict[str, Any], card_type: str) -> int:
        if card_type == "creature":
            return card["health"] + card["attack"] - card["cost"]
        elif card_type == "spell":
            return 5 - card["cost"]
        elif card_type == "artifact":
            return card["durability"] - card["cost"]
        raise ValueError(f"'{card_type}' is not a valid type")

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for creature_name, creature_data in self.__creatures.items():
                if creature_name == name_or_power:
                    return CreatureCard(creature_data["name"],
                                        creature_data["cost"],
                                        creature_data["rarity"],
                                        creature_data["attack"],
                                        creature_data["health"])
        elif isinstance(name_or_power, int):
            for _, creature_data in self.__creatures.items():
                if self.get_power(creature_data, "creature") == name_or_power:
                    return CreatureCard(creature_data["name"],
                                        creature_data["cost"],
                                        creature_data["rarity"],
                                        creature_data["attack"],
                                        creature_data["health"])
        raise ValueError(f"'{name_or_power}' is not valid for creature")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for spell_name, spell_data in self.__spells.items():
                if spell_name == name_or_power:
                    return SpellCard(spell_data["name"],
                                     spell_data["cost"],
                                     spell_data["rarity"],
                                     spell_data["effect_type"])
        elif isinstance(name_or_power, int):
            for _, spell_data in self.__spells.items():
                if self.get_power(spell_data, "spell") == name_or_power:
                    return SpellCard(spell_data["name"],
                                     spell_data["cost"],
                                     spell_data["rarity"],
                                     spell_data["effect_type"])
        raise ValueError(f"'{name_or_power}' is not valid for spell")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for artifact_name, artifact_data in self.__artifacts.items():
                if artifact_name == name_or_power:
                    return ArtifactCard(artifact_data["name"],
                                        artifact_data["cost"],
                                        artifact_data["rarity"],
                                        artifact_data["durability"],
                                        artifact_data["effect"])
        elif isinstance(name_or_power, int):
            for _, artifact_data in self.__artifacts.items():
                if self.get_power(artifact_data, "artifact") == name_or_power:
                    return ArtifactCard(artifact_data["name"],
                                        artifact_data["cost"],
                                        artifact_data["rarity"],
                                        artifact_data["durability"],
                                        artifact_data["effect"])
        raise ValueError(f"'{name_or_power}' is not valid for artifact")

    @staticmethod
    def random_card_name(keys: list[str], themed_deck: dict) -> str:
        keys_amount: int = len(keys)
        random_card_name: str = keys[random.randint(0, keys_amount - 1)]
        while themed_deck.get(random_card_name):
            keys.remove(random_card_name)
            keys_amount -= 1
            if keys_amount == 0:
                raise ValueError("can't generate deck, size is"
                                 " bigger than available cards")
            random_card_name = keys[random.randint(0, keys_amount - 1)]
        return random_card_name

    def random_type(self, themed_deck: dict) -> str:
        not_full: list[str] = []
        for type in self.__supported_types:
            is_full: bool = True
            for card_name in getattr(self,
                                     f"_FantasyCardFactory__{type}").keys():
                if not themed_deck.get(card_name):
                    is_full = False
                    break
            if not is_full:
                not_full.append(type)
        return not_full[random.randint(0, len(not_full) - 1)]

    def create_themed_deck(self, size: int) -> dict:
        if size <= 0:
            return {}
        themed_deck: dict = {}
        for _ in range(size):
            random_type: str = self.random_type(themed_deck)
            keys: list[str]
            random_card_name: str
            if random_type == "creatures":
                keys = list(self.__creatures.keys())
                random_card_name = self.random_card_name(keys,
                                                         themed_deck)
                themed_deck.update({random_card_name:
                                    self.create_creature(random_card_name)})
            elif random_type == "spells":
                keys = list(self.__spells.keys())
                random_card_name = self.random_card_name(keys,
                                                         themed_deck)
                themed_deck.update({random_card_name:
                                    self.create_spell(random_card_name)})
            elif random_type == "artifacts":
                keys = list(self.__artifacts.keys())
                random_card_name = self.random_card_name(keys,
                                                         themed_deck)
                themed_deck.update({random_card_name:
                                    self.create_artifact(random_card_name)})
        return themed_deck

    def get_supported_types(self) -> dict:
        return {
            name: list(getattr(self, f"_FantasyCardFactory__{name}").keys())
            for name in self.__supported_types
        }
