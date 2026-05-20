def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()

    for item in allowed:
        if item in lowered:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
