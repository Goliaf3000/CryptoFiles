from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import *
from tkinter import filedialog as fd 
import encryption
import decryption
#при помощи кнопки добавляеи файлы
def callbackcryptfile():
    name = fd.askdirectory()
    entry.insert(0,name)

def callbackckey():
    name2 = fd.askopenfilename()
    entry2.insert(0,name2)



#вызываем расшифровку файла   
def encrypt():
    
    cryptfile =  entry.get()
    keyfile = entry2.get()    # передаем данные для шифровки файла
    password = entry3.get()
    text = encryption.get(cryptfile, keyfile, password)
    label["text"] = text
#вызываем шифровку файла   
def decrypt():
    
    cryptfile =  entry.get()
    keyfile = entry2.get()    # передаем данные для дешифровки файла
    password = entry3.get()
    text = decryption.get(cryptfile, keyfile, password)
    label["text"] = text
#выбираем чек боксом что хотим сделать 
def select():
    selection = var.get()
    if selection  == 1:
        encrypt()
    elif selection  == 2:
        decrypt()
root = Tk()
root.title("Crypt and DeCrypt")
root.geometry("300x350") 
root.maxsize(300, 350)
root.minsize(300, 350)
#кнопка выбора файла для шифра или дешифра
ttk.Button(text='Выберите путь к папке', command=callbackcryptfile).grid(column=0, row=1)
entry = ttk.Entry()
entry.grid(column=0, row=0, ipadx=50, ipady=5, sticky="n", padx = 30, pady = 15)



ttk.Button(text='Выберите путь к ключу', command=callbackckey).grid(column=0, row=4)
entry2 = ttk.Entry()
entry2.grid(column=0, row=3, ipadx=50, ipady=5, sticky="n", padx = 30, pady = 15)

text = tk.Label( text = "Введите пароль: ")
text.grid(column=0, row=6 , ipadx=10, ipady=5, sticky="w", pady = 10, padx = 10)
entry3 = ttk.Entry()
entry3.grid(column=0, row=6, padx = 20, sticky="e")

var = IntVar()

R1 = Radiobutton(root, text="Шифровка", variable = var, value=1)
R1.grid(column=0, row=8, sticky="w")

R1 = Radiobutton(root, text="Расшифровка", variable = var, value=2)
R1.grid(column=0, row=8, sticky="e")

btn = ttk.Button(text="Начать", command=select)
btn.grid(column=0, row=11,  padx=6, pady=6)
 
label = ttk.Label()
label.grid(column=0, row=12, sticky="s", padx = 10, pady = 15)

root.mainloop()