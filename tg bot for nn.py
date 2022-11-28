import telebot
import cv2
import time
import logging

token = '5478353034:AAGQ5cFEBHgHVh8YT345aKRYwcNO0AgbJ3g' #подключаем токен бота с помощью токена, полученного от BotFather
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start']) 

def start_message(message): #при нажатии команды /start, бот вежливо здоровается, назвав нас по имени
    #ёщё он предлагает список своих услуг
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}', time.asctime())
    bot.send_message(message.chat.id,f"приветствую, {user_full_name}! ✌")
    bot.send_message(message.chat.id, "отправь мне фотографию, на которой я постараюсь отыскать лица! 😛")
@bot.message_handler(content_types=['photo'])
def get_img_message(message): #зададим функцию, цели которой будет реакция бота на полученное изображение
    image_path = message.photo
    bot.send_message(message.from_user.id, "Принято! 🤗")
  
bot.infinity_polling()
