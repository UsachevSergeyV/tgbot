import logging
import  telebot
import SystemState
import apiGetContractByReestr
import  GetFileArchive
import botHelper
import fileManager
import  re
logging.basicConfig(level=logging.WARNING)
fileToken = open('token','r')
token = fileToken.readline()
fileToken.close()
logging.debug(token)



bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    logging.warning("Пользователь {0} запросил информацию о {1}".format( message.from_user.full_name, message.text))
    if message.text.isnumeric():
        bot.reply_to(message, text="Что это'?", reply_markup=botHelper.firstBtn())
        state = SystemState.setStete(message.chat.id,"RegNumber", message.text)
    else:
        bot.send_message(message.from_user.id,"Не понятно что это, не похоже на цифры!",reply_to_message_id=message.id)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    logging.warning("Вызван collback на текст {0} с типом {1} пользователем {2}".format(callback.message.reply_to_message.text,callback.data,callback.message.from_user.full_name))
    arrsubSystem=[]
    if(str(callback.data).startswith("callback_type")):
        typeDoc = re.search(r'callback_type_(.*)', callback.data).group(1)
        SystemState.setStete(callback.message.chat.id, "Type", typeDoc)
        if typeDoc == 'ALL': arrsubSystem.append(["RGK", "RPEC", "RPGZ", "PRIZ", "PRIZ", "PRIZP", "RRK"])
        else:  arrsubSystem.append(typeDoc)
        nameFile = GetFileArchive.getFile(apiGetContractByReestr.getDocsSpecType(callback.message.reply_to_message.text, arrsubSystem))
        if(len(nameFile)!=0):
            #nameFile = fileManager.killSig(nameFile)
            #Удаляем сиги,перекладывааем всё в 1 архив, получаем перечень файлов
            newNameFileAndArrayType = fileManager.killSigAndAddToOneZIP(nameFile,callback.message.reply_to_message.text,callback.message.reply_to_message.text)
            SystemState.setStete(callback.message.chat.id, "Path", newNameFileAndArrayType[0])
            newMarkup=botHelper.createNewMarkup(newNameFileAndArrayType[1],typeBtn="kind")
            bot.send_message(
                         text="уточни!",
                         chat_id=callback.message.chat.id,
                         reply_to_message_id=callback.message.reply_to_message.id,
                         reply_markup=newMarkup )
            logging.warning("Отдаем кнопки с уточнением вида")
        else:
            bot.send_message(callback.message.chat.id, "ничего не найдено", reply_to_message_id=callback.message.reply_to_message.id)


    elif(str(callback.data).startswith("kind_")):
        kind = re.search(r'kind_(.*)', callback.data).group(1)
        logging.warning("Пользователь {0} интересуется видом {1}".format(callback.message.from_user.full_name,kind))
        SystemState.setStete(callback.message.chat.id, "Kind", kind)
        sysUser = SystemState.getStete(callback.message.chat.id)
        pattToNewFileWithOnlyKind = fileManager.getNameFileConcretKind(sysUser)
        #пока отдаем без уточнений
        media = []
        streams = []
        openfile = open(pattToNewFileWithOnlyKind, "rb")
        streams.append(openfile)
        media.append(telebot.types.InputMediaDocument(media=openfile))
        if len(media) == 0:
            bot.send_message(callback.message.chat.id, "ничего не найдено", reply_to_message_id=callback.message.reply_to_message.id)
        else:
            bot.send_media_group(chat_id=callback.message.chat.id, media=media, reply_to_message_id=callback.message.reply_to_message.id)
        #потоки закрываем
        for s in streams:
            s.close()
        fileManager.Summon_Mr_Proper(pattToNewFileWithOnlyKind)

bot.polling(non_stop=True, interval=0)
print("press any key")

'''
          #Дальнейший код имеет смысл если мы отдаем архивами по 100, если будем сувать всё в 1 архив и отдавать по типам то в этом смысла нет
  для тестирования эту часть пока скорем
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
'''