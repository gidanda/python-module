from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def casted(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return casted


def spell_sequence(spells: list[Callable]) -> Callable:
    def combo(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            result = spell(target, power)
            results.append(result)
        return results

    return combo


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


def heal(target: str, power: int) -> str:
    return f"Heal restores {power} HP to {target}"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} defense"


def enough_power(target: str, power: int) -> bool:
    return power >= 10


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print(combined_spell("Dragon", 15))

    print()

    print("Testing power amplifier...")
    strong_fireball = power_amplifier(fireball, 3)
    print(strong_fireball("Dragon", 10))

    print()

    print("Testing conditional caster...")
    safe_fireball = conditional_caster(enough_power, fireball)
    print(safe_fireball("Dragon", 15))
    print(safe_fireball("Dragon", 5))

    print()

    print("Testing spell sequence...")
    combo_spell = spell_sequence([fireball, heal, shield])
    for result in combo_spell("Dragon", 12):
        print(result)