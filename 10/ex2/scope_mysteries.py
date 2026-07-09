from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def add_power(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def create_magic_item(item: str) -> str:
        return enchantment_type + " " + item

    return create_magic_item


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        if key in storage:
            return storage[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall,
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter1 = mage_counter()
    counter2 = mage_counter()
    print(counter1())
    print(counter1())
    print(counter2())

    print()

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(accumulator(20))
    print(accumulator(30))
    print(accumulator(50))

    print()

    print("Testing enchantment factory...")
    fire_enchantment = enchantment_factory("Flaming")
    ice_enchantment = enchantment_factory("Frozen")
    print(fire_enchantment("Sword"))
    print(ice_enchantment("Shield"))

    print()

    print("Testing memory vault...")
    vault = memory_vault()
    store = vault["store"]
    recall = vault["recall"]

    store("secret", 42)
    store("name", "Alex")

    print(recall("secret"))
    print(recall("name"))
    print(recall("unknown"))