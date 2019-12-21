from bot.function import *
from bot.keyboard import *

pupil_kbd = p_k()
admin_kbd = a_k()
nn_kbd = n_k()

@bot.message_handler(commands=['start'])  # Тут все ок и работает
def start(message):
    Man = MansDataBase()

    Man.ID = message.from_user.id
    Man.man = Man.identy(Man.ID)

    if Man.man == "pupil":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=pupil_kbd)
    elif Man.man == "noname":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=nn_kbd)
    elif Man.man == "admin":
        bot.send_message(Man.ID, text="Вот функции, доступные тебе:", reply_markup=admin_kbd)

@bot.message_handler(content_types=['text'])
def text(message):
    Man = MansDataBase()

    Man.ID = message.from_user.id
    Man.man = Man.identy(Man.ID)
    if Man.man == "noname":
        nn_f(message, Man)
    else:
        Man.acts = Man.GetUserActs(Man.ID)
        Man.name = Man.getnames(Man.ID)
        Man.lastname = Man.getSnames(Man.ID)
        if Man.man == "admin":
            admin_f(message, Man)
        elif Man.man == "pupil":
            pupil_f(message, Man)


def nn_f(message, Man):
    Code = CodeCheck()

    if message.text == "Регистрация":  #Регистрация ноунэйма(работает)
            bot.send_message(Man.ID, text="Введи код приглашения")
            bot.register_next_step_handler(message, Code.checkcode)


def pupil_f(message, Man):
    activities_kbd = sub()
    desub_kbd = desub_k(Man.ID)
    if Man.man == "pupil":
        if message.text == "Покажи мои активности":  # Вроде работает
            try:
                bot.send_message(Man.ID,  '\n'.join(Man.GetUserActs(Man.ID)), reply_markup=startkbd )
            except:
                bot.send_message(Man.ID, "У тебя нет активностей!")

        elif message.text == "Подписаться на активность": # Работает
            bot.send_message(Man.ID, text="Держи!\n\n", reply_markup=activities_kbd)
            bot.register_next_step_handler(message, Man.subscribe)

        elif message.text == "Отписаться от активности":
            bot.send_message(Man.ID, text="Выбери активности от которых хочешь отписаться:", reply_markup=desub_kbd)
            bot.register_next_step_handler(message, Man.desub)

        elif message.text == "Привязать/Изменить ВК":
            bot.send_message(Man.ID, text="Введи ID который двл тебе бот ВК:")
            bot.register_next_step_handler(message, Man.addVk)

def admin_f(message, Man):
    Acts = ActsDataBase()
    sendmsg = SendMessage()
    del_act_kbd = del_act_kb()
    sendkbd = send_message_kbd()
    if Man.man == "admin":
        if message.text == "Добавить активность":  # Работает
            bot.send_message(Man.ID, text="Введите название:")
            bot.register_next_step_handler(message, Acts.add_act)

        elif message.text == "Удалить активность":   # Работает
            bot.send_message(Man.ID, "Выберите активность, которую хотите удалить:", reply_markup=del_act_kbd)
            bot.register_next_step_handler(message, Acts.del_act)

        elif message.text == "Посмотреть активности":  # С багом, но работает
            try:
                bot.send_message(Man.ID, '\n'.join(Acts.getallacts()), reply_markup=startkbd)
            except:
                bot.send_message(Man.ID, "Активностей нет!")

        elif message.text == "Отправить сообщение":  #Работает
            bot.send_message(Man.ID, "Какой группе вы хотите отправить сообщение?:", reply_markup=sendkbd)
            bot.register_next_step_handler(message, sendmsg.send)


bot.polling(none_stop=True)

CodeGen().checkdate()