import importlib


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


def analyze_matrix_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    rng = np.random.default_rng(42)
    data = rng.normal(loc=50, scale=10, size=1000)

    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame({
        "signal_strength": data,
    })

    average = df["signal_strength"].mean()
    maximum = df["signal_strength"].max()
    minimum = df["signal_strength"].min()

    print(f"Average signal: {average:.2f}")
    print(f"Maximum signal: {maximum:.2f}")
    print(f"Minimum signal: {minimum:.2f}")

    print("Generating visualization...")

    plt.figure()
    plt.plot(df["signal_strength"])
    plt.title("Matrix Signal Strength")
    plt.xlabel("Data point")
    plt.ylabel("Signal strength")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        print("\nSome dependencies are missing\n")
        print("Install with pip:")
        print("python -m pip install -r requirements.txt\n")
        print("Or install with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        return

    analyze_matrix_data()

    
if __name__ ==  "__main__":
    main()
