__version__ = "1.0.0"

__author__ = "Master Phytonicus"

from .elements import create_fire, create_water


def main() -> None:
    create_fire()
    create_water()


if __name__ == "__main__":
    main()
