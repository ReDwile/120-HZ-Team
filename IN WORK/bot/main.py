from bot.function import *
from bot.keyboard import *

Man = Person

del_act_kbd = del_act_kb()
pupil_kbd = p_k()
admin_kbd = a_k()
nn_kbd = n_k()
sendkbd = send_message_kbd()
activities_kbd = sub()
desub_kbd = desub()

@bot.message_handler(commands=['start'])  # Тут все ок и работает
def start(message):
    Man.ID = message.from_user.id
    Man.man = identy(Man.ID)

    if Man.man == "pupil":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=pupil_kbd)
    elif Man.man == "noname":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=nn_kbd)
    elif Man.man == "admin":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=admin_kbd)

@bot.message_handler(content_types=['text'])
def text(message):
    Man.ID = message.from_user.id
    Man.man = identy(Man.ID)
    if Man.man == "noname":
        nn_f(message, Man)
    else:
        Man.acts = GetUserActs(Man.ID)
        Man.name = getnames(Man.ID)
        Man.lastname = getSnames(Man.ID)
        if Man.man == "admin":
            admin_f(message, Man)
        elif Man.man == "pupil":
            pupil_f(message, Man)


def nn_f(message, Man):
    if message.text == "Регистрация":  #Регистрация ноунэйма(работает)
            bot.send_message(Man.ID, text="Введи код приглашения")
            bot.register_next_step_handler(message, checkcode)


def pupil_f(message, Man):
    if message.text == "Покажи мои активности":  # Вроде работает
        try:
            bot.send_message(Man.ID,  '\n'.join(GetUserActs(Man.ID)),reply_markup=startkbd )
        except:
            bot.send_message(Man.ID, "У тебя нет активностей!")

    elif message.text == "Подписаться на активность": # Работает
        bot.send_message(Man.ID, text="Держи!\n\n", reply_markup=activities_kbd)
        bot.register_next_step_handler(message, subscribe)

    elif message.text == "Отписаться от активности":
        bot.send_message(Man.ID, text="Выбери активности от которых хочешь отписаться:", reply_markup=desub_kbd)
        bot.register_next_step_handler(message, desub)


def admin_f(message, Man):
    if message.text == "Добавить активность":  # Работает
        bot.send_message(Man.ID, text="Введите название:")
        bot.register_next_step_handler(message, add_act)

    elif message.text == "Удалить активность":   # Работает
        bot.send_message(Man.ID, "Выберите активность, которую хотите удалить:", reply_markup=del_act_kbd)
        bot.register_next_step_handler(message, del_act)

    elif message.text == "Посмотреть активности":  # С багом, но работает
        try:
            bot.send_message(Man.ID, '\n'.join(getacts()), reply_markup=startkbd)
        except:
            bot.send_message(Man.ID, "Активностей нет!")

    elif message.text == "Отправить сообщение":  #Работает
        bot.send_message(Man.ID, "Какой группе вы хотите отправить сообщение?:", reply_markup=sendkbd)
        bot.register_next_step_handler(message, send)



bot.polling(none_stop=True)
