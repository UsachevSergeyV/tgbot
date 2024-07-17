import telebot

def createNewMarkup(arrNameButton,typeBtn):
    markup = telebot.types.InlineKeyboardMarkup()
    for button in arrNameButton:
        markup.add(telebot.types.InlineKeyboardButton(text=button, callback_data=typeBtn+"_"+button))
    return markup

def firstBtn():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn1 = telebot.types.InlineKeyboardButton("Контракт", callback_data="callback_type_RGK")
    btn2 = telebot.types.InlineKeyboardButton('Закупка', callback_data="callback_type_PRIZ")
    btn3 = telebot.types.InlineKeyboardButton('План график', callback_data="callback_type_RPGZ")
    btn4 = telebot.types.InlineKeyboardButton('Проект контракта', callback_data="callback_type_RPEC")
   # btn5 = telebot.types.InlineKeyboardButton('Проверить ВСЁ', callback_data="callback_type_ALL")
    markup.add(btn1, btn2, btn3, btn4 )
    return  markup