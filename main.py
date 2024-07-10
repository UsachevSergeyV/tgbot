import logging
import  telebot
logging.basicConfig(level=logging.DEBUG)
#читаем токен с файла
fileToken = open('token','r')
token = fileToken.readline()
fileToken.close()
logging.debug(token)
# определяем бота
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '12345':
        bot.send_message(message.from_user.id,"67890")
    else:
        bot.send_message(message.from_user.id,"ответ на неизвесно что")

bot.polling(non_stop=True, interval=0)

print("press any key")
