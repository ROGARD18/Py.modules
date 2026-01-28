import sys
import math


def calculate_distance(point_one: tuple, point_two: tuple) -> float:
    """
    Use to calculate distance with this formule:
    - math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    :param point_one: start point (tuple)
    :param point_two: end point (tuple)
    :return: distance (float)
    """
    x1, y1, z1 = point_one
    x2, y2, z2 = point_two
    distance: float = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))

    return (round(distance, 2))


def coordinate_system() -> None:
    """
    System use calculate_distance between the two point gived in args.
    """

    n = len(sys.argv)
    if n != 4:
        print("no args")
        return

    coordinate: list = []
    for i in range(1, n):
        try:
            value: int = int(sys.argv[i])
        except Exception as e:
            print(f"Parsing invalid coordinates: {sys.argv[1:]}")
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {e.__class__.__name__}, \
Args: ('{e}')")
            return
        coordinate.append(value)
    print("== Game Coordinate System ===\n")

    point_zero: tuple = (10, 20, 5)
    point_one: tuple = (coordinate)
    point_two: tuple = (0, 0, 0)
    x1, y1, z1 = point_one
    x2, y2, z2 = point_two

    print("Position created: (10, 20, 5)")
    print(f"Distance between ({x2}, {y2}, {z2}) ", end="")
    distance: float = calculate_distance(point_zero, point_two)
    print(f"and (10, 20, 5): {distance}")

    print(f"\nParsing coordinates: {coordinate}")
    print("Parsed position: ", end="")
    print(f"({x1}, {y1}, {z1})")

    distance: float = calculate_distance(point_one, point_two)
    print(f"Distance between ({x2}, {y2}, {z2}) ", end="")
    print(f"and ({x1}, {y1}, {z1}): {distance} ")


if __name__ == "__main__":
    coordinate_system()
