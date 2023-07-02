import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from EncripedAndDecrpt import encryped
from EncripedAndDecrpt import decrypt2
from datetime import datetime
import pytz


def create_clock():
  global root, clock_label
  clock_label = tk.Label(root, text="", padx=10)
  clock_label.grid(row=20, column=4)

def update_clock():
  global root, clock_label
  bst = pytz.timezone("Europe/London")
  current_time = datetime.now(bst).strftime("%d/%m/%y %H:%M:%S")
  clock_label.config(text=current_time)
  root.after(1000, update_clock) #may be off by about 6.5 seconds


def app1():
  import Apps.text_editor_python.main

def app2(user):
  from Apps.BomeGame.bombdodger import start_bombdodger
  start_bombdodger(user)
  
def app3(user):
  decrypt2("Admins.txt")
  with open("Admins.txt","r") as A:
    admins = A.read().splitlines()
  if user in admins:
    from Apps.Settings.AdminDashborde import start
    encryped("Admins.txt")
    start()
  else:
    encryped("Admins.txt")
    tk.messagebox.showerror("Pomishion","You do not have ecress to this app")
    
def app4(user):
  tk.messagebox.showwarning("Warning", "This is a unstable app")
  from Apps.Web.Web import web; web()
def app5(user):
  from Apps.FilesApss.fileexplorer import fileExplorer
  fileExplorer(user)

def on_closing():
  pass
def home(user):
  global root
  root = tk.Tk()
  root.title("Leopard software homepage")
  root.protocol("WM_DELETE_WINDOW", on_closing)
  #root.overrideredirect(True)
  with open("Admins.txt", "r") as f:
    admins = f.read().splitlines()
  text="Welcome to the leopard software homepage. \nClick on an app to enter. \nYou are logged in as"+" "+str(user)+"."
  if user in admins:
    print(f"{user} is admin")
    text = text="Welcome to the leopard software homepage. \nClick on an app to enter. \nYou are logged in as"+" "+str(user)+"." + "\nYou are an admin"
  welcome = tk.Label(root, text=text, font=('Helvetica', 16))
  welcome.grid(row=0, column=0, columnspan=5, rowspan=3)
  #logo = tk.PhotoImage(file="leopard logo.png")
  #label = ttk.Label(root, image=logo)
  #label.grid(row=3, column=0)
  app1img = tk.PhotoImage(file="Apps/Appicons/notpad.gif")
  app1imglbl = ttk.Button(root, image=app1img, command=app1)
  app1lbl = tk.Label(root, text="Notepad--")
  app1imglbl.grid(row=4, column=0)
  app1lbl.grid(row=5, column=0)

  app2img = tk.PhotoImage(file="Apps/Appicons/bombdodger.gif")
  app2imglbl = ttk.Button(root, image=app2img, command= lambda: app2(user))
  app2lbl = tk.Label(root, text="Bomb Game")
  app2imglbl.grid(row=6, column=0)
  app2lbl.grid(row=7, column=0)


  app5img = tk.PhotoImage(file="Apps/Appicons/File_explorer.gif")
  app5imglbl = ttk.Button(root, image=app5img, command= lambda: app5(user))
  app5lbl = tk.Label(root, text="File Explorer")
  app5imglbl.grid(row=4, column=3)
  app5lbl.grid(row=5, column=3)
  
  app3img = tk.PhotoImage(file="Apps/Appicons/Admin_dashbord.gif")
  app3imglbl = ttk.Button(root, image=app3img, command= lambda: app3(user))
  app3lbl = tk.Label(root, text="Admin dashbord")
  app3imglbl.grid(row=4, column=4)
  app3lbl.grid(row=5, column=4)

  app4img = tk.PhotoImage(file="Apps/Appicons/web.gif")
  app4imglbl = ttk.Button(root, image=app4img, command= lambda: app4(user))
  app4lbl = tk.Label(root, text="Web")
  app4imglbl.grid(row=4, column=1)
  app4lbl.grid(row=5, column=1)
  
  copyright = tk.Label(root, text="© Xander & Daniel 2023")
  copyright.grid(row=20, column=0)
  create_clock()
  update_clock()
  root.mainloop()