def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def _count_recursive(day: int, max: int) -> None:
        print(f"Day: {day}")
        if (day == max):
            return
        _count_recursive(day + 1, max)
    _count_recursive(1, days)
    print("Harvest time!")


# ft_count_harvest_recursive()
