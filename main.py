import pyshorteners
from tkinter import *

win = Tk()
win.geometry("600x470")
win.configure(bg="pink")

#Button
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#Label for entering user url
Label(win,text = "Enter your url link",font = "impack 17 bold", bg = "black", fg = "white").pack(fill = 'x')

#Entry box
entry1 = Entry(win,font = "10", bd = 3, width = 40)
entry1.pack(pady = 30)

#Button
Button(win,text = "Click Me", font = "impack 12 bold",bg = "blue", fg = "white", width = "14", command = short).pack()

#Entry
entry2 = Entry(win,font = "impack 16 bold", bg = "pink", width = 24 , bd = 0)
entry2.pack(pady = 30)

mainloop()