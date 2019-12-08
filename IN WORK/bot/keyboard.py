from telebot import types
from bot.function import *

def sub():
    activities_kbd = types.InlineKeyboardMarkup()
    acts = getacts()
    kacts = []
    n = len(acts)+1
    #for i in range(1, n, 1):
    #   kacts.append(types.InlineKeyboardButton(text=acts[i], callback_data=acts[i]))
    #activities_kbd.add(*kacts)

def send_message_kbd():
    acts = getacts()
    actss = []
    k = len(acts)
    send_kbd = types.InlineKeyboardMarkup()
    for i in range(0, k):
        actss.append(types.InlineKeyboardButton(text=acts[i], callback_data=acts[i]))
    send_kbd.add(types.InlineKeyboardButton("Всем", callback_data='everyone'))
    send_kbd.add(*actss)
    return send_kbd

def del_act_kb(): # Высвечивает все активности для удаления
    acts = getacts()
    actss = []
    k = len(acts)
    del_kbd = types.InlineKeyboardMarkup()
    for i in range(0, k):
        actss.append(types.InlineKeyboardButton(text=acts[i], callback_data=acts[i]))
    del_kbd.add(*actss)
    return del_kbd

def p_k(): #pupil
    pupil_kbd = types.ReplyKeyboardMarkup()
    row1 = types.KeyboardButton("Покажи мои активности")
    row2 = types.KeyboardButton("Подписаться на активность")
    pupil_kbd.row(row1)
    pupil_kbd.row(row2)
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