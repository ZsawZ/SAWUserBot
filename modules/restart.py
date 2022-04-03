@Client.on_message(filters.command("restart", prefixes=prefix) & filters.me)
async def restartt(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был выключен"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.delete()
    await Client.send_audio(message.chat.id, "stop.ogg", "<code>Перезагрузка...</code>")
    await restart(message, restart_type="restart")

@Client.on_message(filters.command("update", prefixes=prefix) & filters.me)
async def updatte(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был обновлён"
    await Client.send_message("sawUSERBOT_LOGGERbot", log)

    await message.edit("<code>Обновление...</code>")
    subprocess.call(["bash", "update.sh"])
    await message.edit("<code>Юзербот успешно обновлён!</code>")
    await restart(message, restart_type="1")

module_list['Restarter'] = f'{prefix}restart | {prefix}update'
file_list['Restarter'] = 'restart.py'