import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            if "power" in kwargs:
                power = kwargs["power"]
            elif args:
                power = args[-1]
            else:
                return "Insufficient power for this spell"

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char == " "
            for char in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def broken_spell() -> str:
    raise RuntimeError("Spell exploded")


if __name__ == "__main__":
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print()

    print("Testing retrying spell...")
    print(broken_spell())

    print()

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))