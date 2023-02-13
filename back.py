import os
import view
from os import walk
from tkinter.filedialog import askdirectory

def open_directory():
    global directorypath
    newDirectorypath = askdirectory(title = "Select a destination directory ..." , mustexist = True )
    if newDirectorypath != "":
        directorypath = newDirectorypath
    else:
        return
    view.directoryName.set(directorypath.split("/")[-1])
    
def select_file_for_deletion(SubDirectoryInclued):
    global fileList
    global directoryList
    global fileListToDelete
    global fileType
    fileList = []
    directoryList = []

    for (directory, subdirectory, file) in walk(directorypath):
        fileList.append(file)
        directoryList.append(directory.replace("\\","/"))
        if not SubDirectoryInclued:
            break
    fileListToDelete = []
    for directory in range(len(fileList)):
        fileListToDelete.append([])
        if len(fileList[directory]) > 0:
            i = 0
            while i != len(fileList[directory]):
                if fileList[directory][i].split(".")[-1] == fileType:
                    fileListToDelete[directory].append(fileList[directory][i])
                i += 1

def delete_in_directory():
    for directory in range(len(directoryList)):
        for file in range(len(fileListToDelete[directory])):
            if os.path.exists(directoryList[directory]+"/"+fileListToDelete[directory][file]):
                print("Deletion of",directoryList[directory]+"/"+fileListToDelete[directory][file])
                os.remove(directoryList[directory]+"/"+fileListToDelete[directory][file])
            else:
                view.error(directoryList[directory]+"/"+fileListToDelete[directory][file]+" not exist.")
