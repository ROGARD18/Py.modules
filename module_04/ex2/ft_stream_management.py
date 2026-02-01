import sys


def print_to_stdout(string: str) -> None:
    """
    Use to print on channel stdout.
    """
    print(f"[STANDARD] {string}", file=sys.stdout)


def print_to_stderr(string: str) -> None:
    """
    Use to print on channel stderr.
    """
    print(f"[ALERT] {string}", file=sys.stderr)


def ft_stream_management() -> None:
    """
    Print messages on different chanel.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    user_id = input("Input Stream active. Enter archivist ID: ")
    print("Input Stream active. Enter status report: ", end="", flush=True)
    status = sys.stdin.readline().rstrip()
    print("")
    print_to_stdout(f"Archive status from {user_id}: {status}")
    print_to_stderr("System diagnostic: Communication channels verified")
    print_to_stdout("Data transmission complete")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
