from tkinter import StringVar
import tkinter as tk

from EncripedAndDecrpt import encryped
from EncripedAndDecrpt import decrypt2
from HomePage import home
from os.path import exists as exists
from os import makedirs as makedirs
#from Login import login

def SineUp():
  global root,user,pas
  root.destroy()
  decrypt2("details.txt")
  with open("details.txt", "r") as f:
      details = f.read().splitlines()
      if user + " " + pas not in details: 
        with open("details.txt", "a") as f:
          f.write(user+" "+pas+"\n")
        print(f"Signed up as {user}.")
        encryped("details.txt")

        newpath = "/home/runner/Leopard-software/Files/"+str(user)
        if not exists(newpath):
          makedirs(newpath)
        home(user)
        
      else:
        print("error")
        encryped("details.txt")
def check_pasword_box(*args):
  global e, pas
  if e.get() == pas:
    SineUp()
def pasword_for_sine_up():
  global root
  global e
  lable_for_pasword = tk.Label(root, text = "Type pasword again to create account", fg = "white", bg = "black")
  
  e = StringVar()
  e.trace("w", check_pasword_box)
  pasword = tk.Entry(root, width= 20, highlightcolor= "#FFD700", background= "black", bg= "black", fg = "white", show = "*", textvariable=e)
  lable_for_pasword.grid(row = 2, column = 0, columnspan= 2)
  pasword.grid(row = 3, column= 0, columnspan=2)
  root.mainloop()

def login2():
  global root
  root.destroy()
  #login()
def Chechsineup(username, password):
  global root,user,pas
  user = username
  pas = password
  root = tk.Tk()
  root.config(background="black")
  text = tk.Label(root, text="The account you typed in does not exist \n Would you like to sign \n or \n go back to the login page", fg = "white", bg = "black")
  Sineup = tk.Button(root, text = "SineUp", fg = "white", bg = "black", command= lambda: pasword_for_sine_up())#SineUp(user, pas))
  login = tk.Button(root, text = "Login", fg = "white", bg = "black", command= login2, state=tk.DISABLED)
  
  text.grid(row = 0, column= 0, columnspan=2)
  Sineup.grid(row = 1, column= 0)
  login.grid(row = 1, column= 1)
def invalid(reason):
  if reason=="SPACE":
    print("Username or password must not contain a space, sorry. Please try again.")

def login3(user, pas, root):
  if len(user.split()) > 1:
    invalid("SPACE")
  elif len(pas.split()) > 1:
    invalid("SPACE")
  else:  
    decrypt2("details.txt")
    with open("details.txt", "r") as f:
      details = f.read().splitlines()
      if user + " " + pas not in details: 
        #with open("details.txt", "a") as f:
        encryped("details.txt")
        root.destroy()
        Chechsineup(user, pas)
        return(False)
        #  f.write(user+" "+pas+"\n")
        #print(f"Signed up as {user}.")
      else:
        print(f"Logged in as {user}.")
        encryped("details.txt")
      return(True)
  return(False)