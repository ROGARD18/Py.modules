import sys


def player_analytics() -> None:
    """
    Function demonstrate multiple operations on a list.
    """
    n = len(sys.argv)
    print("== Player Score Analytics ===")
    if n == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return
    scores_list = []
    try:
        for i in range(1, n):
            scores_list.append(int(sys.argv[i]))
    except ValueError as e:
        print(f"Non-numeric values enter ! {e}")
        return
    max_int = max(scores_list)
    min_int = min(scores_list)
    sum_int = sum(scores_list)
    print(f"Scores processed: {scores_list}")
    print(f"Total players: {i}")
    print(f"Total score: {sum(scores_list)}")
    print(f"Average score: {sum_int / i}")
    print(f"High score: {max_int}")
    print(f"Low score: {min_int}")
    print(f"Score range: {max_int - min_int}")


if __name__ == "__main__":
    player_analytics()
