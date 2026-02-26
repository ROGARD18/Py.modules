from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    fire_dragon: TournamentCard = TournamentCard("Fire Dragon", 5, "Rare",
                                                 "dragon_001", 1200, 7, 10)
    ice_wizard: TournamentCard = TournamentCard("Ice Wizard", 5, "Rare",
                                                "wizard_001", 1150, 4, 8)

    tournament: TournamentPlatform = TournamentPlatform()
    print(tournament.register_card(fire_dragon))
    print(tournament.register_card(ice_wizard))

    print("Creating tournament match...")
    print("Match result: "
          f"{tournament.create_match('dragon_001', 'wizard_001')}")

    print("\nTournament Leaderboard:")
    leaderboard: list = tournament.get_leaderboard()
    for i in range(len(leaderboard)):
        c: TournamentCard = leaderboard[i]
        print(f"{i + 1}. {c.name} - Rating {c.rating} ({c.wins}-{c.losses})")

    print(f"\nPlatform Report: {tournament.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
