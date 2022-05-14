from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, version
from telegraph import Telegraph
import time, random, datetime, asyncio, sys, wikipedia, requests, json, colorama, requests, youtube_dl, subprocess, configparser
from time import time
from prefix import my_prefix
prefix = my_prefix()
 
 
@Client.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def helps(client, message):
    lists = []
    for k, v in module_list.items():
        lists.append(f'• {k}: {v}<br>')
    a = " "
    for i in lists:
        a = a.lstrip() + f'{i}'
    helpes = f"""
{len(module_list)} Доступные модули.<br>
<br>
{a}
"""
    await message.edit('Загрузка.')
    await message.edit('Загрузка..')
    await message.edit('Загрузка...')
    telegraph = Telegraph()
    telegraph.create_account(short_name='SAWUserBotHELP')
    link = f"https://telegra.ph/{telegraph.create_page('SAWUserBot Help.', html_content=f'{helpes}')['path']}"
    await message.edit(f"""<b>🚑 | Меню команд. </b>
<b>🔒 | Версия: {version}</b>
<b>💼 | Модули: {len(module_list)}</b>
 
<><a href="https://t.me/SAWuser_Bot">🤖 UserBot SAW {version} 🤖</a></b>
<b><a href="https://t.me/sawandr">👨‍💻 Создатель 👨‍💻</a></b>
<b><a href="https://github.com/Brawl9008/SAWUserbot#readme">🤔 Как установить? 🤔</a></b>
<b><a href="https://telegra.ph/KOMANDY-SAWUSERBOT-03-29">📂 Команды 📂</a></b> """, disable_web_page_preview=True)
 
 
module_list['Help'] = f'{prefix}help'