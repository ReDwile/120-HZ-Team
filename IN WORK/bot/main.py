import telebot
from bot.classes import *
from bot.keyboard import *
from bot.function import *
from telebot import apihelper

#sendkbd = send_message_kbd()
del_act_kbd = del_act_kb()
pupil_kbd = p_k()
admin_kbd = a_k()
nn_kbd = n_k()
sendkbd = send_message_kbd()

@bot.message_handler(commands=['start'])  # Тут все ок и работает
def start(message):
    Man = Person()
    Man.ID = message.from_user.id
    Man.man = identy(Man.ID)

    if Man.man == "noname":
        Man.name = message.from_user.first_name
        Man.lastname = message.from_user.last_name
    else:
        Man.acts = GetUserActs(Man.ID)
        temp = getnames(Man.ID).split(',')
        Man.name = getnames(Man.ID)
        Man.lastname = getSnames(Man.ID)

    if Man.man == "pupil":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=pupil_kbd)
    elif Man.man == "noname":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=nn_kbd)
    elif Man.man == "admin":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=admin_kbd)

@bot.message_handler(content_types=['text'])
def text(message):
    Man = Person()
    Man.ID = message.from_user.id
    Man.man = identy(Man.ID)
    if Man.man == "noname":
        Man.name = message.from_user.first_name
        Man.lastname = message.from_user.last_name
    else:
        Man.acts = GetUserActs(Man.ID)
        Man.name = getnames(Man.ID)
        Man.lastname = getSnames(Man.ID)
###############################################################################
    if Man.man == "noname":
        if message.text == "Регистрация":  #Регистрация ноунэйма(работает)
                bot.send_message(Man.ID, text="Введи код приглашения")

        elif message.text[0] == "$":  # Работает
            if Man.man != "noname":
                bot.send_message(Man.ID, text="Ты уже зарегистрирован!")
            elif message.text == codegen():
                todb(Man.ID, Man.name, Man.lastname)
                bot.send_message(Man.ID, text="Поздравляю, ты зарегистрирован!")
            else:
                bot.send_message(Man.ID, text="Ты ввел неверный код!")
#######################################################################################
    if Man.man == "pupil":
        if message.text == "Покажи мои активности":  # Вроде работает
            try:
                bot.send_message(Man.ID,  '\n'.join(GetUserActs(Man.ID)))
            except TypeError:
                bot.send_message(Man.ID, "У тебя нет активностей!")

        elif message.text == "Подписаться на активность": # В рвзработке
            bot.send_message(Man.ID, text="Держи!\n\n", reply_markup=activities_kbd)
            bot.register_next_step_handler(message, subscribe)
######################################################################################
    if Man.man == "admin":
        if message.text == "Добавить активность":  # Работает
            bot.send_message(Man.ID, text="Введите название:")
            bot.register_next_step_handler(message, add_act)

        elif message.text == "Удалить активность":   # Пока крашится
            bot.send_message(Man.ID, "Выберите активность, которую хотите удалить:", reply_markup=del_act_kbd)
            bot.register_next_step_handler(message, del_act)

        elif message.text == "Посмотреть активности":  # С багом, но работает
            try:
                bot.send_message(Man.ID, '\n'.join(getacts()))
            except:
                bot.send_message(Man.ID, "Прости! Я опять сломался :( Но надеюсь скоро починят)")

        elif message.text == "Отправить сообщение": # Пока крашится
            bot.send_message(Man.ID, "Какой группе вы хотите отправить сообщение?:", reply_markup=sendkbd)
            bot.register_next_step_handler(message, send)

bot.polling(none_stop=True)



