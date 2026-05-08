class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0
        self.age = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

plants_data = [
    {"name": "Rose", "height": 25, "age": 30},
    {"name": "Sunflower", "height": 80, "age": 45},
    {"name": "Cactus", "height": 15, "age": 120},
]

def main() -> None:
    print("=== Garden Plant Registry ===")

    for data in plants_data:
        plant = Plant()
        plant.name = data["name"]
        plant.height = data["height"]
        plant.age = data["age"]
        plant.show()

if __name__ == "__main__":
    main()
