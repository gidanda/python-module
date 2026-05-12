def validate_ingredients(ingredients: str):
    allowed = ["earth", "air", "fire", "water"]
    lowered = ingredients.lower()

    for item in allowed:
        if item in lowered:
            return f"{ingredients} - VALID"
        
    return f"{ingredients} - INVALID"