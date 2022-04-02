@app.on_message(filters.command("time", prefixes=prefix) & filters.me)

async def time(client: Client, message: Message):

    now = datetime.datetime.now()
    timnow = now.strftime("%d.%m.%Y\nВремя %H:%M:%S")
    timenow = "Текущая дата : " + timnow
    await message.edit(timenow)