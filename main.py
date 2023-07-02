import tkinter as tk
from HomePage import home
from Login import login
from tkinter import ttk
from EncripedAndDecrpt import encryped
from EncripedAndDecrpt import decrypt2
import pytz
#decrypt2("details.txt")
#decrypt2("Admins.txt")
def startloginprocess():
  #encryped("details.txt")
  encryped("Admins.txt")
  root.destroy()
  login()


root = tk.Tk()
root.title("Leopard Software")
title = tk.Label(root, font=('Helvetica', 34), text="Welcome to Leopard Software")
title.grid(row=0, column=0)
start = tk.Button(root, text="Start", command=startloginprocess)
start.grid(row=1, column=0)
photo_image = tk.PhotoImage(file="leopard logo.png")
label = ttk.Label(root, image=photo_image)
label.grid(row=2, column=0)