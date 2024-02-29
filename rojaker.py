# Made By James Ryan Wood

# import module checker
import importlib.util

roku_installed = importlib.util.find_spec("roku") is not None
colorama_installed = importlib.util.find_spec("colorama") is not None

if not roku_installed or not colorama_installed:
    print("[ERROR] requirements not installed")
    request = input("Install them? Y or N > ")
    print()
    if request.upper() == "Y":
        if not roku_installed:
            try:
                import pip
                pip.main(["install", "roku"])
                print("[SUCCESS] roku installed!")
            except ImportError:
                print("[ERROR] pip is not installed. Please install it manually.")
        if not colorama_installed:
            try:
                import pip
                pip.main(["install", "colorama"])
                print("[SUCCESS] colorama installed!")
            except ImportError:
                print("[ERROR] pip is not installed. Please install it manually.")
    else:
        print("[EXITING] Requirements not installed...")
        exit()

# imports
import os
from roku import Roku
import colorama
from colorama import Fore, Back, Style
import sys
import socket
import struct
import time

# IP Input
os.system("clear")
print("scanning...")

roku_devices = Roku.discover(timeout=10)
print("M. Manual Input IP")
for i, device in enumerate(roku_devices):
    print(f"{i+1}. {device}")
selected_index = input("Select A Option:  ")

if selected_index.lower() == "m":  
    selected_device = input("Enter IP address: ")
else:
    selected_index = int(selected_index) - 1
    if selected_index < 0 or selected_index >= len(roku_devices):
        print("Invalid selection")
        exit()
    else:
        selected_device = roku_devices[selected_index].host  

# Menu
def main():
    os.system("clear")
    os.system("figlet -f slant RoJaker")
    border = "|---------------------------|"
    formatted_device = selected_device.center(len(border) - 12)
    print(border)
    print('| Made By: RE70-DECEMBER    |')
    print("| Target: {} |".format(formatted_device))
    print(border)
    print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\n5. Run An App\n6. Power off or on TV\n7. Check TV Up Time\n8. Exit")
    menu = input("Menu> ")
    return menu

def remote_menu():
    os.system("clear")
    os.system("figlet -f slant RoJaker")
    print('------------------------')
    print(Fore.GREEN + 'Made By James Ryan Wood')
    print("IP Selected: " + selected_device)
    print('------------------------')
    print("1. Up\n2. Down\n3. Right\n4. Left\n5. Select\n6. Back\n7. Replay\n8.Home menu\n9. Return to RoJaker")
    rem = input("Remote> ")
    
    while True:
        if rem == "1":
        	roku = Roku(selected_device)
        	se = input("Enter something: ")
        	roku.literal(se)
        	remote_menu() 
        	
        elif rem == "8":
        	roku = Roku(selected_device)
        	roku.home()
        	remote_menu()
        elif rem == "9":
        	main()


while True:
    menu = main()
    if menu == "1":
        roku = Roku(selected_device)
        colorama.init()
        print(Fore.GREEN + roku.info)
        input("Press enter to return to menu")
        print(Fore.White)
    elif menu == "2":
        roku = Roku(selected_device)
        print(roku.active_app)
        input("Press enter to return to menu")
    elif menu == "3":
        roku = Roku(selected_device)
        print(roku.apps)
        input("Press enter to return to menu")
    elif menu == "4":
        remote_menu()
    elif menu == "5":
    	roku = Roku(selected_device)
    	user_run = input("Enter A App ID: ")
    	test = roku[user_run]
    	test.launch()
    elif menu == "6":
    	roku = Roku(selected_device)
    	roku._post('/keypress/Power')
    	print("[*]TV Powered Off or On")
    	input("Press enter to return to menu")
    elif menu == "8":
    	exit()
