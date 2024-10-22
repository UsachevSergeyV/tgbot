import logging
import time
from datetime import date
import  telebot
import SystemState
import apiGetContractByReestr
import  GetFileArchive
import botHelper
import fileManager
import  re
from datetime import datetime, timezone

logging.basicConfig(
    level=logging.WARNING,
    filename="log/error/err",
    filemode='a',
    format="%(asctime)s %(levelname)s %(message)s")
fileToken = open('token','r')
token = fileToken.readline()
fileToken.close()

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    print("{2} - Пользователь {0} запросил информацию о {1}".format( message.from_user.full_name, message.text,datetime.now()))
    if message.text.isnumeric():
        bot.reply_to(message, text="Что это'?", reply_markup=botHelper.firstBtn())
        state = SystemState.setStete(message.chat.id,"RegNumber", message.text)
    elif message.text=="FFS":
        raise ("Ошибка")
    else:
        bot.send_message(message.from_user.id,"Не понятно что это, не похоже на цифры!",reply_to_message_id=message.id)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    print("{3} - Вызван collback на текст {0} с типом {1} пользователем {2}".format(callback.message.reply_to_message.text,callback.data,callback.from_user.full_name ,datetime.now()))
    arrsubSystem=[]
    if(str(callback.data).startswith("callback_type")):
        typeDoc = re.search(r'callback_type_(.*)', callback.data).group(1)
        SystemState.setStete(callback.message.chat.id, "Type", typeDoc)
        if typeDoc == 'ALL': arrsubSystem.append("RGK", "RPEC", "RPGZ", "PRIZ", "PRIZP", "RRK")
        else:  arrsubSystem.append(typeDoc)
        nameFile = GetFileArchive.getFile(apiGetContractByReestr.getDocsSpecType(callback.message.reply_to_message.text, arrsubSystem))
        if(len(nameFile)!=0):
            #nameFile = fileManager.killSig(nameFile)
            #Удаляем сиги,перекладывааем всё в 1 архив, получаем перечень файлов
            newNameFileAndArrayType = fileManager.killSigAndAddToOneZIP(nameFile,callback.message.reply_to_message.text,callback.message.reply_to_message.text)
            SystemState.setStete(callback.message.chat.id, "Path", newNameFileAndArrayType[0])
            newMarkup=botHelper.createNewMarkup(newNameFileAndArrayType[1],typeBtn="kind")
            newMarkup.add(telebot.types.InlineKeyboardButton(text="Скачать всё", callback_data="kind_all"))
            bot.send_message(
                         text="уточни!",
                         chat_id=callback.message.chat.id,
                         reply_to_message_id=callback.message.reply_to_message.id,
                         reply_markup=newMarkup )
        else:
            bot.send_message(callback.message.chat.id, "ничего не найдено", reply_to_message_id=callback.message.reply_to_message.id)


    elif(str(callback.data).startswith("kind_")):
        kind = re.search(r'kind_(.*)', callback.data).group(1)
        print("{2} - Пользователь {0} интересуется видом {1}".format(callback.from_user.full_name,kind, datetime.now()))
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
        fileManager.Summon_Mr_Proper_For_Delete_Single_File(pattToNewFileWithOnlyKind)


err=None

def zeroPoint():
    try:
        bot.polling(non_stop=True, interval=0)
    except Exception as e:
        time.sleep(2)
        logging.error("Бот упал. "+str(e))
        print("{0} - Бот упал. пробуем поднять".format(datetime.now()))
        zeroPoint()


zeroPoint()
print("press any key")
