import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    elif operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    result: dict[str, Callable] = {}

    fire_enchanter = functools.partial(base_enchantment, 50, "fire")
    ice_enchanter = functools.partial(base_enchantment, 50, "ice")
    lightning_enchanter = functools.partial(base_enchantment, 50, "lightning")
    result["fire"] = fire_enchanter
    result["ice"] = ice_enchanter
    result["lightning"] = lightning_enchanter

    return result


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    

def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(value: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @cast.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @cast.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment on {target} with {power} power"


if __name__ == "__main__":
    print("Testing spell reducer...")
    spell_powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")

    print()

    print("Testing partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))
    print(enchanters["lightning"]("Staff"))

    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "wind"]))
    print(dispatcher(3.14))