import importlib
import sys

REQUIRED_PACKAGES = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
    ("matplotlib", "Visualization ready"),
]

def check_dependencies() ->bool:
    all_available = True

    print("Checking dependencies:")
    for package_name, message in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package_name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package_name} ({version}) - {message}")
        except ModuleNotFoundError:
            print(f"[MISSING] {package_name}")
            all_available = False

    return all_available

def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        print("Some dependencies are missing.")
        return
    
if __name__ ==  "__main__":
    main()
