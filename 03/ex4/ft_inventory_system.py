import sys

def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    
    for arg in args:
        parts = arg.split(":")
        
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name = parts[0]
        item_quantity = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(item_quantity)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        inventory[item_name] = quantity
    
    return inventory



def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    item_count = len(inventory)
    print(f"Total quantity of the {item_count} items: {total}")

    for item in inventory:
        percentage = inventory[item] / total * 100
        print(f"Item {item} represents {round(percentage, 1)}%")

    most_item = ""
    most_quantity = 0
    least_item = ""
    least_quantity = 0

    first = True

    for item in inventory:
        quantity = inventory[item]

        if first:
            most_item = item
            most_quantity = quantity
            least_item = item
            least_quantity = quantity
            first = False
        else:
            if quantity > most_quantity:
                most_item = item
                most_quantity = quantity
            
            if quantity < least_quantity:
                least_item = item
                least_quantity = quantity

    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")
    
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
        main()
