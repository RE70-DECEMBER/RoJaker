#Made By James Ryan Wood 

#Imports 
import os
from roku import Roku
import time 


#Menu 
os.system("clear")
os.system("figlet -f slant RoJaker")
print('------------------------')
print('Made By James Ryan Wood')
print('------------------------')
roku.discover(timeout=10)
ip = input("Enter IP: ")
print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\5.Run A App\n6.Exit")
menu = input("Menu> ")


if menu == "1":
    roku = Roku(ip)
    roku.info

elif menu == "2":
    roku = Roku(ip)
    a.active_app
elif menu == "3":
    Roku = Roku(ip)
    app = a.apps[0]
    print(app.id, app.name, app.version)
elif menu == "4":
    print("Work in progress")
elif menu == "5":
    print("Work in Progress")
elif menu == "6":
    print ("Work In Progress")
