class Plant:
    def __init__(self, name: str, starting_height: float, starting_age: int) -> None:
        self.name = name
        self.height = starting_height
        self.days = starting_age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")


plants_data = [
    {"name": "Rose", "height": 25.0, "days": 30},
    {"name": "Oak", "height": 200.0, "days": 365},
    {"name": "Cactus", "height": 5.0, "days": 90},
    {"name": "Sunflower", "height": 80.0, "days": 45},
    {"name": "Fern", "height": 15.0, "days": 120},
]


def main() -> None:
    print("=== Plant Factory Output ===")
    for data in plants_data:
        plant = Plant(data["name"], data["height"], data["days"])
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
