from tkinter import *
from tkinter import filedialog
import os,time
#--------------------------------------------------
direc=r""
files=[]
#--------------------------------------------------
def debug(text,color):
    label_debug.config(text=text,fg=color)

def thor(arg):
    result=[]
    for i in arg:
        if i not in result:
            result.append(i)
    return result

def dir_select():
    global direc
    global files
    try:
        direc=filedialog.askdirectory()
        debug("Dir Selected!","Green")
        print(direc+"/"+"me.txt")
        files=os.listdir(direc)
        if not files:
            debug("Error_Dir_No_Files","Red")
    except Exception as e:
        debug(f"Error_Dir: {e}","Red")
def run():
    count=0
    count_files=0
    try:
        for file in files:
            file_date=str(time.gmtime(os.path.getatime(direc+"/"+file))[0])
            if not os.path.exists(direc+"/"+file_date):
                os.makedirs(direc+"/"+file_date)
                count+=1
            os.replace( (direc+"/"+file) , (direc+"/"+file_date+"/"+file)  )
            count_files+=1
    
        debug((f"Finished With: \n {count} Folders Created \n {count_files} Files Moved"), "Green")

    except Exception as e:
        debug(f"Error_Dir: {e}", "Red")


#--------------------------------------------------
app=Tk()
app.title("Folder Date Organizer")
app.geometry("270x220")
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