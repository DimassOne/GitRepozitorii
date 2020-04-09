import telebot
import tokkken
from telebot import types
import pprint

bot = telebot.TeleBot(tokkken.tok)
user = bot.get_me()
@bot.message_handler(commands=['start'])
def srart(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Фото')
    btn2 = types.KeyboardButton('message')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Hello", reply_markup=markup)
@bot.message_handler(commands=['start','help'])
def mess(message):
    bot.send_message(message.chat.id, "Ну как дела, друг?")

@bot.message_handler(content_types=['sticker'])
def mes(message):
    bot.send_message(message.chat.id, message.text)



# @bot.message_handler(func=lambda message:True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

#
#
# # @bot.message_handler(commands=['start', 'help'])
@bot.message_handler(content_types=['text'])
def welkom(message):
    foto = open('foto.jpg', 'rb')
    if message.text == "Фото":
        bot.send_photo(message.chat.id, foto)
        bot.send_photo(message.chat.id, "FILEID")
    print('hello')
    #bot.reply_to(message, message.text)
    bot.reply_to(message, message.text)
#     bot.send_message(message.chat.id, "Ну как же так...")
#
@bot.message_handler(content_types=['audio'])
def audiofunc(message):
    # audio = open('')
    bot.send_message(message.chat.id, "Получи музончик")
#
# @bot.message_handler(content_types=['document'])
# def documentss(message):
#     bot.send_message(message.chat.id, 'Это текстовый файл')

if __name__ == '__main__':
    bot.polling(none_stop=True)
