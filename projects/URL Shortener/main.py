import tkinter
import pyshorteners


def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) //2
    y = (screen_height - window.winfo_reqheight()) //2
    window.geometry(f"+{x}+{y}")

window = tkinter.Tk()
window.title("URL Shortener")
window.geometry("300x200")
frame = tkinter.Frame(window)
frame.configure(bg='lightblue')

frame.pack()
center_window(window)
window.configure(bg='lightblue')

info_frame = tkinter.LabelFrame(frame, text="URL Shorten")
info_frame.grid(row=0,column=0,padx=30,pady=30)
info_frame.configure(bg='lightblue')

def shorturl():
    shortu = pyshorteners.Shortener()
    short_url = shortu.tinyurl.short(long_entry.get())
    short_entry.insert(0,short_url)



# user rent
longurl_label = tkinter.Label(info_frame, text="Enter Long URL")
longurl_label.grid(row=0, column=0,padx=10,pady=10)
longurl_label.configure(bg='lightblue')

# user food
Shorturl_label = tkinter.Label(info_frame, text="Output Short URL")
Shorturl_label.grid(row=1, column=0,padx=10,pady=10)
Shorturl_label.configure(bg='lightblue')


long_entry = tkinter.Entry(info_frame)
short_entry = tkinter.Entry(info_frame)

long_entry.grid(row=0,column=1,padx=10,pady=10)
short_entry.grid(row=1,column=1,padx=10,pady=10)


submit_button = tkinter.Button(info_frame, text ="Submit" , command=shorturl)
submit_button.grid(row=5, column=1,padx=10,pady=10)


window.mainloop()