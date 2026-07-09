def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Ancient Wand", "power": 70, "type": "wand"},
    ]

    mages = [
        {"name": "Alex", "power": 95, "element": "fire"},
        {"name": "Jordan", "power": 60, "element": "water"},
        {"name": "Riley", "power": 80, "element": "earth"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)")

    print()

    print("Testing power filter...")
    powerful_mages = power_filter(mages, 80)
    for mage in powerful_mages:
        print(f"{mage['name']} ({mage['power']} power)")

    print()

    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print()

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")