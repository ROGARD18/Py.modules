import random


class Players:
    """
    Class Players for different random player who will have event.
    """
    def __init__(self, name: str, level: int):
        """
        Init object Player with:

        - param name: player's name
        - param level: player's level
        """
        self.name = name
        self.level = level

    def ft_levelup(self) -> None:
        """
        Update player's level when he has levelup event.
        """
        self.level += 1

    def return_info(self) -> str:
        """
        Use to return all player's data
        :rtype: str
        """
        return (f"Player {self.name} (level {self.level})")


class Events:
    """
    Class for events.
    """
    events_dict: dict = {}
    total_event: int = 0

    def __init__(self, name: str):
        """
        Init Event object with:

        - param name : event's name
        """
        self.name: str = name
        self.total_event += 1

        if (self.name in self.events_dict):
            self.events_dict[self.name] += 1
        else:
            self.events_dict.update({self.name: 1})

    def return_event_name(self) -> str:
        """Use to return the event's name"""
        return (self.name)

    @classmethod
    def get_events_dict(cls) -> dict:
        """
        Getter to have all event's infos

        :param cls: Class Events
        """
        return cls.events_dict

    def __repr__(self) -> str:

        return self.name


def events_generators(n: int):
    """
    Generate n events.
    """
    players: list = [
        ["Alice", 25],
        ["Bob", 200],
        ["Charlie", 5],
        ["Antoine", 80]
    ]
    players_list: list = []

    for info in players:
        player_loop = Players(*info)
        players_list.append(player_loop)

    events_list: list = ["kill_monster", "found_treasure", "levelup"]

    for i in range(n):
        event_index: int = random.randrange(len(events_list))
        event_name: str = events_list[event_index]
        player_index: str = random.randrange(len(players_list))
        event = Events(event_name)
        player = players_list[player_index]

        if (event == events_list[2]):
            player.ft_levelup()
        yield player.return_info() + f" {event.return_event_name()})"


def fibonacci_generator():
    """
    Fibonacci numbers generator.
    """

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_number_generator():
    """
    Prime numbers generator.
    """

    a = 2
    while True:
        is_prime: bool = True
        for i in range(2, a - 1):
            if (a % i == 0):
                is_prime = False
                break
        if is_prime:
            yield a
        a += 1


def main() -> None:
    """
    All tests on the generators:
    - fibonacci
    - event
    - prime
    """
    n: int = 1000
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {n} game events...\n")

    gen_event = events_generators(n)
    for i in range(n):
        if (i < 3):
            print(next(gen_event))
        else:
            next(gen_event)
    print("...\n")

    print("=== Stream Analytics ===")

    print(f"Total events processed: {n}")
    print(Events.get_events_dict())
    print("")
    print("=== Generator Demonstration ===")

    fibonacci_list: list = []
    prime_list: list = []
    gen_fibonacci = fibonacci_generator()
    gen_prime = prime_number_generator()

    for _ in range(10):
        fibonacci_list.append(int(next(gen_fibonacci)))
    print(f"Fibonacci sequence (first 10): {fibonacci_list}")

    for _ in range(5):
        prime_list.append(int(next(gen_prime)))
    print(f"Prime numbers (first 5): {prime_list}")


if __name__ == "__main__":
    main()
