import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.geometry("700x300")
window.title("Rent Calculator")


frame = tkinter.Frame(window)
frame.pack()



user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)


def calculate():
 rent = rent_entry.get()
 food = food_entry.get()
 elect= electricity_spend_entry.get()
 unit = charge_unit_entry.get()
 person = person_spinbox.get()


 tot_total = (int(rent)+int(food)+(int(unit)*int(elect)))
 
 messagebox.showinfo(str("Total-Rent"),str(tot_total))

# user rent
user_rent_label = tkinter.Label(user_info_frame, text="User Rent")
user_rent_label.grid(row=0, column=0)

# user food
user_food_label = tkinter.Label(user_info_frame, text="Food Price")
user_food_label.grid(row=1, column=0)

# elecricity spend 
user_food_label = tkinter.Label(user_info_frame, text="Electricity Spend")
user_food_label.grid(row=2, column=0)

# charge_per_unit 
charge_unit_label = tkinter.Label(user_info_frame, text="Charge per Unit")
charge_unit_label.grid(row=2, column=1)

# person living in room 
person_label = tkinter.Label(user_info_frame, text="Number Of Person Living In The Room/Flat")
person_label.grid(row=2, column=2)

rent_entry = tkinter.Entry(user_info_frame)
food_entry = tkinter.Entry(user_info_frame)
electricity_spend_entry = tkinter.Entry(user_info_frame)
charge_unit_entry = tkinter.Entry(user_info_frame)
person_spinbox= tkinter.Spinbox(user_info_frame, from_=1 , to=5)


rent_entry.grid(row=0,column=1)
food_entry.grid(row=1,column=1)
electricity_spend_entry.grid(row=3,column=0)
charge_unit_entry.grid(row=3,column=1)
person_spinbox.grid(row=3,column=2)


submit_button = tkinter.Button(user_info_frame, text ="Submit", command=calculate)
submit_button.grid(row=5, column=2)


for widget in user_info_frame.winfo_children():
 widget.grid_configure(padx=10, pady=5)
window.mainloop()

