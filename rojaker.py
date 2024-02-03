#Made By James Ryan Wood 

#Imports 
import os
from roku import Roku
import time 


#Menu 
os.system("clear")
result = input("Enter IP: ")
os.system("clear")
os.system("figlet -f slant RoJaker")
print('------------------------')
print('Made By James Ryan Wood')
print("IP Slected "+result)
print('------------------------')
roku = Roku(result)
print("1. Get Info\n2. See Current Running App\n3. Dump Apps\n4. Remote\5.Run A App\n6.home menu")
menu = input("Menu> ")


if menu == "1":
    print(roku.info)
    input("press enter to return to menu")
   
elif menu == "2":
    print(roku.active_app)
elif menu == "3":
    app = roku.apps[0]
    print(app.id, app.name, app.version)
elif menu == "4":
    print("Work in progress")
elif menu == "5":
   roku.discover()
elif menu == "6":
   roku.home() 
   print("command launched")
else: 
    print("Invaild menu slection!")
