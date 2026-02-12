import alchemy


def test_sacred_scroll() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    fire_string: str = "alchemy.elements.create_fire()"
    water_string: str = "alchemy.elements.create_water()"
    earth_string: str = "alchemy.elements.create_earth()"
    air_string: str = "alchemy.elements.create_air()"

    print(f"{fire_string}: {alchemy.elements.create_fire()}")
    print(f"{water_string}: {alchemy.elements.create_water()}")
    print(f"{earth_string}: {alchemy.elements.create_earth()}")
    print(f"{air_string}: {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")

    print("alchemy.create_fire(): ", end="")
    try:
        print(alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_water(): ", end="")
    try:
        print(alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_earth(): ", end="")
    try:
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_air(): ", end="")
    try:
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage MetaData:")
    print("Version:", alchemy.__version__)
    print(alchemy.__author__)


if __name__ == "__main__":
    test_sacred_scroll()
