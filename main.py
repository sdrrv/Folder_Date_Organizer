from tkinter import *
from tkinter import filedialog
import os
#--------------------------------------------------
direc=r""
#--------------------------------------------------
def dir_select():
    direc=filedialog.askdirectory()

def run():
    pass
#--------------------------------------------------
app=Tk()
app.title("Folder Date Organizer")
app.geometry("700x300")
#--------------------------------------------------
label_dir=Label(app,text="Select the folder:",font=("Calibri",14))
label_dir.grid(row=0,column=0)

#--------------------------------------------------
button_dir=Button(app,text="Select",command=dir_select)
button_dir.grid(row=0, column=1)

button_run=Button(app,text="Run",activebackground="Green", fg="Red", command=run, padx=5,pady=5)
button_run.grid(row=2, column=0)
#--------------------------------------------------


app.mainloop()