import sqlite3
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Crypt and DeCrypt')
window.geometry('500x500')
window.minsize(500,500)
window.maxsize(900,900)

frame_add_crypt = tk.Frame(window, width=150, height=150)
frame_add_decrypt = tk.Frame(window, width= 150, height= 150)
frame_add_db = tk.Frame(window, width=300, height=150)

frame_add_crypt.place(relx=0, y=0, relwidth=0.5, relheight=0.5)
frame_add_decrypt.place(relx=0.5, y=0, relwidth=0.5, relheight=0.5)
frame_add_db.place(x=0, rely=0.5, relwidth=1, relheight=0.5)

window.mainloop()

with sqlite3.connect('db/database.db') as db:
	cursor = db.cursor()
	query = """ CREATE TABLE IF NOT EXISTS expenses (id INTEGER, passwords TEXT) """

	cursor.execute(query)
	db.commit()
db.close()
ttk.Entry().pack(anchor=NW, padx=8, pady= 8)
l_fail_to_crypt = tk.label(frame_add_crypt, text = "1")
l_fail_to_passwords = tk.label(frame_add_crypt, text = "2")
l_fail_to_key = tk.label(frame_add_crypt, text = "3")
l_fail_to_decrypt = tk.label(frame_add_decrypt, text = "1")
l_fail_to_passwords2 = tk.label(frame_add_decrypt, text = "2")
l_fail_to_key2 = tk.label(frame_add_decrypt, text = "3")
l_fail_to_key2 = tk.label(frame_add_db, text = "3")

l_fail_to_crypt.grid(row="0",column="0")
l_fail_to_passwords.grid(row="0",column="1")
l_fail_to_key.grid(row="0",column="0")
l_fail_to_decrypt.grid(row="0",column="0")
l_fail_to_passwords2.grid(row="0",column="0")
l_fail_to_key2.grid(row="0",column="0")