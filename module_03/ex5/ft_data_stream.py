import random


class Players:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def ft_levelup(self) -> None:
        self.level += 1

    def print_player(self) -> str:
        return (f"Player {self.name} (level {self.level})")


class Events:
    events_dict: dict = {}
    total_event: int = 0

    def __init__(self, name: str):
        self.name: str = name
        self.total_event += 1
        if (self.name in self.events_dict):
            self.events_dict[self.name] += 1
        else:
            self.events_dict.update({self.name: 1})

    def print_event(self) -> str:
        return (self.name)

    @classmethod
    def get_events_dict(cls) -> dict:
        return cls.events_dict
    
    def __repr__(self) -> str:
        return self.name


def events_generators(n: int):
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
        index: int = random.randrange(len(events_list))
        name: str = events_list[index]
        player_index: str = random.randrange(len(players_list))
        event = Events(name)
        player_for_event = players_list[player_index]
        print(f".{event}.")
        if (event == events_list[2]):
            print(player_for_event.level)
            player_for_event.ft_levelup()
            print(player_for_event.level)
        yield player_for_event.print_player() + f" {event.print_event()})"


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_number_generator():
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
