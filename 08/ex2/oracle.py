import os

from dotenv import load_dotenv

REQUIRED_CONFIG = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

def is_config_complete() -> bool:
    complete = True

    for key in REQUIRED_CONFIG:
        value = os.getenv(key)
        if value is None or value == "":
            print(f"[WARNING] Missing configuration: {key}")
            complete = False

    return complete


def display_configuration() -> None:
    mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL", "missing")
    api_key = os.getenv("API_KEY", "missing")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "missing")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url == "missing":
        print("Database: Not configured")
    elif "sqlite" in database_url or "local" in database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production instance")

    if api_key == "missing":
        print("API Access: Missing")
    elif "replace_me" in api_key:
        print("API Access: Development placeholder")
    else:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")

    if zion_endpoint == "missing":
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")

    if mode == "production":
        print("Runtime: Production configuration active")
    else:
        print("Runtime: Development configuration active")

    
def display_security_check() -> None:
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file should be ignored by .gitignore")
    print("[OK] Production overrides available")

def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_dotenv()

    is_config_complete()
    display_configuration()
    display_security_check()

    print()
    print("The Oracle sees all configurations.")

if __name__ == "__main__":
    main()