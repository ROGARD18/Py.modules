import sys
import math


def calculate_distance(point1: tuple, point2: tuple) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance: float = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    return (distance)


def coordinate_system() -> None:
    n = len(sys.argv)
    if n != 4:
        return
    coordinate: list = []
    try:
        for i in range(1, n):
            try:
                value: int = int(sys.argv[i])
            except Exception as e:
                print(f"{e}")
                return
            coordinate.append(value)
    except Exception as e:
        print(f"{e}")
        return
    point1: tuple = (coordinate)
    print("Parsed position: ", end="")
    print(point1)
    x1, y1, z1 = point1
    point2: tuple = (0, 0, 0)
    x2, y2, z2 = point2
    distance: float = calculate_distance(point1, point2)
    print(f"Distance between ({x2}, {y2}, {z2}) ", end="")
    print(f"and ({x1}, {y1}, {z1}: --> {distance} <--")


if __name__ == "__main__":
    coordinate_system()
