import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def show_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("\nThen run this program again.")


def show_inside_construct() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(site.getsitepackages()[0])


def  main() -> None:
    if is_virtual_env():
        show_inside_construct()
    else:
        show_outside_matrix()


if __name__ == "__main__":
    main()