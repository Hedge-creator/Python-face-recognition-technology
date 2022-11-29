import telebot
import time
import logging
from telebot import types

token = '5478353034:AAGQ5cFEBHgHVh8YT345aKRYwcNO0AgbJ3g' #подключаем токен бота с помощью токена, полученного от BotFather
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start']) 

def start_message(message): #при нажатии команды /start, бот вежливо здоровается, назвав нас по имени
    #ёщё он предлагает список своих услуг
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сравнение лиц на схожесть")
    item2 = types.KeyboardButton("Поиск лиц на фотографии")
    item3 = types.KeyboardButton("Возраст человека, пол, раса")

    markup.add(item1, item2, item3)

    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}', time.asctime())
    
    bot.send_message(message.chat.id,f"приветствую, {user_full_name}! ✌", reply_markup=markup)
@bot.message_handler(content_types=['photo'])
def get_img_message(message): #зададим функцию, цели которой будет реакция бота на полученное изображение
    image_path = message.photo
    bot.send_message(message.from_user.id, "Принято! 🤗")
  
bot.polling(none_stop=True)
