import telebot
from bot.keyboard import *
from bot.config import TG_TOKEN

bot = telebot.TeleBot(f'{TG_TOKEN}')
man = "admin"

@bot.message_handler(content_types=['text'])
def main(message):
    user_id = message.from_user.id
    #man = identefication(user_id)

    if man == 'admin':
        admin_func(message)

    elif man == 'pupil':
        pupil_func(message)

    else:
        null_func(message)

def admin_func(message): # Работа с учителем
    admin_keyboard = keyboard_admin()
    bot.send_message(message.from_user.id, text="Здраствуйте! Что вы хотели бы сделать?", reply_markup=admin_keyboard)
    if message.text == '/add_activity':
        bot.register_next_step_handler(message, add_activity)
    elif message.text == '/activities':
        pass
    elif message.text == '/add_access':
        pass # сгенирировать код
    elif message.text == '/del_activity':
        pass # удалить активность

def pupil_func(message):
    pupil_keyboard = keyboard_pupil()
    if message.text == '/start':
        bot.send_message(message.from_user.id, text="Привет!", reply_markup=pupil_keyboard)
    elif message.text == '/subscribe':
        pupil_change_act = keyboard_pupil_change()
        bot.send_message(message.from_user.id,text="Выбери активности которые тебе интересны!", reply_markup=pupil_change_act)
    elif message.text == '/shownews':
        pass # Вывести все новости по подпискам

def null_func(message): # хз кто такой
    bot.send_message(message.from_user.id, text="Привет, тебя нет в базе. Введи код, который тебе выдали.")
    input_code = message.text

def identefication(id):
    pass

def add_activity(message):
    bot.send_message(message.from_user.id, text="Введите название активности:")

    name = message.text
    print(name)

bot.polling(none_stop=True, interval=0)
