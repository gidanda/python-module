from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    lowered = ingredients.lower()

    for item in allowed:
        if item in lowered:
            return f"{ingredients} - VALID"
        
    return f"{ingredients} - INVALID"