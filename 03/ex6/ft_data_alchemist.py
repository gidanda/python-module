import random

players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]

def main() -> None:
    print("=== Game Data Alchemist ===\n")

    capitalized_players = [name.capitalize() for name in players]
    capitalized_only = [name for name in players if name[0].isupper()]
    score_dict = {
        name: random.randint(0, 1000)
        for name in capitalized_players
    }
    average = sum(score_dict.values()) / len(score_dict)
    high_scores = {
        name: score
        for name, score in score_dict.items()
        if score > average
    }

    print(f"Initial list of players: {players}\n")

    print(f"New list with all names capitalized: {capitalized_players}\n")

    print(f"New list of capitalized names only: {capitalized_only}\n")

    print(f"Score dict: {score_dict}\n")

    print(f"Score average is {round(average, 2)}")

    print(f"High scores: {high_scores}")

if __name__ == "__main__":
    main()
