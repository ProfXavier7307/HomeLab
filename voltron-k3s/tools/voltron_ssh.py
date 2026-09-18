import subprocess

"""
Voltron SSH Connection Program

Opens a new Windows Command Prompt SSH session for a selected Voltron node.
The launcher remains open so multiple nodes can be connected at the same time.

Local cluster addressing:
- Machine #1: 192.168.1.101 - Lance  (Red Lion)
- Machine #2: 192.168.1.102 - Hunk   (Yellow Lion)
- Machine #3: 192.168.1.103 - Allura (Blue Lion)
- Machine #4: 192.168.1.104 - Keith  (Black Lion)
- Machine #5: 192.168.1.105 - Pidge  (Green Lion)
"""

devices = {
    "1": ("Lance", "Red Lion", "192.168.x.x"),
    "2": ("Hunk", "Yellow Lion", "192.168.x.x"),
    "3": ("Allura", "Blue Lion", "192.168.x.x"),
    "4": ("Keith", "Black Lion", "192.168.x.x"),
    "5": ("Pidge", "Green Lion", "192.168.x.x"),
}

print("Welcome to the Voltron SSH Connection Program!")

while True:
    print()
    print("Please select a device to connect to:")

    for number, (name, lion, ip) in devices.items():
        print(f"{number}. {name} ({lion}) - {ip}")

    print("6. Exit")
    print()

    choice = input("Enter the number of the device you want to connect to: ")

    if choice == "6":
        print("Exiting...")
        break

    if choice in devices:
        name, lion, ip = devices[choice]
        print(f"Connecting to {name} ({lion}) at {ip}...")

        subprocess.Popen(
            ["cmd.exe", "/k", "ssh", f"xander@{ip}"],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    else:
        print("Invalid choice.")
