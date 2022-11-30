import telebot
import time
import logging
from telebot import types

token = '5478353034:AAGQ5cFEBHgHVh8YT345aKRYwcNO0AgbJ3g' #подключаем токен бота с помощью токена, полученного от BotFather
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start']) 

def start_message(message): #при нажатии команды /start, бот вежливо здоровается, назвав нас по имени
    #ёщё он предлагает список своих услуг

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Поиск лиц")
    item2 = types.KeyboardButton("Возраст, пол, раса")

    markup.add(item1, item2)

    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}', time.asctime())
    
    bot.send_message(message.chat.id,f"Приветствую, {user_full_name}! ✌", reply_markup = markup)

@bot.message_handler(content_types=['text'])

def get_text_message(message):

    if message.text == 'Поиск лиц':
        bot.send_message(message.chat.id, "Пожалуйста, отправь фотографию для анализа 😛")

    elif message.text == 'Возраст, пол, раса':
        bot.send_message(message.chat.id, "Пожалуйста, отправь фотографию для анализа 😛")

    else:
        bot.send_message(message.chat.id, "Я не поняла команду 😕")


bot.infinity_polling()
