from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import back

app = Tk()

app.title("By Okiushi")

app.resizable(width=False, height=False)

fileNameListToDelete = StringVar()
fileNameListToDelete.set("No file found")

def ImportOfDeletionOrders():
    global NumberOfFilesToDelete
    back.fileType = textZone_FileType.get().replace(".","").replace(" ","").lower()
    if back.fileType == "":
        error("The extension name has not been provided")
        return
        
    try:
        back.directorypath = back.directorypath
    except:
        error("The path of the folder has not been provided")
        return
    
    back.select_file_for_deletion(SubDirectoryInclued.get())

    NumberOfFilesToDelete = 0
    fileNameListToDelete = ""
    for directory in range(len(back.directoryList)):
        for file in range(len(back.fileListToDelete[directory])):
            NumberOfFilesToDelete += 1
            if NumberOfFilesToDelete < 10:
                fileNameListToDelete += "\n"+back.fileListToDelete[directory][file]

    if NumberOfFilesToDelete >= 10:
        fileNameListToDelete += f"\n\nAnd other files..."

    if NumberOfFilesToDelete == 0:
        error(f"No .{back.fileType} file was found")
        return

    Confirme_Deletion = messagebox.askokcancel("Confirm the deletion",f"We will delete {NumberOfFilesToDelete} .{back.fileType} files in the folder {directoryName.get()}\n{fileNameListToDelete}")

    if Confirme_Deletion:
        back.delete_in_directory()
        deletion_Done()

def error(message):
    messagebox.showerror("Error",message)

def deletion_Done():
    global SubDirectoryInclued
    if SubDirectoryInclued.get():
        messagebox.showinfo("Deletion done",f"{NumberOfFilesToDelete} .{back.fileType} files have been deleted in the folder and subfolders of {directoryName.get()}")
    else:
        messagebox.showinfo("Deletion done",f"{NumberOfFilesToDelete} .{back.fileType} files have been deleted in the folder {directoryName.get()}")



window = Frame(app)
window.grid(row=0, column=0, padx=10,pady=10,sticky="nesw")

# ---

text_Delete_files_of_types = Label(window,text="Delete files of types")
text_Delete_files_of_types.grid(row=0, column=0, padx=10,pady=5,sticky=W)

text_FileType = Label(window,text=".")
text_FileType.grid(row=0, column=1,pady=5,sticky=W)

textZone_FileType = ttk.Entry(window)
textZone_FileType.grid(row=0, column=1, padx=10,pady=5,sticky=E)

# ---

text_In_the_folder = Label(window,text="In the folder")
text_In_the_folder.grid(row=1, column=0, padx=10,pady=5,sticky=W)

directoryName = StringVar()
directoryName.set("Select a folder")

button_In_the_folder = ttk.Button(window,textvariable=directoryName,command=back.open_directory)
button_In_the_folder.grid(row=1, column=1, padx=10,pady=5,sticky=EW,)

# ---

text_Include_subfolder = Label(window,text="Include subfolder")
text_Include_subfolder.grid(row=2, column=0, padx=10,pady=5,sticky=W)

SubDirectoryInclued = BooleanVar()
SubDirectoryInclued.set(False)
checkButton_Include_subfolder = ttk.Checkbutton(window,variable=SubDirectoryInclued,onvalue=True,offvalue=False,takefocus = 0)
checkButton_Include_subfolder.grid(row=2, column=1, padx=10,pady=5,sticky=W)

button_preDelete = ttk.Button(window,text="Delete",command=ImportOfDeletionOrders)
button_preDelete.grid(row=3, columnspan=2, padx=10,pady=10,sticky=EW)