import datetime


def time_show(string): # разделяет время
    array = string.split()
    time = array[3].split(':')
    data = {
        "year": array[4],
        "month": array[1],
        "day": int(array[2]),
        "hour": int(time[0]),
        "minute": int(time[1]),
        "seconds": int(time[2])
    }
    return data

def time_now():  # эта функция  выдаёт словарь с данными текущего времени
    time = datetime.datetime.now()
    time_dict = time_show(time)
    return time_dict

with open('puple.txt', 'a') as f:
    print(f.read())


def identification(id): # в этой функции мы сравниваем входящий id и id админа и учеников
    with open('admin.txt', 'r') as f:
        admin = f.read()


    with open('puple.txt', 'r') as g:
        studens_arrays = g.read().split(',')

    man = 'null'
    if id == admin:
        man = 'admin'
    elif id in studens_arrays:
        man = 'puple'
    return man

with open('puple.txt', 'a') as f:
    print(f.read())