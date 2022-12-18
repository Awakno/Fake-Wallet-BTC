#===========Import============#
import string , time , colorama
from random import *
from pystyle import *
import requests
import subprocess
import os
import re
import json
from urllib.request import Request, urlopen
colorama.init()
os.system("title PutinMine V2 - register")
n = 0
rand = randint(1,1000000)
rand1 = randint(1,99)


#==============Intro================#
banner = """           
                        
        _______               __      __                  __       __  __                     __     __   ______  
        |       \             |  \    |  \                |  \     /  \|  \                   |  \   |  \ /      \ 
        | $$$$$$$\ __    __  _| $$_    \$$ _______        | $$\   /  $$ \$$ _______    ______ | $$   | $$|  $$$$$$\
              | $$__/ $$|  \  |  \|   $$ \  |  \|       \       | $$$\ /  $$$|  \|       \  /      \| $$   | $$ \$$__| $$
        | $$    $$| $$  | $$ \$$$$$$  | $$| $$$$$$$\      | $$$$\  $$$$| $$| $$$$$$$\|  $$$$$$\\$$\ /  $$ /      $$
        | $$$$$$$ | $$  | $$  | $$ __ | $$| $$  | $$      | $$\$$ $$ $$| $$| $$  | $$| $$    $$ \$$\  $$ |  $$$$$$ 
        | $$      | $$__/ $$  | $$|  \| $$| $$  | $$      | $$ \$$$| $$| $$| $$  | $$| $$$$$$$$  \$$ $$  | $$_____ 
        | $$       \$$    $$   \$$  $$| $$| $$  | $$      | $$  \$ | $$| $$| $$  | $$ \$$     \   \$$$   | $$     \
              \$$        \$$$$$$     \$$$$  \$$ \$$   \$$       \$$      \$$ \$$ \$$   \$$  \$$$$$$$    \$     \$$$$$$$$
                                                                                                                
                                                                                                                
                                                                                                           

"""


box = '''
                   |=================================================================|
                   |----------------           Putin Mine V2            -------------|
                   |- Created ----------------------------------------- PolarisWolf -|
                   |- Site For Wallet - https://login.blockchain.com/fr/#/coins/BTC -|
                   |- GiTHUB  ------------------------------ Github.Com/PolarisWolf -|
                   |=================================================================|
'''
#=====================Print Intro=================#
Write.Print(banner,Colors.purple_to_red,interval=0.000001)
Write.Print(box,Colors.red_to_yellow,interval=0.000001)

#Fake Proxies Choice
proxies = Write.Input("""
        
Proxies[1]
Don't use Proxies[2]
> """,Colors.red_to_yellow,interval=0.0001)
print()
print(colorama.Fore.LIGHTYELLOW_EX+ "               -------------------------------------------------------------------------")


if proxies == "1":
        print(colorama.Fore.LIGHTMAGENTA_EX+"Importing...")
        time.sleep(0.6)
        print("Connection to google Proxies...")
        time.sleep(2)
        print(colorama.Fore.LIGHTCYAN_EX + "Succes - Imported")
if proxies == "2":
        print(colorama.Fore.LIGHTBLUE_EX+"Start :)")

#Vérification Du Wallet 
Write.Print("\nHi ! ",Colors.red_to_yellow,interval=0.000001)
wallet = Write.Input("\nAdress Wallet : ",Colors.purple_to_red,interval=0.000001)
walletCheck =requests.get("https://blockchain.info/q/addressbalance/"+ wallet)
if walletCheck.status_code == 200:
    print()
    
    print(colorama.Fore.RED+"\nConnecting To The Server...")
    os.system("title PutinMine V2 - connecting...")
    time.sleep(0.3)
    Write.Print(colorama.Fore.LIGHTGREEN_EX+"\nConnected Succes !\n ",Colors.purple_to_red,interval=0.000001)
    os.system("title PutinMine V2 - connected !")
else:
    Write.Print("\nConnecting To The Server...",Colors.purple_to_red,interval=0.000001)
    time.sleep(0.3)
    print(colorama.Fore.LIGHTRED_EX + "\nInvalid Wallet !")
    os.system("title PutinMine V2 - Invalid Wallet")
    time.sleep(30)
    exit(123)
list = ["1", "2","3","4","5","6","7","8","9","0"]
all = string.ascii_lowercase + string.digits
all = str(all) 
all1 = string.digits
#Affichage Des Code BTC
os.system("title PutinMine V2 - Start ")
while n < rand:
        
    n = n + 1
    gen = "".join(choice(all)for x in range(randint(40,40)))
    print(colorama.Fore.WHITE + "[" + colorama.Fore.LIGHTBLUE_EX + "+" +colorama.Fore.WHITE + "]" +colorama.Fore.LIGHTRED_EX +f"bc{gen}"+ colorama.Fore.CYAN + f"{colorama.Fore.BLUE}[ {colorama.Fore.CYAN}Invalid {colorama.Fore.BLUE}] " + colorama.Fore.WHITE + "-> 0.0000 BTC")
    print(colorama.Fore.LIGHTYELLOW_EX+ "----------------------------------------------------------------------------------------------------------")
    
    time.sleep(0.01)
#Fake Trouveurs
os.system("title PutinMine V2 - BTC Find !")
gen = "".join(choice(all)for x in range(randint(40,40)))
gen1 = "".join(choice(all1)for x in range(randint(1,9)))
gen1 = str(gen1)
print(colorama.Fore.WHITE + "[" + colorama.Fore.LIGHTBLUE_EX + "+" +colorama.Fore.WHITE + "]"+colorama.Fore.LIGHTGREEN_EX + f"bc{gen}"+ f"{colorama.Fore.BLUE}[{colorama.Fore.CYAN} Valid {colorama.Fore.BLUE}]" + colorama.Fore.WHITE+f"-> 0.00{gen1} BTC")
#Envoie Vers Le Wallet
os.system("title PutinMine V2 - Sending")
Write.Print("\nSending To Wallet...\n",Colors.red_to_purple,interval=0.00001)
time.sleep(1.8)
os.system("title PutinMine V2 - Sended")
Write.Print("Sended Succes !\n",Colors.red_to_purple,interval=0.00001)
time.sleep(5)
exit()

