import telebot
from bot.keyboard import *
from bot.config import TG_TOKEN
from bot.admin_functions import *

bot = telebot.TeleBot(f'{TG_TOKEN}')

def identefication(id):
    pass

# Начало работы с учителем (admin)
@bot.message_handler(commands=['add_activity']) # Добавляем активность
def add_activity(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'admin':
        bot.send_message(
            user_id,
            text="Введите название активности:")
        pass
    else:
        bot.send_message(user_id, text="У вас нет прав на выполнение данной операции!")

@bot.message_handler(commands=['activities']) # Показываем все активности
def list_acts(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'admin':
        pass
    else:
        bot.send_message(user_id, text="У вас нет прав на выполнение данной операции!")

@bot.message_handler(commands=['add_access']) # Даем доступ ученику
def add_access(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'admin':
        pass
    else:
        bot.send_message(user_id, text="У вас нет прав на выполнение данной операции!")

@bot.message_handler(commands=['del_activity']) # Удаляем активность
def del_activity(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'admin':
        pass
    else:
        bot.send_message(user_id, text="У вас нет прав на выполнение данной операции!")
# Конец работы с учителем (admin)
#
# Начало работы с учеником(pupil)
@bot.message_handler(commands=['subscribe']) # Подписаться на мероприятие
def subscribe(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'pupil':
        pass
    else:
        bot.send_message(user_id, text="У вас нет прав на выполнение данной операции!")

@bot.message_handler(commands=['shownews']) # Показать новости по подпискам
def shownews(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'pupil':
        pass
    else:
        bot.send_message(user_id, text="У вас нет прав на выполнение данной операции!")
# Конец работы с учеником (pupil)
#
# Начало работы с ноунэймом (noname)
@bot.message_handler(commands=['enter'])
def enter(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'noname':
        bot.send_message(message.from_user.id, text="Введи код, который тебе дала вожатая")
        pass
    else:
        bot.send_message(user_id, text="Ты уже авторизован!")
# Конец работы с ноунэймом (noname)
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    man = identefication(user_id)

    if man == 'admin':
        admin_keyboard = keyboard_admin()
        bot.send_message(message.from_user.id, text="Здраствуйте! Что вы хотели бы сделать?", reply_markup=admin_keyboard)

    elif man == 'pupil':
        pupil_keyboard = keyboard_pupil()
        bot.send_message(message.from_user.id, text="Привет!", reply_markup=pupil_keyboard)
    else:
        noname_keyboard = noname_kbd()
        bot.send_message(message.from_user.id, text="Привет, тебя нет в базе. Нажми на кнопку ниже для аутентификации.",reply_markup=noname_keyboard)

bot.polling(none_stop=True, interval=0)
