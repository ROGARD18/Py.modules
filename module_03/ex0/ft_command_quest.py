import sys


def take_args():
    n = len(sys.argv)
    print("=== Command Quest ===")
    if n == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print("Total arguments: 1")
        return 0
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments receveid: {n - 1}")
    for i in range(1, n):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {n}")


take_args()
