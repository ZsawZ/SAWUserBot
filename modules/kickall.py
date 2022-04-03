@Client.on_message(filters.command("kickall hide", prefixes=prefix) & filters.me)

def kickall(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Удалены участники"
    Client.send_message("sawUSERBOT_LOGGERbot", log)

    message.delete()
    num = 0
    for all in client.iter_chat_members(message.chat.id):
       try:
           num =+ 1
           client.kick_chat_member(message.chat.id, all.user.id, 0)
       except:
           pass

@Client.on_message(filters.command("kickall", prefixes=prefix) & filters.me)

def kickall(client: Client, message: Message):

    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Удалены участники"
    Client.send_message("sawUSERBOT_LOGGERbot", log)

    message.edit("Вашим участникам конец)")
    num = 0
    for all in client.iter_chat_members(message.chat.id):
       try:
           num =+ 1
           client.kick_chat_member(message.chat.id, all.user.id, 0)
       except:
           pass

module_list['Kickall'] = f'{prefix}kickall | {prefix}kickall hide'
file_list['Ki'] = 'bomber.py'