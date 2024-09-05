import onetimepad
from tkinter import *
import tkinter.messagebox 

win = Tk()
win.title("Encryption")
win.geometry("300x200")
win.configure(bg="#19172e")



def encryptmessage():
    message = e1.get()
    ciphertext = onetimepad.encrypt(msg=message, key='random')
    
    tkinter.messagebox.showinfo("cipher",ciphertext) 
   


label = Label(win, text='Enter message') 
label.grid(row=10, column=1, padx=20, pady=20)
label.configure(bg="#19172e")
label.configure(fg="white")


e1 = Entry(win)
e1.grid(row=10, column=2)


encryptionButton = Button(win, text='Encryption', bg='red', fg='black', command=encryptmessage)
encryptionButton.grid(row=13, column=2)

win.mainloop()