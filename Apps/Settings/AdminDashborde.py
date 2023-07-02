import tkinter as tk
from EncripedAndDecrpt import encryped
from EncripedAndDecrpt import decrypt2
def adduser2():
  global User
  User.insert(tk.END, "Username Password\n")
def save1():
  global root, User
  open("details.txt", "w").close()
  with open("details.txt", "w") as d:
    d.write(User.get("1.0",'end-1c'))
  encryped("details.txt")
  root.destroy()
  start()
def editU():
  global root, User
  decrypt2("details.txt")
  with open ("details.txt", "r") as d:
    Usertext = d.read()
  encryped("details.txt")
  edit = tk.Frame(root)
  edit.grid(row = 2, column=0)
  User = tk.Text(edit, width= 20, height= 10)
  save = tk.Button(edit, text = "Save", command = save1)
  adduser = tk.Button(edit, text = "Adduser", command = adduser2)
  User.grid(row = 3, column= 0, columnspan= 2)
  save.grid(row = 4, column=0)
  adduser.grid(row=4, column= 1)
  
  User.delete("1.0", tk.END)
  User.insert(tk.END, Usertext)
def addAdmin2():
  global Admin
  Admin.insert(tk.END, "Username\n")

def save2():
  global root, Admin
  open("Admins.txt", "w").close()
  with open("Admins.txt", "w") as d:
    d.write(Admin.get("1.0",'end-1c'))
  encryped("Admins.txt")
  root.destroy()
  start()

def editA():
  global root, Admin
  decrypt2("Admins.txt")
  with open ("Admins.txt", "r") as d:
    Admintext = d.read()
  encryped("Admins.txt")
  edit1 = tk.Frame(root)
  edit1.grid(row = 2, column=0)
  Admin = tk.Text(edit1, width= 20, height= 10)
  save = tk.Button(edit1, text = "Save", command = save2)
  addAdmin = tk.Button(edit1, text = "Add Admin", command = addAdmin2)
  Admin.grid(row = 3, column= 0, columnspan= 2)
  save.grid(row = 4, column=0)
  addAdmin.grid(row=4, column= 1)
  
  Admin.delete("1.0", tk.END)
  Admin.insert(tk.END, Admintext)






def start():
  global root
  decrypt2("details.txt")
  with open ("details.txt","r") as D:
    username = D.read().splitlines()
  usernamedetels = ""
  for x in range(0,len(username)):
    usernamedetels = usernamedetels + str(username[x]) +"\n"
  encryped("details.txt")
  
  decrypt2("Admins.txt")
  with open ("Admins.txt", "r") as d:
    Admintextlist = d.read()
  encryped("Admins.txt")
  

  
  root = tk.Tk()
  root.title("Admin Dashbord")

  
  title = tk.Label(root, text = "Admin Dashbord", font=('Helvetica', 16))



  info = tk.Frame(root,highlightbackground="#FFD700", highlightthickness=2)

  UserLabal = tk.Label(info, text = "Users")
  Usertext = tk.Label(info, text = usernamedetels)
  userbuttion = tk.Button(info, text = "Edit", command = editU)

  spacer1 = tk.Label(info, text ="                ")
  spacer2 = tk.Label(info, text ="                ")
  spacer3 = tk.Label(info, text ="                ")
  
  spacer1.grid(row = 0, column=1)
  spacer2.grid(row = 2, column=1)
  spacer3.grid(row = 3, column=1)
  
  AdminLabel = tk.Label(info, text = "Admins")
  Admintext = tk.Label(info, text = Admintextlist)
  Adminbutton = tk.Button(info, text = "Edit", command = editA)

  title.grid(row = 0, column= 0, columnspan= 2)
  
  info.grid(row = 1, column= 0)
  UserLabal.grid(row = 0, column= 0)
  Usertext.grid(row = 1, column = 0)
  userbuttion.grid(row = 2, column=0)


  AdminLabel.grid(row = 0, column= 2)
  Admintext.grid(row = 1, column = 2)
  Adminbutton.grid(row = 2, column=2)
