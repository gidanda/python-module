class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0.0
        self.days = 0
        self.growth_rate = 0.0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days += 1

def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    rose.growth_rate = 0.8
    start_height = rose.height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age()
        rose.grow()
        rose.show()

    week_total_growth = rose.height - start_height
    print(f"Growth this week: {round(week_total_growth, 1)}cm")

if __name__ == "__main__":
        main()
    
