def analytics_dashboard() -> None:
    """
    Desmontrate all knowledge of list's comprehension, set's comprehension
    and dictionary's comprehension.
    """
    print("== Game Analytics Dashboard ===\n")

    players_dict: dict = {
        "alice": {
            "score": 2300,
            "achievements": [
                'kill_monster',
                'kill_monster',
                'level_2',
                'level_5',
                'first_kill',
                'second_kill',
                'heroic',
                'level_up']
        },
        "bob": {
            "score": 1800,
            "achievements": [
                'level_2',
                'level_5',
                'level_10',
                'level_up',
                'boss_slayer']
        },
        "charlie": {
            "score": 2150,
            "achievements": [
                'level_2',
                'level_5',
                'kill_monster',
                'kill_monster',
                'kill_monster',
                'level_up',
                'heroic']
        },
        "diana": {
            "score": 2050,
            "achievements": [
                'kill_monster',
                'kill_monster',
                'level_2',
                'level_5',
                'heroic',
                'level_up']
        },
        "charotte": {
            "score": 200,
            "achievements": [
                "level_2",
                'kill_monster',]
        }
    }
    print("=== List Comprehension Examples ===")

    players_list: list = [player for player, infos in players_dict.items()
                          if infos.get("score") > 2000]

    print("High scorers (>2000): ", players_list)

    score_doubled: list = [(infos.get("score") * 2) for player, infos in
                           players_dict.items()]

    print("Scores doubled:", score_doubled)

    active_players: list = [player for player, infos in players_dict.items()
                            if infos.get("score") > 500]

    print("Active players:", active_players)

    print("\n=== Dict Comprehension Examples ===")

    players_scores: dict = {player: infos.get("score") for player, infos
                            in players_dict.items()}

    print("Players scores: ", players_scores)

    players_counts_achi: dict = {player: len(infos.get('achievements')) for
                                 player, infos in players_dict.items()}

    print("Achievements counts: ", players_counts_achi)

    print("\n=== Set Comprehension Examples ===")
    players_demo: list = ["alice", "alice", "bob", "charlie", "bob", "bob"]
    unique_achievements: set = {
        achievements for user, infos in players_dict.items()
        for achievements in infos.get("achievements")
        if all(achievements not in infos_bis.get("achievements") for user_bis,
               infos_bis in players_dict.items() if user != user_bis)
    }
    players_unique: set = {player for player in players_demo}
    print("Unique players:", players_unique)
    print("Unique achievements: ", unique_achievements)


if __name__ == "__main__":
    analytics_dashboard()
