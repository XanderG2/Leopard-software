import tkinter as tk
from tkinter import ttk
from HomePage import home
from Testlogin import login3
from EncripedAndDecrpt import encryped
from EncripedAndDecrpt import decrypt2

def get(root):
  global userentry, passentry
  userentrygot = userentry.get()
  passentrygot = passentry.get()
  identity = login3(userentrygot, passentrygot, root)
  if identity:
    root.destroy()
    home(userentrygot)
def get2(root):
  global userentry, passentry, passentryrepeet
  user = userentry.get()
  pas = passentry.get()
  pascheck = passentryrepeet.get()
  if len(user.split()) > 1:
    #invalid("SPACE")
    pass
  elif len(pas.split()) > 1:
    #invalid("SPACE")
    pass
  else:  
    decrypt2("details.txt")
    with open("details.txt", "r") as f:
      details = f.read().splitlines()
      if user + " " + pas not in details and pas == pascheck: 
        with open("details.txt", "a") as f:
          f.write(user+" "+pas+"\n")
        print(f"Signed up as {user}.")
        encryped("details.txt")
        home(user)
      else:
        print(f"Logged in as {user}.")
        encryped("details.txt")

def deleet(e):
  userentry.delete(0,"end")

def deleet2(e):
  global sineUp
  passentry.delete(0,"end")
  if sineUp == 1:
    passLablerepet.grid(row= 3, column=0)
    passentryrepeet.grid(row= 3, column=1)
def deleet3(e):
  passentryrepeet.delete(0,"end")


'''
def SineUp():
  global userentry, passentry, root2, root,passentryrepeet,passLablerepet, sineUp
  sineUp = 1
  root.destroy()
  root2= tk.Tk()
  root2.config(background="black")
  root2.title("Login to Leopard")
  
  titte = tk.Label(root2, text= "SineUp", fg = "white",bg = "black",font=('Helvetica', 34))

  userLable = tk.Label(root2, text = "Username: ", fg = "white", bg= "black")
  passLable = tk.Label(root2, text = "Password: ", fg = "white", bg= "black")
  passLablerepet = tk.Label(root2, text = "CofermPassword: ", fg = "white", bg= "black")

  userentry = tk.Entry(root2, width= 20, highlightcolor= "#FFD700", background= "black", bg= "black", fg = "white")
  passentry = tk.Entry(root2, width= 20, show="*", highlightcolor= "#FFD700", background= "black", bg= "black", fg = "white")
  passentryrepeet = tk.Entry(root2, width= 20, show="*", highlightcolor= "#FFD700", background= "black", bg= "black", fg = "white")

  
  userentry.insert(0,"Username")
  passentry.insert(0,"Password")
  passentryrepeet.insert(0,"Coferm Password")
  userentry.bind("<FocusIn>", deleet)
  passentry.bind("<FocusIn>", deleet2)
  passentryrepeet.bind("<FocusIn>", deleet3)
  
  titte.grid(row= 0, column= 0, columnspan= 3)
  userLable.grid(row = 1, column= 0) 
  passLable.grid(row = 2, column= 0)
  userentry.grid(row = 1, column= 1)
  passentry.grid(row = 2, column= 1)

  login = tk.Button(root2, text="Sine up", bg= "black",fg = "white", highlightbackground= "black", highlightcolor= "#FFD700",command= lambda: get2(root))
  login.grid(row=4, column=0 , columnspan= 3)
'''
def login():
  global userentry, passentry, root, sineUp
  sineUp = 0
  root= tk.Tk()
  root.config(background="black")
  root.title("Login to Leopard")
  
  titte = tk.Label(root, text= "Login", fg = "white",bg = "black",font=('Helvetica', 34))

  userLable = tk.Label(root, text = "Username: ", fg = "white", bg= "black")
  passLable = tk.Label(root, text = "Password: ", fg = "white", bg= "black")


  userentry = tk.Entry(root, width= 20, highlightcolor= "#FFD700", background= "black", bg= "black", fg = "white")
  passentry = tk.Entry(root, width= 20, show="*", highlightcolor= "#FFD700", background= "black", bg= "black", fg = "white")

  #sine_up= tk.Button(root, text = "sine up", fg = "white", bg= "black", command=SineUp)
  
  userentry.insert(0,"Username")
  passentry.insert(0,"Password")
  userentry.bind("<FocusIn>", deleet)
  passentry.bind("<FocusIn>", deleet2)
  
  titte.grid(row= 0, column= 0, columnspan= 3)
  userLable.grid(row = 1, column= 0) 
  passLable.grid(row = 2, column= 0)
  userentry.grid(row = 1, column= 1)
  passentry.grid(row = 2, column= 1)
 #sine_up.grid(row = 3, column=0)

  login = tk.Button(root, text="login", bg= "black",fg = "white", highlightbackground= "black", highlightcolor= "#FFD700",command= lambda: get(root))
  login.grid(row=3, column=1 , columnspan= 3)