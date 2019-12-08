from openpyxl.utils import get_column_letter
from openpyxl import Workbook, load_workbook
import random
import telebot
from bot.classes import *
from bot.config import *

bot = telebot.TeleBot(f'{TG_TOKEN}')

ras = sm()

wb = load_workbook('Data/test.xlsx')
wbSearch=wb
wsSearch=wbSearch.active
lookfor_1="pupil"
lookfor_2="admin"
kolichestvo = wsSearch.max_row

def codegen():
    ran=random.randint(10000, 99999)
    return ran


def db():
    for sheet in wb:
        vals =[sheet.title]
    return vals

def GetUserActs(ID):
    kolichestvo = wsSearch.max_row + 1
    activities=[]
    zero=[]
    for i in range(1, kolichestvo):
        value = wsSearch.cell(row=i,column=1).value
        if value == ID:
            activities.append(wsSearch.cell(row=i, column=5).value)
            set(activities)
    if zero == activities:
        return None
    else:
        return activities

def getacts():
    kolichestvo = wsSearch.max_row + 1
    activities=[]
    for i in range(1,kolichestvo):
        value = wsSearch.cell(row=i, column=5).value
        if value != "":
            activities.append(value)
        set(activities)
    return activities

def getnames(ID):
    z = None
    name_status=None
    for i in range(1,kolichestvo+1):
        value=wsSearch.cell(row=i,column=1).value
        if value == ID:
            name_status=wsSearch.cell(row=i,column=3).value
    if name_status!=None:
        return name_status
    return z

def getSnames(ID):
    z = None
    lastname_status = None
    for i in range(1, kolichestvo + 1):
        value = wsSearch.cell(row=i, column=1).value
        if value == ID:
            lastname_status = wsSearch.cell(row=i, column=4).value
    if lastname_status != None:
        return lastname_status
    return z

def identy(ID):
    status = "noname"
    kolichestvo = wsSearch.max_row + 1
    for i in range(1,kolichestvo):
        value=wsSearch.cell(row=i,column=1).value
        if value == ID:
            status = wsSearch.cell(row=i,column=2).value
    return status

def subscribe(message):
    id = message.from_user.id
    activ = message.text
    kolichestvo = wsSearch.max_row + 1
    for i in range(1,kolichestvo):
        value=wsSearch.cell(row=i,column=1).value
        if value == id:
            value_activities=wsSearch.cell(row=i,column=5).value
            if value_activities == None:
                wsSearch.cell(row=i, column=5).value=activ
            elif value_activities != None:
                row = kolichestvo
                wsSearch.cell(row=i,column=5).value=activ
    wb.save("Data/test.xlsx")

def todb(ID, name, lastname):
    maxrow = wsSearch.max_row
    Row =maxrow+1
    wsSearch.cell(row=Row, column=1).value = ID
    wsSearch.cell(row=Row, column=2).value = "pupil"
    wsSearch.cell(row=Row, column=3).value = name
    wsSearch.cell(row=Row, column=4).value = lastname
    wb.save("Data/test.xlsx")

def add_act(message):
    name = message.text
    Row = wsSearch.max_row + 1
    wsSearch.cell(row = Row, column = 5).value = name
    wb.save("Data/test.xlsx")

def del_act(message):
    name = message.text
    cout = wsSearch.max_row + 1
    for i in range(1, cout):
        if wsSearch.cell(row=i, column=5).value == name:
            wsSearch.cell(row = i, column=5).value = ""
    wb.save("Data/test.xlsx")

def send(message):
    group = []
    gr = message.text
    Row = wsSearch.max_row + 1
    for i in range(1,Row):
        if wsSearch.cell(row = i, column=5).value == gr:
            group.append(wsSearch.cell(row = i, column=1).value)
        set(group)
    bot.send_message(message.from_user.id, "Введите сообщение:")
    bot.register_next_step_handler(message, send2)
    ras.group = group

def send2(message):
    ras.text = message.text
    for i in range(0, len(ras.group)):
        bot.send_message(ras.group[i], ras.text)



