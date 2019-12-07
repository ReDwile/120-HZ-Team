from bot.main import *
from bot.keyboard import *

bot = telebot.TeleBot(f'{TG_TOKEN}')

@bot.message_handler(content_types=['text'])
def text(message):
    Man = Person()
    Man.ID = message.from_user.id
    Man.man = identy(Man.ID)
    if Man.man == "noname"
        Man.name = message.from_user.first_name
        Man.lastname = message.from_user.lastname
    else:
        Man.acts = GetUserActs(Man.ID)

        temp = GetNames(Man.ID).split(',')

        Man.name = temp[0]
        Man.lastname = temp[1]


    if message.text == "Регистрация":  #Регистрация ноунэйма
        if Man.man != "noname":
            bot.send_message(Man.ID, text="Ты уже зарегистрирован!")
        else:
            bot.send_message(Man.ID, text="Введи код приглашения")

    elif message.text[0] == "$":
        if Man.man != "noname":
            bot.send_message(Man.ID, text="Ты уже зарегистрирован!")
        elif message.text == codegen():
            todb(Man.ID, Man.name, Man.lastname)
            bot.send_message(Man.ID, text="Поздравляю, ты зарегистрирован!")
        else:
            bot.send_message(Man.ID, text="Ты ввел неверный код!")

    elif message.text == "Покажи мои активности":
        stru = '\n'.join(Man.acts)
        bot.send_message(Man.ID, text=f"{stru}")

    elif message.text == "Подписаться на активность":
        bot.send_message(Man.ID, text="Держи!\n\n", reply_markup=activities_kbd)

    elif message.text[0] == "/":
        actname = message.text[1:]
        subscribe(Man.ID, actname)










