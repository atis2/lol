import telebot # библиотека telebot
from config import token # импорт токена

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! я люблю банить!")

# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     if message.text == "https://":
#         chat_id = message.chat.id # сохранение id чата
#          # сохранение id и статуса пользователя, отправившего сообщение
#         user_id = message.from_user.id
#         user_status = bot.get_chat_member(chat_id, user_id).status 
#          # проверка пользователя
#         if user_status == 'administrator' or user_status == 'creator':
#             bot.reply_to(message, "Невозможно забанить администратора.")
#         else:
#             bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
#             bot.reply_to(message, f"Пользователь @{message.from_user.username} был otpravlen k babuzke.")
#             bot.send_sticker(chat_id, "CAACAgIAAxkBAAEsaJVmirlCMze1jZRG-HWWjw_K169lAQACpjQAAji2uEqk-zFPA8ARczUE")

@bot.message_handler(commands=['unban'])
def unban(message):
    if message.reply_to_message:
        chat_id = message.chat.id 
        user_id = message.reply_to_message.from_user.id
        bot.unban_chat_member(chat_id, user_id) 
        bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} priexal obratno.")


@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        chat_id = message.chat.id # сохранение id чата
         # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был otpravlen k babuzke.")
            bot.send_sticker(chat_id, "CAACAgIAAxkBAAEsaJVmirlCMze1jZRG-HWWjw_K169lAQACpjQAAji2uEqk-zFPA8ARczUE")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")

bot.infinity_polling(none_stop=True)
