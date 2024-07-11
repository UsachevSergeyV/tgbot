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
    logging.warning("Обратился пользователь " + message.from_user.full_name+", хочет знать про "+ message.text)
    # ПОКА ЧТО ОБРАБАТЫВАЕМ ВСЁ ЧТО ПОХОЖЕ НА ЧИСЛА, если это числа запускаем процес попытки получить информацию с сервиса
    if message.text.isnumeric():
       #получаем файлы и возвращаем пути к этим файлам
       nameFile = GetFileArchive.getFile(apiGetContractByReestr.getDocs(message.text))
       nameFile = fileManager.killSig(nameFile)
       media =[]
       streams =[]
       for n in nameFile:
           openfile = open(n,"rb")
           streams.append(openfile)
           media.append(telebot.types.InputMediaDocument(media=openfile))

       if len(media)==0:
           bot.send_message(message.from_user.id, "ничего не найдено")
       else:
           for i in range(0,round(len(media)//10)+1):
               subMedia = media[i*10:i*10+10]
               if len(subMedia) >0:
                bot.send_media_group(chat_id=message.from_user.id, media=subMedia, reply_to_message_id=message.id)

       for s in streams:
           s.close()

        # for name in nameFile:
        #    logging.warning("name"+name)
        #     f = open(name,'rb')
        #    # отдаем файл пользователю который его запросил в виде ответа на сообщение
        #   #bot.send_document(chat_id=message.from_user.id,document= f,reply_to_message_id=message.id)
        #  f.close()
       fileManager.Summon_Mr_Proper(nameFile)




    elif message.text == '12345':
        bot.send_message(message.from_user.id,"67890")
    else:
        bot.send_message(message.from_user.id,"ответ на неизвесно что")

bot.polling(non_stop=True, interval=0)

print("press any key")
