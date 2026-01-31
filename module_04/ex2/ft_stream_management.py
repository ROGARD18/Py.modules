import sys


def print_to_stdout(string: str) -> None:
    print("[STANDARD] ", string, file=sys.stdout)


def print_to_stderr(string: str) -> None:
    print("[ALERT] ", string, file=sys.stderr)


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

for line in sys.stdin[slice(2)]:
    print("Input: ")
    id = line

    # id: str = input("Input Stream active. Enter archivist ID: ")
    # status: str = input("Enter status report: ")
    print("")
    print_to_stdout(f"Archive status from {id}: {status}")


if __name__ == "__main__":
    ft_stream_management()
