import sys
import typing

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename)
        content = file.read()
        print("---")
        print(content)
        print("---")
        file.close()
        print(f"File '{filename}' closed.")

    except Exception as error:
        print(f"Error opening file '{filename}': {error}")

if __name__ == "__main__":
    main()
