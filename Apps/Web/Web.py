import tkinterweb
import tkinter as tk
from tkinter import messagebox
def web():
  root = tk.Tk()
  test = tk.messagebox.askquestion("Warning","Are you shor you want to contine", icon = "warning")
  print(test)
  if test == "yes":
    root.title("Web")
    frame = tkinterweb.HtmlFrame(root)
    frame.load_website("https://www.google.co.uk/")
    frame.pack()
    root.mainloop()
  else:
    root.destroy()