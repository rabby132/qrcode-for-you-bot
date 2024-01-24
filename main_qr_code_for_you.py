from needed_modules import *
from functions import *
from log import *

bot = telebot.TeleBot(6836264981:AAGd2EPZXoHuZK4B5TxjcgbcwgBnFUtE8w8)

@bot.message_handler(commands=['start'])
def start_sent(message):
    log(f"{Dogbot Dwonloder} log:\n\nstart command received from user {message.chat.id}")
    bot.send_message(message.chat.id, \
                        start_cmd_msg, \
                        disable_web_page_preview=True)

@bot.message_handler(commands=['help'])
def help_sent(message):
    log(f"{Dogbot Dwonloder} log:\n\nhelp command received from user {message.chat.id}")
    bot.send_message(message.chat.id, \
                        help_cmd_msg, \
                        disable_web_page_preview=True)

@bot.message_handler(func=lambda message: True)
def send_qr(message):
    log(f"{bot_name} log:\n\nText from user {message.chat.id}:\n\n{message.text}")
    generate_qr(message.chat.id, message.text)
    output_file_path = f"{output_folder}/{message.chat.id}.png"
    with open(output_file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, \
                        photo, \
                        # reply_to_message_id=message.message_id, \
                        caption = f"{bot_username}\n\n{message.text}")
    
bot.infinity_polling()
