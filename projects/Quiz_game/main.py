import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_ques import quiz_ques



def show_ques():
    question = quiz_ques[current_question]
    ques_label.config(text=question["question"])

    choices = question["choices"]

    for i in range(4):
        choice_btn[i].config(text=choices[i], state="normal") # reset



    #clear
    feed_label.config(text="")
    next_btn.config(state="disabled")    



def check_answer(choice):
    question = quiz_ques[current_question]
    selected_choice = choice_btn[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_ques)))
        feed_label.config(text="Correct!", foreground="green")
    else:
        feed_label.config(text="Incorrect!", foreground="red")


    for button in choice_btn:
        button.config(state="disabled")
        next_btn.config(state="normal")  




def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_ques):
        show_ques()
    else:
        messagebox.showinfo("Quiz Completed","Quiz Completed! Final score: {}/{}".format(score, len(quiz_ques)))
        root.destroy()         


# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
# root.configure(bg="#19172e")
style = Style(theme="flatly")


style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

ques_label = ttk.Label(root, anchor="center", wraplength=500, padding=10)
ques_label.pack(pady=10)

choice_btn = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btn.append(button)

feed_label = ttk.Label(root, anchor="center",padding=10)
feed_label.pack(pady=10)  

score = 0

score_label = ttk.Label(root, text="Score: 0/{}".format(len(quiz_ques)), anchor="center",padding=10)
score_label.pack(pady=10)

next_btn = ttk.Button(root,text="Next",command=next_question,state="disabled")
next_btn.pack(pady=10)

current_question = 0

show_ques()



root.mainloop()