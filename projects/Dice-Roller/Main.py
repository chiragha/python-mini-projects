from tkinter import *
import random

root = Tk()
root.geometry("700x450")
root.title("Roll-Dice")
root.configure(bg="#19172e")


label = Label(root,text="",font=("times",260))
label.configure(bg="#19172e")

def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button = Button(root, text="lets roll", width=10, height=3,font=15,bg="white",bd=2,fg="black",command=roll)
button.pack(padx=10,pady=10)

root.mainloop()
