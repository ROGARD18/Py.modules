def analytics_dashboard() -> None:
    """Desmontrate all knowledge of list, set and dictionary.
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

    # i: int = 0
    # score_categories: dict = {"hight": for player, infos in players_dict.items()
    #                           if infos.get("score")}
    
    players_counts_achi: dict = {player: len(infos.get('achievements')) for
                                 player, infos in players_dict.items()}
    print("Achievements counts: ", players_counts_achi)

    print("\n=== Set Comprehension Example ===")
    print("Unique achievements: ", )
    # hight_score: list = []
    # score_doubled: list = []
    # score_simple: list = []
    # active_player: list = []
    # player_user: list = []
    # all_list_of_achievements: list[list] = []

    # for user, infos in players_dict.items():
    #     if (infos.get("score") > 2000):
    #         hight_score.append(user)
    #     if (infos.get("score") > 500):
    #         active_player.append(user)
    #     player_user.append(user)
    #     score_simple.append(infos.get("score"))
    #     all_list_of_achievements.append(infos.get("achievements"))
    #     score_doubled.append(infos.get("score") * 2)

    # print(f"High scores (>2000): {hight_score}")
    # print(f"Scores doubled: {score_doubled}")
    # print(f"Active players: {active_player}")

    # print("\n=== Set Comprehension Examples ===")
    # achievements_tot: set = {0}
    # achiev_mult: set = {0}
    # i: int = 0

    for user, infos in players_dict.items():
        achievements = set(infos["achievements"])
        mult = set(infos["achievements"])
        for subuser, subinfos in players_dict.items():
            if user == subuser:
                continue
            achievements = achievements.difference(subinfos["achievements"])
            mult = mult.intersection(subinfos["achievements"])
        if (i == 0):
            achievements_tot = achievements
            achiev_mult = mult
        else:
            achievements_tot = achievements_tot.union(achievements)
            achiev_mult = achiev_mult.union(mult)
        i += 1

    # print(f"Unique achievements: {achievements_tot}")
    # print(f"Achievements obtained by all: {achiev_mult}")

    # print("\n=== Combined Analysis ===")
    # achievements_flat: list = []
    # for element in all_list_of_achievements:
    #     for item in element:
    #         achievements_flat.append(item)

    # player_number: int = len(players_dict.keys())
    # print(f"Total players: {player_number}")2


if __name__ == "__main__":
    analytics_dashboard()
