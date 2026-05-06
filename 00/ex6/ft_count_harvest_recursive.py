def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def helper(day: int, max_day: int) -> None:
        if day > max_day:
            return
        print(f"Day {day}")
        helper(day + 1, max_day)

    helper(1, days)
    print("Harvest time!")
