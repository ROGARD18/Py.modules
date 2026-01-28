def achievement_tracker() -> None:
    """Analyze player achievements using set operations
    like union and intersection."""

    print("=== Achievement Tracker System ===\n")

    alice_set: set = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }

    bob_set: set = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }

    charlie_set: set = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    print(f"Player alice achievements: {alice_set}")
    print(f"Player bob achievements: {bob_set}")
    print(f"Player charlie achievements: {charlie_set}")

    print("\n=== Achievement Analytics ===")

    total_set = alice_set.union(bob_set, charlie_set)
    print(f"All unique achievements: {total_set}")
    print(f"Total unique achievements: {len(total_set)}\n")

    common_all = alice_set.intersection(bob_set, charlie_set)
    print(f"Common to all players: {common_all}")

    rare_alice = alice_set.difference(bob_set.union(charlie_set))
    rare_bob = bob_set.difference(alice_set.union(charlie_set))
    rare_charlie = charlie_set.difference(alice_set.union(bob_set))
    all_rare = rare_alice.union(rare_bob, rare_charlie)

    print(f"Rare achievements (1 player): {all_rare}\n")

    print(f"Alice vs Bob common: {alice_set.intersection(bob_set)}")
    print(f"Alice unique: {alice_set.difference(bob_set)}")
    print(f"Bob unique: {bob_set.difference(alice_set)}")


if __name__ == "__main__":
    achievement_tracker()
