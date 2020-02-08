from tkinter import *
from tkinter import filedialog
import os
#--------------------------------------------------
direc=r""
#--------------------------------------------------
def debug(text,color):
    label_debug.config(text=text,fg=color)

def dir_select():
    try:
        direc=filedialog.askdirectory()
        debug("Dir Selected!","Green")
    except Exception as e:
        debug("Error_Dir"& e)
def run():
    pass
#--------------------------------------------------
app=Tk()
app.title("Folder Date Organizer")
app.geometry("250x200")
#--------------------------------------------------
label_dir=Label(app,text="Select the folder:",font=("Calibri",14))
label_dir.grid(row=0,column=0, pady=20, padx=10)

label_debug=Label(app,font=("BookMan Old Style",14), padx=10, pady=20)
label_debug.grid(row=1,column=0)

#--------------------------------------------------
button_dir=Button(app,text="Select",command=dir_select)
button_dir.grid(row=0, column=1, padx=10)

button_run=Button(app,text="Run",activebackground="Green", fg="Red", command=run, padx=5,pady=5)
button_run.grid(row=2, column=0, ipadx=20)
#--------------------------------------------------


app.mainloop()