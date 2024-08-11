import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")  #title
root.geometry("400x600+400+100")
root.resizable(False,False)


list_task = []


# add task function 

def addTask():
   task = task_entry.get()
   task_entry.delete(0,END)

   if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        list_task.append(task)
        listbox.insert(END,task)

# delete function

def deleteTask():
    global list_task
    task = str(listbox.get(ANCHOR))   

    if task in list_task:
        list_task.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in list_task:
               taskfile.write(f"\n{task}")
        
            listbox.delete(ANCHOR)


# show task 

def openTaskFile():
     try:
         global task_list 
         with open("tasklist.txt", "r") as taskfile:
              tasks = taskfile.readlines()

         for task in tasks:
              if task !='\n':
                 list_task.append(task)
                 listbox.insert(END,task)   
     except:
          file = open('tasklist.txt', 'w')
          file.close()                 

img_icon = PhotoImage(file="images/list.png") #icon
root.iconphoto(False,img_icon)

heading = Label(root,text="To-Do-List", font="Arial 25 bold", fg="#19172e")
heading.place(x=110,y=30)

frame = Frame(root,width=400,height=35,bg="white")
frame.place(x=0,y=120)

task = StringVar()
task_entry= Entry(frame,width=15,font="Arial 15", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

btn = Button(frame,text="Add", font="Arial 15 bold", fg="white", bg="#19172e", command=addTask)
btn.place(x=345,y=0)


#show-task

frame1 = Frame(root,width=700,height=300,bg="#19172e")
frame1.pack(pady=(220,0))

listbox = Listbox(frame1,font="Arial 12",width=40,height=15, bg="#19172e",fg='white',cursor='hand2',selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()


#delete
del_img = PhotoImage(file="images/bin.png")
Button(root, image=del_img,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()