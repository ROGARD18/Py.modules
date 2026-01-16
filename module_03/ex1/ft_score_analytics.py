import sys


def player_analytics():
    n = len(sys.argv)
    print("== Player Score Analytics ===")
    if n == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return 0
    scores_list = []
    for i in range(1, n):
        scores_list.append(sys.argv[i])
    print(f"Scores processed: {scores_list}")
    print(f"Total players: {i}")
    total = 0
    for score in scores_list:
        total += int(score)
    print(f"Total score: {total}")


player_analytics()
