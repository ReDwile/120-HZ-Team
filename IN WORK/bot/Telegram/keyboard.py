from telebot import types

AdminTexts = getText("admin")
PupilTexts = getText("pupil")
NonameTexts = getText("noname")
OthersTexts = getText("other")

def backkbd():
    backkbd = types.ReplyKeyboardMarkup()
    backkbd.add("Назад")
    return backkbd

class TGkeyboards(object):

    def __init__(self):

        from modules.function import ActsDataBase
        self.Acts = ActsDataBase()
        from modules.function import MansDataBaseTG
        self.Man = MansDataBaseTG()


class AdminTGkeyboards(TGkeyboards):

    def send_message_kbd(self):
        acts = self.Acts.getallacts()
        k = len(acts)
        send_kbd = types.ReplyKeyboardMarkup()
        rowb = types.KeyboardButton("Назад")
        send_kbd.add(rowb)
        row = types.KeyboardButton("Всем")
        send_kbd.add(row)
        for i in range(0, k):
            row = types.KeyboardButton(f'{acts[i]}')
            send_kbd.add(row)
        return send_kbd

    def del_act_kb(self):  # Высвечивает все активности для удаления
        acts = self.Acts.getallacts()
        k = len(acts)
        del_kbd = types.ReplyKeyboardMarkup()
        rowb = types.KeyboardButton("Назад")
        del_kbd.add(rowb)
        for i in range(0, k):
            row = types.KeyboardButton(f'{acts[i]}')
            del_kbd.add(row)
        return del_kbd

    @staticmethod
    def admin_k():  # admin
        admin_kbd = types.ReplyKeyboardMarkup()
        rowa1 = types.KeyboardButton(AdminTexts.gettext("Добавление активности"))
        rowa2 = types.KeyboardButton(AdminTexts.gettext("Удаление активности"))
        rowa3 = types.KeyboardButton(AdminTexts.gettext("Просмотр активностей"))
        rowa4 = types.KeyboardButton(AdminTexts.gettext("Отправка сообщения"))
        rowa5 = types.KeyboardButton(AdminTexts.gettext("Получить код"))
        admin_kbd.row(rowa1)
        admin_kbd.row(rowa2)
        admin_kbd.row(rowa3)
        admin_kbd.row(rowa4)
        admin_kbd.row(rowa5)
        return admin_kbd

class PupilTGkeyboards(TGkeyboards):

    def desub_k(self, ID):
        activities_kbd = types.ReplyKeyboardMarkup()
        acts = self.Man.GetUserActs(ID)
        k = len(acts)
        rowb = types.KeyboardButton("Назад")
        activities_kbd.add(rowb)
        row = types.KeyboardButton("Отписаться от всех активностей")
        activities_kbd.add(row)
        for i in range(0, k):
            row = types.KeyboardButton(f'{acts[i]}')
            activities_kbd.add(row)
        return activities_kbd

    def sub(self):

        activities_kbd = types.ReplyKeyboardMarkup()
        acts = self.Acts.getallacts()
        k = len(acts)
        rowb = types.KeyboardButton("Назад")
        activities_kbd.add(rowb)
        for i in range(0, k):
            row = types.KeyboardButton(f'{acts[i]}')
            activities_kbd.add(row)
        return activities_kbd
    @staticmethod
    def p_k():  # pupil
        pupil_kbd = types.ReplyKeyboardMarkup()
        row1 = types.KeyboardButton(PupilTexts.gettext("Показать активности"))
        row2 = types.KeyboardButton(PupilTexts.gettext("Подписка на активность"))
        row3 = types.KeyboardButton(PupilTexts.gettext("Отписка от активности"))
        row4 = types.KeyboardButton(PupilTexts.gettext("Изменение данных"))
        pupil_kbd.row(row1)
        pupil_kbd.row(row2)
        pupil_kbd.row(row3)
        pupil_kbd.row(row4)
        return pupil_kbd

class NonameTGKeyboards(TGkeyboards):
    @staticmethod
    def n_k(): #noname
        nn_kbd = types.ReplyKeyboardMarkup()
        row3 = types.KeyboardButton("Регистрация")
        nn_kbd.row(row3)
        return nn_kbd