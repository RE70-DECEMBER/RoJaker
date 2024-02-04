# Made By James Ryan Wood

# Imports
import os
from roku import Roku
import sys

# IP Input
os.system("clear")
print("scanning...")

roku_devices = Roku.discover()
print("M. Manual Input IP")
for i, device in enumerate(roku_devices):
    print(f"{i+1}. {device}")
selected_index = input("Select A Option:  ")

if selected_index.lower() == "m":  # Convert selected_index to lowercase before comparison
    selected_device = input("Enter IP address: ")
else:
    selected_index = int(selected_index) - 1

    if selected_index < 0 or selected_index >= len(roku_devices):
        print("Invalid selection")
        exit()
    else:
        selected_device = roku_devices[selected_index].host  # Get only the IP address without the port

# Menu
def main():
    os.system("clear")
    os.system("figlet -f slant RoJaker")
    print('------------------------')
    print('Made By James Ryan Wood')
    print("IP Selected: " + selected_device)
    print('------------------------')
    print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\n5. Run An App\n6. Exit")
    menu = input("Menu> ")
    return menu

def remote_menu():
    os.system("clear")
    os.system("figlet -f slant RoJaker")
    print('------------------------')
    print('Made By James Ryan Wood')
    print("IP Selected: " + selected_device)
    print('------------------------')
    print("1. Up\n2. Down\n3. Right\n4. Left\n5. Select\n6. Back\n7. Replay\n8. Return to RoJaker")
    rem = input("Remote> ")
    if rem == "1":
        roku = Roku(selected_device)
        se = input("Enter something: ")
        roku.literal(se)
        remote_menu()  # Call remote_menu() again to return to the remote menu

while True:
    menu = main()
    if menu == "1":
        roku = Roku(selected_device)
        print(roku.info)
        input("Press enter to return to menu")
    elif menu == "2":
        roku = Roku(selected_device)
        print(roku.active_app)
        input("Press enter to return to menu")
    elif menu == "3":
        app = roku.apps[0]
        print(app.id, app.name, app.version)
    elif menu == "4":
        remote_menu()
    elif menu == "6":
        break
