from operator import mul, add
from functools import reduce, partial, lru_cache, singledispatch
from time import time


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == 'min':
        return (reduce(min, spells))
    if operation == 'max':
        return (reduce(max, spells))
    if operation == 'add':
        return (reduce(add, spells))
    if operation == 'mul':
        return (reduce(mul, spells))
    else:
        return (-1)


def base_enchantment(power: int, element: str, target: str) -> str:
    return (f"{element} hits {power} to {target}")


def partial_enchanter(base_enchantment: callable
                      ) -> dict[str, callable]:
    fire_element: callable = partial(base_enchantment, element="fire",
                                     power=50)
    ice_element: callable = partial(base_enchantment, element="ice",
                                    power=50)
    lightning_elemen: callable = partial(base_enchantment, element="lightning",
                                         power=50)
    return {
        'fire_enchant': fire_element,
        'ice_enchant': ice_element,
        'lightning_enchant': lightning_elemen
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def not_memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return (not_memoized_fibonacci(n - 1) + not_memoized_fibonacci(n - 2))


@singledispatch
def spell_dispatcher() -> callable:
    pass


@spell_dispatcher.register(int)
def _1(x: int) -> str:
    return (f"Spell hits {x} damage")


@spell_dispatcher.register(str)
def _2(x: str) -> str:
    return (f"The spell is a {x}'s enchantment")


@spell_dispatcher.register(list)
def _3(x: list) -> str:
    spell_list: list = []
    for spell in x:
        spell_list.append(spell)
    return (f"List of spells is {spell_list}")


def main() -> None:

    print("\nTesting spell reducer...")
    test_powers = [30, 28, 23, 16]
    print(f"Sum: {spell_reducer(test_powers, 'add')}")
    print(f"Product: {spell_reducer(test_powers, 'mul')}")
    print(f"Max: {spell_reducer(test_powers, 'max')}")

    print("\nTesting partial enchanter...")
    base_enchant: dict[str, callable] = partial_enchanter(base_enchantment)
    fire_element: callable = base_enchant['fire_enchant']
    ice_element: callable = base_enchant['ice_enchant']
    lightning_element: callable = base_enchant['lightning_enchant']
    print(fire_element(target="enemy"))
    print(ice_element(target="enemy"))
    print(lightning_element(target="enemy"))

    print("\nTesting memoised fibonacci...")
    begin = time()
    print(f"Fib(10): {not_memoized_fibonacci(10)}")
    print(f"Fib(15): {not_memoized_fibonacci(15)}")
    end = time()
    print("Time taken to execute Fibonacci without lru_cache is", end-begin)

    begin = time()
    print(f"\nFib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    end = time()
    print("Time taken to execute Fibonacci with lru_cache is", end-begin)

    print("\nTesting spell dispatcher...")
    spell_list: list = ['flash', 'fireball', 'tornado', 'blizzard']
    print(f"Int: {spell_dispatcher(5)}")
    print(f"Str: {spell_dispatcher('lighting')}")
    print(f"List: {spell_dispatcher(spell_list)}")


if __name__ == "__main__":
    main()
