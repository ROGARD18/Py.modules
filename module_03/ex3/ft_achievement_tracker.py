def achievement_tracker() -> None:
    total_achievement: set = {
        "boss_slayer",
        "collector",
        "first_kill",
        "level_10",
        "perfectionist",
        "speed_demon",
        "treasure_hunter",
    }
    bob_set: set = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }
    alice_set: set = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }
    charlie_set: set = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "collector",
    }
    print(f"Palyer alice achievements: {alice_set}")
    print(f"Palyer bob achievements: {bob_set}")
    print(f"Palyer charlie achievements: {charlie_set}")

    print("")
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {total_achievement})")
    print(f"Total unique achievements : {len(total_achievement)}")

    print("")
    print(f"Common all player: {alice_set.intersection(bob_set, charlie_set)}")
    # print(f"Rare achievements ({player} players): {}")
    # UTILISER UNION !!
    print("")
    print(f"Alice vs Bob common: {alice_set.intersection(bob_set)}")
    print(f"Alice unique: {alice_set.difference(bob_set)}")
    print(f"Bob unique: {bob_set.difference(alice_set)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievement_tracker()
