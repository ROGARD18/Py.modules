from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.turns: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.__battlefield: list = []
        self.__hand: list = []
        self.__factory: CardFactory | None
        self.__strategy: GameStrategy | None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:

        self.__factory = factory
        print(f"Factory: {type(self.__factory).__name__}")
        self.__strategy = strategy
        print(f"Strategy: {self.__strategy.get_strategy_name()}")

    @property
    def factory(self) -> CardFactory:
        if self.__factory is None:
            raise RuntimeError("Engine not configured. Call configure_engine()"
                               " first.")
        return self.__factory

    @property
    def strategy(self) -> GameStrategy:
        if self.__strategy is None:
            raise RuntimeError("Engine not configured. Call configure_engine()"
                               " first.")
        return self.__strategy

    def draw_hand(self, size: int = 3) -> None:
        if not self.__hand:
            themed_deck: dict = self.factory.create_themed_deck(size)
            for card in themed_deck.values():
                self.__hand.append(card)

    def add_to_battlefield(self, card) -> None:
        self.__battlefield.append(card)
        self.cards_created += 1

    def add_to_hand(self, card) -> None:
        self.__hand.append(card)

    def simulate_turn(self) -> dict:
        if self.__strategy is None or self.__factory is None:
            raise RuntimeError("Engine not configured. Call configure_engine()"
                               " first.")

        self.turns += 1
        print(f"Strategy: {self.__strategy.get_strategy_name()}")

        if not self.__hand:
            self.draw_hand()

        turn_result: dict = self.__strategy.execute_turn(
            self.__hand, self.__battlefield
        )
        self.cards_created += len(turn_result["cards_played"])
        self.total_damage += turn_result["damage_dealt"]
        return turn_result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": (type(self.__strategy).__name__
                              if self.__strategy else "None"),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
