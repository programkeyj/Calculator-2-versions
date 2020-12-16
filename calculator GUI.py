from tkinter import*

def bl_click():
    vidp = eval(entry1.get())
    entry2.delete(0, END)
    entry2.insert(0, vidp)

import tkinter

root = Tk()
root.title('app')
root.geometry('250x250')

label = Label(root, text = 'введіть', font = 'arial 18')
label.place(x = 20, y = 10)

label.pack()

s = 'try'
entry1 = Entry(root, text = s, width = 16, font = 'arial 18')
entry1.place(x = 20, y = 50)

entry2 = Entry(root, width = 16, font = 'arial 18')
entry2.place(x = 20, y = 140)

bl = Button(root, text = 'розв\'зати', command = bl_click)
bl.place(x = 40, y = 90)

root.mainloop

print('нажмите ентер')
input('')

