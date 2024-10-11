from tkinter import *
from tkinter import ttk
import encryption
import decryption



def encrypt():
    
    cryptfile =  entry.get()
    keyfile = entry2.get()    # получаем введенный текст
    password = entry3.get()
    text = encryption.get(cryptfile, keyfile, password)
    label["text"] = text

def decrypt():
    
    cryptfile =  entry.get()
    keyfile = entry2.get()    # получаем введенный текст
    password = entry3.get()
    text = decryption.get(cryptfile, keyfile, password)
    label["text"] = text

def select():
    selection = var.get()
    if selection  == 1:
        encrypt()
    elif selection  == 2:
        decrypt()
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
entry2 = ttk.Entry()
entry2.pack(anchor=NW, padx=6, pady=6)
entry3 = ttk.Entry()
entry3.pack(anchor=NW, padx=6, pady=6)

var = IntVar()

R1 = Radiobutton(root, text="Шифровка", variable = var, value=1)
R1.pack(anchor = NW)

R1 = Radiobutton(root, text="Расшифровка", variable = var, value=2)
R1.pack(anchor = NW)

btn = ttk.Button(text="Click", command=select)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
  
root.mainloop()