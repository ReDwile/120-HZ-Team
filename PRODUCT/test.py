import PySimpleGUI as sg
import re
import hashlib

def hash(fname,algo):
    if algo=='MD5':
        hash = hashlib.md5()
    elif algo =='SHA1':
        hash = hashlib.sha1()
    elif algo =='SHA256':
        hash = hashlib.sha256()

    with open(fname) as handle:
        for line in handle:
            hash.update(line.encode(encoding='utf-8'))

    return (hash.hexdigest())


layout =[
    [sg.Text('File 1'), sg.InputText(), sg.FileBrowse(), sg.Checkbox('MD5'), sg.Checkbox('SHA1')],
    [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(), sg.Checkbox('SHA256')],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('File Compare', layout)

while True:
    event, values = window.read()
    if event in(None,'Exit','Cancel'):
        break
    if event == 'Submit':
        file1 = file2 = isitago = None

        if values[0] and values[3]:
            file1=re.findall('.+:\/.+\.+.', values[0])
            file2=re.findall('.+:\/.+\.+.', values[3])
            isitago = 1

            if not file1 and file1 is not None:
                print("путь до файла 1")

