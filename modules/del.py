@app.on_message(filters.command("del", prefixes=prefix) & filters.me)

async def delete_messages(client: Client, message: Message):

    if message.reply_to_message:
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Удалено сообщение"
        await app.send_message("sawUSERBOT_LOGGERbot", log)

        message_id = message.reply_to_message.message_id
        await message.delete()
        await client.delete_messages(message.chat.id, message_id)
