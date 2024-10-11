from tkinter import *
master = Tk()
v = StringVar()

def Entered(p1):
    print ('Got: ', Entry1.get())
    print ('Got: ', v.get())

Entry1 = Entry(master, width = 25, textvariable = v) # No text now
Entry1.pack()
Entry1.bind('<Return>', Entered)
master.mainloop()