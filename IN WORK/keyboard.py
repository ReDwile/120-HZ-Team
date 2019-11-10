from telebot import types

def keyboard_admin():
    keyboard = types.InlineKeyboardMarkup()
    key_add_act = types.InlineKeyboardButton(text="Добавить активность", callback_data="/add_activity")
    keyboard.add(key_add_act)
    key_activities = types.InlineKeyboardButton(text="Показать все активности", callback_data="/activities")
    keyboard.add(key_activities)
    key_add_access = types.InlineKeyboardButton(text="Сгенирировать ключ доступа", callback_data="/add_access")
    keyboard.add(key_add_access)
    key_del_act = types.InlineKeyboardButton(text="Удалить активность", callback_data="/del_activity")
    keyboard.add(key_del_act)
    return keyboard

def keyboard_pupil():
    keyboard = types.InlineKeyboardMarkup()
    subscribe_button = types.InlineKeyboardButton(text="Подписаться на новости", callback_data="/subcribe")
    keyboard.add(subscribe_button)
    news_button = types.InlineKeyboardButton(text="Посмотреть текущие новости по подпискам", callback_data="/shownews")
    keyboard.add(news_button)
    return keyboard

def keyboard_pupil_change():
    pass

