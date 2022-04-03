linkToken = "6c2ac1846a1c1A2d5f88A3E5fbf0e14fcf96d7d0"

async def link_short(link: str):

    async with ClientSession(
        headers={
            "Authorization": f"API-Key {linkToken}"
        }
    ) as ses:
        async with ses.post(
            "https://api.waa.ai/v2/links",
            json={"url": link}
        ) as resp:
            return await resp.json()

@Client.on_message(filters.command("short", prefixes=prefix) & filters.me)
async def shorten_link_command(client: Client, message: Message):
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Сокращенная ссылка"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
         link = message.reply_to_message.text
    else:
        try:
            link = message.command[1]
        except IndexError:
            return await message.delete()
    output = (await link_short(link))["data"]
    await message.edit(f"Сокращенная ссылка: {output['link']}")

module_list['LinkShorter'] = f'{prefix}bomber | {prefix}sbomber | {prefix}bbomber'
file_list['Bomber'] = 'bomber.py'