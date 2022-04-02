import os
import colorama
from plugins.settings.main_settings import version
 
from prefix import my_prefix
prefix = my_prefix()
 
yellow = "\033[1;33m"
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\33[1;36m"
purple = "\33[1;35m"
 
os.system("cls" if os.name == "nt" else "clear")
print(f"""{red}

▒█▀▀▀█ ░█▀▀█ ▒█░░▒█ 
░▀▀▀▄▄ ▒█▄▄█ ▒█▒█▒█ 
▒█▄▄▄█ ▒█░▒█ ▒█▄▀▄█

▒█░▒█ ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀█ ░░ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
▒█░▒█ ░▀▀▀▄▄ ▒█▀▀▀ ▒█▄▄▀ ▀▀ ▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
░▀▄▄▀ ▒█▄▄▄█ ▒█▄▄▄ ▒█░▒█ ░░ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
{green}
Channel: @foxteam0
Help: @foxteamchat
Version: {version}
Prefix: [ {prefix} ]
 
Client Started!
Type {prefix}ping to check Userbot works
""")