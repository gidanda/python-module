import random

ACHIEVEMENTS = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder",
    ]

def gen_player_achievements() -> set[str]:
    count = random.randint(4, 8)
    selected = random.sample(ACHIEVEMENTS, count)
    return set(selected)

def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    players = [
        ("Alice", alice),
        ("Bob", bob),
        ("Charlie", charlie),
        ("Dylan", dylan),
    ]

    for name , achievements in players:
        print(f"Player {name}: {achievements}\n")
    
    common = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print(f"Common achievements: {common}\n")

    only_alice = alice.difference(bob).difference(charlie).difference(dylan)
    only_bob = bob.difference(alice).difference(charlie).difference(dylan)
    only_charlie = charlie.difference(alice).difference(bob).difference(dylan)
    only_dylan = dylan.difference(alice).difference(bob).difference(charlie)

    only = [
        ("Alice", only_alice),
        ("Bob", only_bob),
        ("Charlie", only_charlie),
        ("Dylan", only_dylan),
    ]

    for name, only_achievements in only:
        print(f"only {name} has: {only_achievements}")

    all_achievements = set(ACHIEVEMENTS)
    alice_missing = all_achievements.difference(alice)
    bob_missing = all_achievements.difference(bob)
    charlie_missing = all_achievements.difference(charlie)
    dylan_missing = all_achievements.difference(dylan)

    print(f"\nAlice is missing: {alice_missing}")
    print(f"\nBob is missing: {bob_missing}")
    print(f"\nCharlie is missing: {charlie_missing}")
    print(f"\nDylan is missing: {dylan_missing}")

if __name__ == "__main__":
    main()
