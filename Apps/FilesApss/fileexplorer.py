import tkinter as tk
from tkinter import StringVar 

import os
import pathlib

def pathAtStart():
  currentPath.set("/home/runner/Leopard-software/Files/"+user)
  dic = os.listdir(currentPath.get())
  list.delete(0, tk.END)
  for file in dic:
    list.insert(0, file)
def pathChange(*event):
  print(currentPath.get())
  dic = os.listdir(currentPath.get())
  list.delete(0, tk.END)
  for file in dic:
    list.insert(0, file)
def chngepath(event= "None"):
  global list
  print(currentPath.get())
  picked =list.get(list.curselection()[0])
  path = os.path.join(currentPath.get(), picked)
  if os.path.isfile(path):
    print("open")
    os.startfile(path)
  else:
    currentPath.set(path)
def NewFolderAction(name, root2):
  root2.destroy()
  print (currentPath.get())
  os.mkdir(str(currentPath.get() + "/") + str(name))
  pathChange("")
def NewFolder():
  root2 = tk.Tk()
  root2.geometry("250x50")
  root2.title("New folder")
  Label = tk.Label(root2, text= "Enter a new name for new folder")
  Label.grid(row = 0, column= 0, columnspan= 2)
  name = tk.Entry(root2, width= 20, highlightcolor= "#FFD700")
  name.grid(row = 1, column= 0)
  submit = tk.Button(root2, text = "Submit", command= lambda: NewFolderAction(name.get(), root2 ))
  submit.grid(row = 1, column= 1)
def NewFileAction(name, root2):
  root2.destroy()
  print (currentPath.get())
  open(os.path.join(currentPath.get() + str(name)), "w").close()
  pathChange("")
def NewFile():
  root2 = tk.Tk()
  root2.geometry("250x50")
  root2.title("New File")
  Label = tk.Label(root2, text= "Enter a new name for new  file")
  Label.grid(row = 0, column= 0, columnspan= 3)
  name = tk.Entry(root2, width= 20, highlightcolor= "#FFD700")
  name.grid(row = 1, column= 0)

  submit = tk.Button(root2, text = "Submit", command= lambda: NewFolderAction(name.get(), root2 ))
  submit.grid(row = 1, column= 2)

def deleate():
  pass
def back():
  pass

def fileExplorer(users):
  global root, newthefile, submit, topbar, user, sidebar, list, currentPath, top
  top = ""
  user = users

  root = tk.Tk()
  root.grid_columnconfigure(1, weight=1)
  root.grid_rowconfigure(1, weight=1)
  root.title("File Explorer")
  #root.iconphoto(False, tk.PhotoImage(file='Apps/Appicons/File_explorer.png'))
  
  sidebar = tk.Frame(root)#, highlightbackground="black", highlightthickness=2, width= 40, height= 50)
  topbar = tk.Frame(root)#, highlightbackground="black", highlightthickness=2)
  dicnory = tk.Frame(root)
  mainItonm = tk.Frame(root)#, highlightbackground="black", highlightthickness=2)


  topbar.grid(row = 0, column= 0, columnspan=2)
  sidebar.grid(row = 2, column= 0, rowspan= 2)
  mainItonm.grid(row = 3, column= 1)
  dicnory.grid(row = 2, column= 1)


  tittle = tk.Label(topbar, text = "File explorer", font=('Helvetica', 16))

  tittle.grid(row = 0, column= 0)

  Back = tk.Button(sidebar, text = "Back", command= back, state = tk.DISABLED)
  New_Folder = tk.Button(sidebar, text = "New Folder", command = NewFolder)
  New_file = tk.Button(sidebar, text = "New File", command = NewFile)
  Delete = tk.Button(sidebar, text = "Deleet", command = deleate)
  
  Back.grid(row = 0, column=0)
  New_Folder.grid(row = 1, column= 0)
  New_file.grid(row = 2, column= 0)
  Delete.grid(row = 3, column= 0)


  currentPath = StringVar(
    root,
    name = 'currentPath',
    value = pathlib.Path.cwd()
  )

  currentPath.trace("w", pathChange)

  
  list = tk.Listbox(mainItonm)
  list.grid(row = 0, column= 0)
  list.bind('<Double-1>', chngepath)
  list.bind('<Return>', chngepath)
  pathAtStart()
  root.mainloop()

