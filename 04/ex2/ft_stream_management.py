import sys
import typing

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    
    print("=== Cyber Archives Recovery & Preservation ===")
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
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {error}\n")
        return

    new_content = ""
    for line in content.splitlines():
        new_content += line + "#\n"

    print()
    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()
    if new_filename == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")
        try:
            output_file = open(new_filename, "w")
            output_file.write(new_content)
            output_file.close()
            print(f"Data saved in file '{new_filename}'.")
        except Exception as error:
            sys.stderr.write(f"[STDERR] Error opening file '{new_filename}': {error}\n")
            print("Data not saved.")



if __name__ == "__main__":
    main()
