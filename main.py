# -*- coding: utf-8 -*-
from pyrogram import Client
from configurator import my_api
from prestarter import prestart
 
 
# start
if __name__ == "__main__":
    api_id, api_hash, device_mod = my_api()
    prestart()
    plugins = dict(root="modules")
    Client = Client("my_account", api_id=api_id, api_hash=api_hash, device_model=device_mod, plugins=modules).run()
    app = Client("my_account", api_id=api_id, api_hash=api_hash, device_model=device_mod, plugins=modules).run()
    logi = "╭ Логи\n┃ "
    with app:
         app.join_chat("SAWuser_bot") 
  
 
