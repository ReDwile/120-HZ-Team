from telebot import types
from bot.main import *

item =[]
activities_kbd = types.ReplyKeyboardMarkup()
acts = getacts()
n = len(acts) - 1
for i in range(0, n, 1):
    item[i] = '/' + types.ReplyKeyboardMarkup(f'{acts[i]}')
    activities_kbd.row(item[i])
