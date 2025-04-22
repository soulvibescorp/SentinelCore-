from core import encryption, scanner, firewall
import getpass

def menu():
    print("\n🛡 SentinelCore CLI\n1. Encrypt\n2. Decrypt\n3. Scan\n4. Firewall Check")
    return input("Select action: ")

def run():
    while True:
        choice = menu()
        if choice == "1":
            encryption.encrypt_file("tests/input.txt", "storage/output.bin", get_random_bytes(32))
        elif choice == "2":
            encryption.decrypt_file("storage/output.bin", "storage/restore.txt", get_random_bytes(32))
        elif choice == "3":
            print(scanner.scan_file("tests/input.txt"))
        elif choice == "4":
            port = int(input("Port: "))
            print(firewall.run_check(port))
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run()

