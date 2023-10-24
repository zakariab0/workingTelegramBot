import os
import telebot

bot = telebot.TeleBot('6911546574:AAEg8NM0NMcagHlzEbJEWeYyRz7h0cQKuHI')
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "didikas l omar zbda")
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()
