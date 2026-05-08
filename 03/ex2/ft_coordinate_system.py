import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = text.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords: list[float] = []
        has_error = False

        for part in parts:
            cleaned = part.strip()
            try:
                coords.append(float(cleaned))
            except ValueError as error:
                print(f"Error on parameter '{cleaned}': {error}")
                has_error = True
                break
        if has_error:
            continue

        return (coords[0], coords[1], coords[2])
        
def main() -> None:
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {distance}")
    print()

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x2, y2, z2 = pos2
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    print(f"Distance between the 2 sets of coordinates: {distance}")
    print()

if __name__ == "__main__":
        main()
