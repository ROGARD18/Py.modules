def read_ancient_fragement_file() -> None:
    """Try to read a file. So we check if the file exist or not.
    """
    file_name: str = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ", {file_name})
    try:
        file = open(file_name, "r")
        print("Connection established...\n")
    except Exception:
        print("ERROR: Storage vault not found")
        return
    print("RECOVERED DATA:")
    print(file.read())

    print("\nData recovery complete. Storage unit disconnected.")
    file.close()


if __name__ == "__main__":
    read_ancient_fragement_file()
