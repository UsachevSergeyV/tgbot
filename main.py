import logging
import  telebot
import apiGetContractByReestr
import  GetFileArchive
import fileManager
logging.basicConfig(level=logging.WARNING)
fileToken = open('token','r')
token = fileToken.readline()
fileToken.close()
logging.debug(token)



bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.isnumeric():
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        btn1 = telebot.types.InlineKeyboardButton("Контракт",callback_data="callback_C")
        btn2 = telebot.types.InlineKeyboardButton('Закупка', callback_data ="callback_Z")
        btn3 = telebot.types.InlineKeyboardButton('План график', callback_data="callback_PG")
        btn4 = telebot.types.InlineKeyboardButton('Проект контракта',callback_data="callback_PK")
        btn5 = telebot.types.InlineKeyboardButton('хуй знает',callback_data="callback_hz")
        markup.add(btn1, btn2, btn3, btn4,btn5)
        bot.reply_to(message, text="Что это'?", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id,"Не понятно что это, херь какая то!",reply_to_message_id=message.id)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    media =[]
    streams = []
    nameFile=[]
    arrsubSystem=[]
    if(str(callback.data).startswith("callback")):
        #bot.send_message(callback.message.chat.id, "Вычисляем..",reply_to_message_id=callback.message.message_id-1)
        if callback.data == "callback_C":
            arrsubSystem.append("RGK")
        elif callback.data =="callback_Z":
            arrsubSystem.append("PRIZ")
        elif callback.data =="callback_PG":
            arrsubSystem.append("RPGZ")
        elif callback.data =="callback_PK":
            arrsubSystem.append("RPEC")
        elif callback.data =="callback_hz":
            arrsubSystem.append("RGK")
            arrsubSystem.append("RPEC")
            arrsubSystem.append("RPGZ")
            arrsubSystem.append("PRIZ")
            arrsubSystem.append("PRIZ")
            arrsubSystem.append("PRIZP")
            arrsubSystem.append("RRK")
        nameFile = GetFileArchive.getFile(apiGetContractByReestr.getDocsSpecType(callback.message.reply_to_message.text, arrsubSystem))

        #ТЕСТ nameFile21 = GetFileArchive.getFile(apiGetContractByReestr.getDocs(callback.message.reply_to_message.text))

        nameFile = fileManager.killSig(nameFile)
        for n in nameFile:
            openfile = open(n,"rb")
            streams.append(openfile)
            media.append(telebot.types.InputMediaDocument(media=openfile))
        if len(media)==0:
            bot.send_message(callback.message.chat.id, "ничего не найдено",reply_to_message_id=callback.message.message_id-1)
        else:
            for i in range(0,round(len(media)//10)+1):
                subMedia = media[i*10:i*10+10]
                if len(subMedia) >0:
                    bot.send_media_group(chat_id=callback.message.chat.id, media=subMedia, reply_to_message_id=callback.message.id-1)
        for s in streams:
            s.close()
        fileManager.Summon_Mr_Proper(nameFile)
    else:
        bot.send_message(callback.message.chat.id, "Непонятно делать то  что..",reply_to_message_id=callback.message.message_id-1)




#
#   logging.warning("Обратился пользователь " + message.from_user.full_name+", хочет знать про "+ message.text)
#   # ПОКА ЧТО ОБРАБАТЫВАЕМ ВСЁ ЧТО ПОХОЖЕ НА ЧИСЛА, если это числа запускаем процес попытки получить информацию с сервиса
#   if message.text.isnumeric():
#      #получаем файлы и возвращаем пути к этим файлам
#      nameFile = GetFileArchive.getFile(apiGetContractByReestr.getDocs(message.text))
#      nameFile = fileManager.killSig(nameFile)
#      media =[]
#      streams =[]
#      for n in nameFile:
#          openfile = open(n,"rb")
#          streams.append(openfile)
#          media.append(telebot.types.InputMediaDocument(media=openfile))
#      if len(media)==0:
#          bot.send_message(message.from_user.id, "ничего не найдено")
#      else:
#          for i in range(0,round(len(media)//10)+1):
#              subMedia = media[i*10:i*10+10]
#              if len(subMedia) >0:
#               bot.send_media_group(chat_id=message.from_user.id, media=subMedia, reply_to_message_id=message.id)
#      for s in streams:
#          s.close()
#      fileManager.Summon_Mr_Proper(nameFile)
#   elif message.text == '12345':
#       bot.send_message(message.from_user.id,"67890")
#   elif str(message.text).startswith("_"):
#
#       bot.send_message(message.from_user.id, "ответ на ветку кода соответствующий регистрации следующей функции. Умножит переданное число на 12")
#       bot.register_message_handler(message,wtf)
#   else:
#       bot.send_message(message.from_user.id,"ответ на неизвесно что")
#


bot.polling(non_stop=True, interval=0)

print("press any key")
