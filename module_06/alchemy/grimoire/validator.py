def validate_ingredients(ingredients: str) -> str:
    status: str = ("VALID" if "fire" and "water" and "earth" and "air"
                   in ingredients else "INVALID")
    return (f"{ingredients} - {status}")
