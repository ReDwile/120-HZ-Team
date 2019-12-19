from telebot import types
from bot.function import *

def desub_k(ID):
    activities_kbd = types.ReplyKeyboardMarkup()
    acts = GetUserActs(ID)
    k = len(acts)
    row = types.KeyboardButton("Отписаться от всех активностей")
    activities_kbd.add(row)
    for i in range(0, k):
        row = types.KeyboardButton(f'{acts[i]}')
        activities_kbd.add(row)
    return activities_kbd

def sub():
    activities_kbd = types.ReplyKeyboardMarkup()
    acts = getacts()
    k = len(acts)
    for i in range(0, k):
        row = types.KeyboardButton(f'{acts[i]}')
        activities_kbd.add(row)
    return activities_kbd

def send_message_kbd():
    acts = getacts()
    k = len(acts)
    send_kbd = types.ReplyKeyboardMarkup()
    row = types.KeyboardButton("Всем")
    send_kbd.add(row)
    for i in range(0, k):
        row = types.KeyboardButton(f'{acts[i]}')
        send_kbd.add(row)
    return send_kbd

def del_act_kb(): # Высвечивает все активности для удаления
    acts = getacts()
    k = len(acts)
    del_kbd = types.ReplyKeyboardMarkup()
    for i in range(0, k):
        row = types.KeyboardButton(f'{acts[i]}')
        del_kbd.add(row)
    return del_kbd

def p_k(): #pupil
    pupil_kbd = types.ReplyKeyboardMarkup()
    row1 = types.KeyboardButton("Покажи мои активности")
    row2 = types.KeyboardButton("Подписаться на активность")
    row3 = types.KeyboardButton("Отписаться от активности")
    row4 = types.KeyboardButton("Привязать/Изменить ВК")
    pupil_kbd.row(row1)
    pupil_kbd.row(row2)
    pupil_kbd.row(row3)
    pupil_kbd.row(row4)
    return pupil_kbd

def a_k(): #admin
    admin_kbd = types.ReplyKeyboardMarkup()
    rowa1 = types.KeyboardButton("Добавить активность")
    rowa2 = types.KeyboardButton("Удалить активность")
    rowa3 = types.KeyboardButton("Посмотреть активности")
    rowa4 = types.KeyboardButton("Отправить сообщение")
    admin_kbd.row(rowa1)
    admin_kbd.row(rowa2)
    admin_kbd.row(rowa3)
    admin_kbd.row(rowa4)
    return admin_kbd

def n_k(): #noname
    nn_kbd = types.ReplyKeyboardMarkup()
    row3 = types.KeyboardButton("Регистрация")
    nn_kbd.row(row3)
    return nn_kbd