def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if (unit == "area"):
        unit = "square meters"
    elif (unit == "packets"):
        unit = "packet available"
    elif (unit == "grams"):
        unit = "grams total"
    else:
        unit = "Unknown unit type"
    print(f"{seed_type} seeds: {quantity} {unit}")


# ft_seed_inventory("carrot", 8, "fefef")
