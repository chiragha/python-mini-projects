from tkinter import *
import random


attempts = 10


answer = random.randint(1, 99)

def check_answer():
    global attempts
    global text

    attempts -= 1

    # Getting users input and converting it to integer data type.
    guess = int(entry_window.get())

    # Comparing guess to answer
    if answer == guess:
        text.set("You win!!")
        btn_check.pack_forget()
  
    elif attempts == 0:
        text.set("You are out of attempts goodbye!")
        btn_check.pack_forget()
  
    elif guess < answer:
        text.set("Incorrect! - You have " + str(attempts) + " remaining attempts - Go higher!")
      
        entry_window.delete(0, END)
  
    elif guess > answer:
        text.set("Incorrect! - You have " + str(attempts) + " remaining - Go lower!")
   
        entry_window.delete(0, END)
    return


root = Tk()

root.title("Number Guessing Game")

root.geometry("400x200")

label = Label(root, text="Guess the number between 1 and 99" , padx=10, pady=10, font=14)
label.pack()

entry_window = Entry(root, width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 10 attempts! Good luck" )
guess_attempts = Label(root, textvariable=text, padx=10, pady=10, font=15)
guess_attempts.pack()

root.mainloop()