from functools import wraps
from typing import Any, Callable
from time import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper():
        print(f"Casting {wrapper.__name__}")
        begin = time()
        res = func()
        end = time()
        t = end-begin
        print(f"Spell completed in {t}")
        print("Result:", res)
        return func()
    return wrapper


@spell_timer
def fireball() -> str:
    return ("Fireball cast !")


def power_validator(min_power: int) -> Callable[..., Any]:
    @wraps
    def wrapper(func) -> str | None:
        @wraps
        def wrapper_bis(*args, **kwargs):
            return (func(*args, **kwargs) if args[2] > min_power else
                    "Insufficient power for this spell")
        return wrapper_bis
    return wrapper


def retry_spell(max_attemps: int) -> callable:
    def wrapper(func):
        def wrapper_bis(*args, **kwargs):
            attemps: int = 1
            print()
            try:
                func(*args, **kwargs)
            except Exception:
                while attemps <= max_attemps:
                    print(f"Spell failed, retrying {attemps}/{max_attemps}")
                    attemps += 1
        return wrapper_bis
    return wrapper


@retry_spell(5)
def ice_spell(mana: int) -> str:
    if mana > 2:
        raise Exception(f"Too much mana: {mana}")
    print("Ice spell successfully")


@retry_spell(5)
def earth_spell(mana: int) -> str:
    if mana > 3:
        raise Exception(f"Too much mana: {mana}")
    print("Earth spell successfully")


@retry_spell(5)
def air_spell(mana: int) -> str:
    if mana > 5:
        raise Exception(f"Too much mana: {mana}")
    print("Air spell successfully")


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (True if len(name) > 3 else False)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> int:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    mage = MageGuild()
    print("\nTesting spell timer...")
    fireball()

    print("\nTesting power validator...")
    print(mage.cast_spell("antoine", 9))

    print("\nTesting retry spell...")
    ice_spell(5)
    air_spell(5)
    earth_spell(5)


if __name__ == "__main__":
    main()
