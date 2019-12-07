import telebot
from bot.classes import *
from bot.config import *
from bot.functions import *



telebot.apihelper.proxy = {'https': 'socks5://geek:socks@t.geekclass.ru:7777'}

def polling():
    bot.polling(none_stop=True)



