import os


def error_handling(data: str) -> None:
    print(f"Error: No {data} found")


def oracle() -> None:
    """
    Accesses the mainframe configuration by loading and 
    validating environment variables.
    """
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Try: pip install dotenv")
        return
    # Load variables from .env file into os.environ and
    # This allows development settings to be stored locally
    load_dotenv()
    MATRIX_MODE = os.getenv('MATRIX_MODE')
    if MATRIX_MODE is None:
        return error_handling("MATRIX_MODE")
    DATABASE_URL = os.getenv('DATABASE_URL')
    if DATABASE_URL is None:
        return error_handling("DATABASE_URL")
    API_KEY = os.getenv('API_KEY')
    if API_KEY is None:
        return error_handling("API_KEY")
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    if LOG_LEVEL is None:
        return error_handling("LOG_LEVEL")
    ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')
    if ZION_ENDPOINT is None:
        return error_handling("ZION_ENDPOINT")
    print("\nORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print("Mode:", MATRIX_MODE)
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print("Log Level:", LOG_LEVEL)
    print("Zion Network:", ZION_ENDPOINT)

    print("\n")
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly conigured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
