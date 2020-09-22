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
                print("путь до файла 1 не найден")
            elif not file2 and file2 is not None:
                print("путь до файла 2 не найден")
            elif values[1] is not True and values[2] is not True and values[4] is not True:
                print("error")
            elif isitago == 1:
                print("path has benn finded")

                algos = []

                if values[1]==True:
                    algos.append('MD5')
                if values[2] == True:
                    algos.append('SHA1')
                if values[4] == True:
                    algos.append('SHA256')

                filepaths=[]
                filepaths.append(values[0])
                filepaths.append(values[3])

                print(f"programm using ${algos}")

                for algo in algos:
                    print(algo, ':')
                    print(filepaths[0],':',hash(filepaths[0],algo))
                    print(filepaths[1], ':', hash(filepaths[1], algo))

                    if hash(filepaths[0],algo) == hash(filepaths[1], algo):
                        print(f"files match for ${algo}")
                    else:
                        print("fauck you leatherman")