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

from colorama import Fore, Back, Style, init

import sys

import socket

import struct

import time

import requests





def check_for_update():

    pastebin_link = "https://pastebin.com/raw/Fg1HgGhX"

    response = requests.get(pastebin_link)

    if response.status_code == 200:

        pastebin_number = int(response.text.strip())



        current_script_number = 3



        if pastebin_number > current_script_number:

            print("["+Fore.RED+ "UPDATE"+Fore.WHITE+"]"+" is available!")

        else:

            print("["+Fore.GREEN+ "No Update"+Fore.WHITE+"]"+" is available!")

    else:

        print("Failed to retrieve data from Pastebin. Please check the link.")

# IP Input

os.system("clear")

check_for_update()

file_path = "chosen_color.txt"

init(autoreset=False) 

with open(file_path, 'r') as file:

    c_clr = file.read()

print(getattr(Fore, c_clr.upper(),) + "scanning...")



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

    print(border)

    print("| Version:        3         |")

    print(border)

    print("| Target: {} |".format(formatted_device))

    print(border)

    print()

    print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\n5. Run An App\n6. Power off or on TV\n7. Script Color \n8. Exit")

    print()

    menu = input("(Menu) --> ")

    return menu



def remote_menu():

    os.system("clear")



    os.system("figlet -f slant RoJaker")



    border = "|---------------------------|"

    formatted_device = selected_device.center(len(border) - 12)

    print(border)

    print('| Made By: RE70-DECEMBER    |')

    print(border)

    print("| Version:        3         |")

    print(border)

    print("| Target: {} |".format(formatted_device))

    print(border)

    print()

    print("1. Up\n2. Down\n3. Right\n4. Left\n5. Select\n6. Back\n7. Replay\n8. Home menu\n9. Return to RoJaker")

    print()

    rem = input("(Remote) --> ")

    

    if rem == "1":

      roku = Roku(selected_device)

      roku._post('/keypress/Up')

      remote_menu() 

        	

    elif rem == "2":

      roku = Roku(selected_device)

      roku._post('/keypress/Down')

      remote_menu()

      

    elif rem == "3":

      roku = Roku(selected_device)

      roku._post('/keypress/Right')

      remote_menu()

    elif rem == "4":

      roku = Roku(selected_device)

      roku._post('/keypress/Left')

      remote_menu()

    elif rem == "5": 

      roku = Roku(selected_device)

      roku._post('/keypress/Select')

      remote_menu()

    elif rem == "6":

      roku = Roku(selected_device)

      roku._post('/keypress/Back')

      remote_menu()

    elif rem == "7": 

      roku = Roku(selected_device)

      roku._post('/keypress/Replay')

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

    elif menu == "7": 

      os.system("clear")

      os.system("python3 config.py")

    elif menu == "8":

    	exit()

