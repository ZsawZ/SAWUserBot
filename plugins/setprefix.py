from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from plugins.restart import restart
import configparser
import os
import sys

from prefix import my_prefix
prefix = my_prefix()


config_path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(config_path)


@Client.on_message(filters.command("sp", prefixes=prefix) & filters.me)
async def sprefix(client, message):
    if len(message.command) > 1:
        prefixgett = message.command[1]
        config.set("prefix", "prefix", prefixgett)
        with open(config_path, "w") as config_file:
            config.write(config_file)
        await message.edit(
            f"<b>prefix [ <code>{prefixgett}</code> ] set!</b>\nRestarting userbot..."
        )
        await restart(message, restart_type="restart")
    else:
        await message.edit("<b>prefix don't be None</b>")


module_list['setprefix'] = f'{prefix}setprefix'
file_list['setprefix'] = 'setprefix.py'
