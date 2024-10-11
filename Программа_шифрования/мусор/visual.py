from tkinter import *
from tkinter import ttk
import os
import попытка1
#from encrypto.py import walking_by_dirs

def show_message():

    label["text"] = 'E:\Программа шифрования\O'     # получаем введенный текст
    label2["text"] = 'E:\Программа шифрования\1.png'
    label3["text"] = "123"
    return [label, label2, label3]
 
window = Tk()
window.title("Crypt and DeCrypt")
window.geometry('500x500')
window.minsize(500,500)
window.maxsize(900,900)
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

entry2 = ttk.Entry()
entry2.pack(anchor=NW, padx=6, pady=12)

entry3 = ttk.Entry()
entry3.pack(anchor=NW, padx=6, pady=18)
  
btn = ttk.Button(text="Click", command=walking_by_dirs(cryptfile, keys))
btn.pack(anchor=NW, padx=6, pady=24)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=30)

label2 = ttk.Label()
label2.pack(anchor=NW, padx=6, pady=36)

label3 = ttk.Label()
label3.pack(anchor=NW, padx=6, pady=42)
  
window.mainloop()