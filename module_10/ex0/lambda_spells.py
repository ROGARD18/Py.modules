def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda index: -index['power']))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return (list(filter(lambda x: (x['power'] > min_power), mages)))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda x: "* " + x + " *", spells)))


def mage_stats(mages: list[dict]) -> dict:
    mage_max = max(mages, key=lambda x: x['power'])
    mage_min = min(mages, key=lambda x: x['power'])
    avg: float = sum(map(lambda x: x['power'], mages)) / len(mages)
    return {
        'max_power': mage_max['power'],
        'min_power': mage_min['power'],
        'avg_power': round(avg, 2)
    }


def main() -> None:
    artifacts: list = [
        {'name': 'Fire Staff', 'power': 109, 'type': 'armor'},
        {'name': 'Water Chalice', 'power': 74, 'type': 'focus'},
        {'name': 'Earth Shield', 'power': 84, 'type': 'weapon'},
        {'name': 'Earth Shield', 'power': 62, 'type': 'focus'}
        ]
    mages: list = [
        {'name': 'Riley', 'power': 99, 'element': 'lightning'},
        {'name': 'Alex', 'power': 50, 'element': 'earth'},
        {'name': 'Rowan', 'power': 67, 'element': 'lightning'},
        {'name': 'Alex', 'power': 93, 'element': 'lightning'},
        {'name': 'Storm', 'power': 52, 'element': 'lightning'}
        ]
    spells: list = ['lightning', 'shield', 'fireball', 'freeze']

    print("\nTesting artifact sorter...")
    artifact_sorted: list[dict] = artifact_sorter(artifacts)
    index: int = 0
    len_list: int = len(artifact_sorted)

    for artifact in (artifact_sorted):
        print(artifact['name'], f"({artifact['power']} power)", end="")
        if (index == len_list - 1):
            break
        print(" comes before ", end="")
        index += 1

    print("\n\nTesting spell transformer...")
    spells_transformed: list[str] = spell_transformer(spells)
    for spell in spells_transformed:
        print(spell, end=" ")

    print("\n\nTesting power filter (power > 90)...")
    print(power_filter(mages, 90))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
