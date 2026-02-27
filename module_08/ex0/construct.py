import site
import os
import sys


def ft_construct() -> None:
    """
    Detects the current Python environment and provides instructions
    to enter the virtual 'construct'.
    """
    # VIRTUAL_ENV is an environment variable set by the activation script of a venv
    if 'VIRTUAL_ENV' not in os.environ:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")

        print("\nThen run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix)

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\nthe global system")

        print("\nPackage installation path:")
        # site.getsitepackages() returns the location where modules are installed
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    ft_construct()
