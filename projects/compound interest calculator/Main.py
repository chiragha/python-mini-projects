import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.geometry("400x250")
window.title("compound interest calculator")
window.configure(background='#19172e')


frame = tkinter.Frame(window)
frame.pack()


user_info_frame = tkinter.LabelFrame(frame, text="Calculate", background='#19172e', fg='white', font='5')
user_info_frame.grid(row=0,column=0)


def calculate():
 principle = int(prin_entry.get())
 rate = float(rate_entry.get())
 time = int(time_label.get())

 CI = principle * (pow((1+rate/100), time))

 result_label.insert(10,CI)


# Principle
prin_label = tkinter.Label(user_info_frame, text="Principle", background='#19172e',fg='white', font='5')
prin_label.grid(row=0, column=0)

# Rate
rate_label = tkinter.Label(user_info_frame, text="Rate", background='#19172e',fg='white', font='5')
rate_label.grid(row=1, column=0)

# Time
time_label = tkinter.Label(user_info_frame, text="Time", background='#19172e',fg='white', font='5')
time_label.grid(row=2, column=0)



prin_entry = tkinter.Entry(user_info_frame)
prin_entry.grid(row=0,column=1)

rate_entry = tkinter.Entry(user_info_frame)
rate_entry.grid(row=1,column=1)

time_label = tkinter.Entry(user_info_frame)
time_label.grid(row=2,column=1)



# RESULT
result_label = tkinter.Label(user_info_frame, text="RESULT", background='#19172e',fg='white', font='4')
result_label.grid(row=3, column=0)

result_label = tkinter.Entry(user_info_frame)
result_label.grid(row=3,column=1)


submit_button = tkinter.Button(user_info_frame, text ="Submit", command=calculate, font='5')
submit_button.grid(row=5, column=1)


for widget in user_info_frame.winfo_children():
 widget.grid_configure(padx=10, pady=5)
window.mainloop()

