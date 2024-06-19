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
                os.system("python3 config.py")

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



def print_text_from_pastebin():

    """

    Function to print the text content from a given Pastebin link.



    Parameters:

    - pastebin_link: str

        The link to the Pastebin containing the text to be printed.



    Raises:

    - Exception:

        Raises an exception if there is an issue accessing the Pastebin link or retrieving the text content.

    """



    try:

        # Sending a GET request to the Pastebin link to retrieve the text content

        response = requests.get(pastebin_link)



        # Checking if the request was successful (status code 200)

        if response.status_code == 200:

            # Printing the text content from the Pastebin link

            print(response.text)

        else:

            # Handling unsuccessful request

            raise Exception(f"Failed to retrieve text content. Status Code: {response.status_code}")



    except Exception as e:

        # Handling any exceptions that might occur during the process

        print(f"An error occurred: {e}")



# Example of using the function to print text from a Pastebin link

pastebin_link = "https://pastebin.com/raw/ZXKCHMPG"

print_text_from_pastebin()



def check_for_update():

    pastebin_link = "https://pastebin.com/raw/Fg1HgGhX"

    response = requests.get(pastebin_link)

    if response.status_code == 200:

        pastebin_number = int(response.text.strip())



        current_script_number = 4



        if pastebin_number > current_script_number:

            print("["+Fore.RED+ "UPDATE"+Fore.WHITE+"]"+" is available!")

            print_text_from_pastebin()

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

    print("      _______________ ")

    print("     | /~~~~~~~~\ |||| ")

    print("     ||  fuck    |...| ")

    print("     || dem tvs  |   | ")

    print("     | \________/  O | ")

    print("      _______________ ")

    print()

    border = "|---------------------------|"

    formatted_device = selected_device.center(len(border) - 12)

    print(border)

    print('| Made By: RE70-DECEMBER    |')

    print(border)

    print("| Version:     1.04         |")

    print(border)

    print("| Target: {} |".format(formatted_device))

    print(border)

    print()

    print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\n5. Run An App\n6. Power off or on TV\n7. Script Color \n8 Enable Developer Mode \n9 Volume Loop\n0. Exit")

    print()

    menu = input("(Menu) --> ")

    return menu

#NEEDS WORK WILL DO AS SOON AS POSSIBLE
def enable_dev():
    print("Enabling developer Menu!")
    roku = Roku(selected_device)
    roku.home()
    time.sleep(1)
    roku.home()
    time.sleep(1)
    roku.home()
    time.sleep(1)
    roku._post('/keypress/Up')
    time.sleep(1)
    roku._post('/keypress/Up')
    time.sleep(1)
    roku._post('/keypress/Right')
    time.sleep(1)
    roku._post('/keypress/Left')
    time.sleep(1)
    roku._post('/keypress/Right')
    time.sleep(1)
    roku._post('/keypress/Left')
    time.sleep(1)
    roku._post('/keypress/Right')
    time.sleep(1)
    roku._post('/keypress/Left')
    time.sleep(1)
    roku._post('/keypress/Right')
    print("Developed Mode enabled\nTv Will Restart")
    print("wait 30 seconds then goto")
    print("http://"+selected_device+":80")
    print("Login Set To\nUsername: rokudev\npassword: abcd")
    input("click enter to return")
    main()


#WORKING!!!!!!
def dev_menu_check():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((selected_device,80))
    if result == 0:
        print("Developer Mode Already Detected!")
        print("Goto Browser and type to access it")
        print("http://"+selected_device+":80")
        print("Dont know login\nUsername: rokudev\npassword: ????")
        input("click enter to return to menu")
    else:
            print("No Developer Mode Detected! ")
            sock.close()
            input("click enter To Enable menu")
            enable_dev()


def vol_up_menu():
    roku = Roku(selected_device)
    while True:
        roku._post('/keypress/VolumeUp')

def vol_down_menu():
    roku = Roku(selected_device)
    while True:
        roku._post('/keypress/VolumeDown')
        


def vol_menu():
    print("Turn The volume all the way up or down")
    print("1.Up\n2.Down")
    u = input("Volume > ")
    if u == "1":
        vol_up_menu()
    elif u == "2":
        vol_down_menu()



def remote_menu():

    os.system("clear")



    os.system("figlet -f slant RoJaker")



    border = "|---------------------------|"

    formatted_device = selected_device.center(len(border) - 12)

    print(border)

    print('| Made By: RE70-DECEMBER    |')

    print(border)

    print("| Version:        4         |")

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

        print(roku.info)

        input("Press enter to return to menu")

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
        dev_menu_check()
    elif menu == "9":
        vol_menu()

    elif menu == "0":

    	exit()




