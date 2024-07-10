import logging
import  time
import  telebot
import apiGetContractByReestr
import  GetFileArchive
logging.basicConfig(level=logging.WARNING)
#читаем токен с файла
fileToken = open('token','r')
token = fileToken.readline()
fileToken.close()
logging.debug(token)
# определяем бота
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    logging.warning("Обратился пользователь " + message.from_user.full_name+", хочет знать про "+ message.text)
    if len(message.text) == 19:
       returnText =  apiGetContractByReestr.getContract(message.text)
       #time.sleep(10)
       nameFile = GetFileArchive.getFile(returnText)
       for name in nameFile:
           logging.warning("name"+name)
           f = open(name,'rb')
           bot.send_document(message.from_user.id, f)
           f.close()
       if len(nameFile)==0:
        bot.send_message(message.from_user.id, "ничего не найдено")


    elif message.text == '12345':
        bot.send_message(message.from_user.id,"67890")
    else:
        bot.send_message(message.from_user.id,"ответ на неизвесно что")

bot.polling(non_stop=True, interval=0)

print("press any key")
