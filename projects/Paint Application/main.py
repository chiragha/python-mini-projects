from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
import PIL.ImageGrab as ImageGrab   # for save image
from tkinter import filedialog




root=Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#19172e")
root.resizable(False,False)

current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
     
     global current_x, current_y
     current_x = work.x
     current_y = work.y




def addLine(work):
   global current_x, current_y

   canvas.create_line((current_x,current_y,work.x,work.y),width=current_value(),fill=color,capstyle=ROUND, smooth=TRUE)
   current_x,current_y = work.x,work.y



def show_color(new_color):
 global color
 
 color=new_color



def new_canvas():
    canvas.delete('all')
    show_pallete()



def saveImage():
    # Choose a location to save the file
    fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")

    # Define the initial coordinates of the image to be saved
    x = root.winfo_rootx()+100
    y = root.winfo_rooty()+35

    # Define the final coordinates of the image to be saved
    img = ImageGrab.grab(bbox=(x,y,x+900,y+470))
    
    # Show the image saved
    img.show()

    # Save it
    img.save(fileLocation)  
   

icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)


sidebar = PhotoImage(file="sidebar.png")
lbl_side = Label(root,image=sidebar,bg="#19172e" )
lbl_side.place(x=10, y=15)

eraser = PhotoImage(file="eraser.png")  #reaser
btn_erase = Button(root,image=eraser,bg="#ffffff" , command=new_canvas)
btn_erase.place(x=30, y=380)


save_image = PhotoImage(file="save.png")   #image save
save_button = Button(root, image=save_image, bg="#f2f3f5", command=saveImage)
save_button.place(x=25, y=450)

colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)


#function for pallete
def show_pallete():
  
  id = colors.create_rectangle((10,10,30,30), fill='black')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

  id = colors.create_rectangle((10,40,30,60), fill='gray')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

  id = colors.create_rectangle((10,70,30,90), fill='brown4')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

  id = colors.create_rectangle((10,100,30,120), fill='red')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

  id = colors.create_rectangle((10,130,30,150), fill='orange')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

  id = colors.create_rectangle((10,160,30,180), fill='yellow')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

  id = colors.create_rectangle((10,190,30,210), fill='green')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

  id = colors.create_rectangle((10,220,30,240), fill='blue')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

  id = colors.create_rectangle((10,250,30,270), fill='purple')
  colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))
  
show_pallete()  
  




canvas = Canvas(root, width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=15)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)


curr_value = tk.DoubleVar()

def current_value():
   return '{: .2f}'.format(curr_value.get())

def change_slider(event):
   value_label.configure(text=current_value())

slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=change_slider,
    variable=curr_value
)
slider.place(x=100,y=530)


value_label = ttk.Label(root, text=current_value(),background ='green')
value_label.place(x=200,y=535)


txtlabel = ttk.Label(root, text="Thickness")
txtlabel.place(x=240,y=535)






root.mainloop()