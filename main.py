# -*- coding: utf-8 -*-
from pyrogram import Client
from configurator import my_api
from prestarter import prestart
 
logi = "╭ Логи\n┃ "
# start
if __name__ == "__main__":
    api_id, api_hash, device_mod = my_api()
    prestart()
    plugins = dict(root="plugins")
    Client = Client("my_account", api_id=api_id, api_hash=api_hash, device_model=device_mod, plugins=plugins).run()
    with Client:
         Client.join_chat("SAWUserBot") 
         Client.unblock_user("sawUSERBOT_LOGGERbot")
         now = datetime.datetime.now()
         timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
         startlog = logi + timnow + "\n╰ Юзербот был запущен"
         Client.send_message("sawUSERBOT_LOGGERbot", startlog)
 
