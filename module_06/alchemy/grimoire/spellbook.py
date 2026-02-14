def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients as valid
    if "INVALID" in valid(ingredients):
        return (f"Spell rejected: {spell_name} ({valid(ingredients)})")
    else:
        return (f"Spell recorded: {spell_name} ({valid(ingredients)})")
