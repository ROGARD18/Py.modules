def write_in_new_file() -> None:
    """
    Write infos in a new file.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name: str = "new_discovery.txt"

    print("Initializing new storage unit:", file_name)
    print("Storage unit created successfuly...\n")

    file = open(file_name, "w")
    file.write("[ENTRY 001] New quantum algorithm discovered\n"
               "[ENTRY 002] Efficiency increased by 347%\n"
               "[ENTRY 003] Archived by Data Archivist trainee\n")

    file.close()
    file = open(file_name, "r")
    print("Inscribing preservatiom data...")
    print(file.read())
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name} ready for long-term preservation.")


if __name__ == "__main__":
    write_in_new_file()
