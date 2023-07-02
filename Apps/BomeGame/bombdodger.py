import random
import tkinter
from linecache import getline
from tkinter import *
from tkinter import messagebox
from random import choice
from cryptography.fernet import Fernet
def encryped(name):
  with open("key.key","r+") as keytext:
    key = keytext.read()
  f = Fernet(key)
  with open (name,"rb") as pwd:
    pd= pwd.read()
  pc = f.encrypt(pd)
  with open (name,"wb") as wc:
    wc.write(pc)

def decrypt2(name):
  with open("key.key","r+") as keytext:
    key = keytext.read()
  f = Fernet(key)
  with open(name, "rb") as Pc:
    encrepted = Pc.read()
  decypt = f.decrypt(encrepted)
  with open (name, "wb") as Pd:
    Pd.write(decypt)

def start_bombdodger(user):
  global gameOver
  gameOver = False
  global score
  score = 0
  global highscore
  highscore = score
  global squaresToClear
  squaresToClear = 0
  play_bombdodger(user)


def play_bombdodger(user):
  create_bombfield(bombfield)
  global score
  decrypt2("Admins.txt")
  with open("Admins.txt","r") as A:
    admins = A.read().splitlines()
  if user in admins:
    from Apps.Settings.AdminDashborde import start
    encryped("Admins.txt")
  if user in admins:
    print("Answers:")
    printfield(bombfield)
  global username
  username = user
  global window
  window = tkinter.Tk()
  #window.iconbitmap('Apps/Appicons/bombdodger(copy).ico')
  window.title("Bombdodger")
  layout_window(window)
  window.mainloop()


bombfield = []
def create_bombfield(bombfield):
  global squaresToClear
  for row in range(0, 10):
    rowList = []
    for calumn in range(0, 10):
      if random.randint(1, 100) < 20:
        rowList.append(1)
      else:
        rowList.append(0)
        squaresToClear = squaresToClear + 1
    bombfield.append(rowList)


def printfield(bombfield):
  for rowList in bombfield:
    print(rowList)
def layout_window(window):
  for rowNumber, rowList in enumerate(bombfield):
    for columnNumber, columnEntry in enumerate(rowList):
      if random.randint(1, 100) < 25:
        square = tkinter.Label(window, text="    ", bg="darkgreen")
      elif random.randint(1, 100) > 75:
        square = tkinter.Label(window, text="    ", bg="seagreen")
      else:
        square = tkinter.Label(window, text="    ", bg="green")
      square.grid(row=rowNumber, column=columnNumber)
      square.bind("<Button-1>", on_click)


def on_click(event):
  global score
  global highscore
  global gameOver
  global squaresToClear
  global bombfield
  global window
  square = event.widget
  row = int(square.grid_info()["row"])
  column = (square.grid_info()["column"])
  currentText = square.cget("text")
  if gameOver == False:
    if bombfield[row][column] == 1:
      gameOver = False
      square.config(bg="red")
      if score > highscore:
        highscore = score
      else:
        highscore = highscore
      global username
      info = "Game over, your score was " + str(
        score) + " and your highscore is " + str(
          highscore) + ". Do you want to play again?"
      playAgain = messagebox.askyesno(message=info)
      if playAgain == True:
        window.destroy()
        score = 0
        gameOver == False
        bombfield = []
        play_bombdodger(username)

      #score = 0
      #global username
      #if username == "daniel@bombgame.com":
      #global Dscore
      #Dscore = score
      #elif username == "xander@bombgame.com":
      #global Xscore
      #Xscore = score

      #print(
      #"------------------------------------------Restart-----------------------------"
      #)
      #gameOver == False
      #bombfield = []
      #global window
      #window.destroy
      #play_bombdodger()

    elif currentText == "    ":
      square.config(bg="brown")
      totalbombs = 0
      if row < 9:
        if bombfield[row + 1][column] == 1:
          totalbombs = totalbombs + 1
      if row > 0:
        if bombfield[row - 1][column] == 1:
          totalbombs = totalbombs + 1
      if column > 0:
        if bombfield[row][column - 1] == 1:
          totalbombs = totalbombs + 1
      if column < 9:
        if bombfield[row][column + 1] == 1:
          totalbombs = totalbombs + 1
      if row > 0 and column > 0:
        if bombfield[row - 1][column - 1] == 1:
          totalbombs = totalbombs + 1
      if row < 9 and column > 0:
        if bombfield[row + 1][column - 1] == 1:
          totalbombs = totalbombs + 1
      if row > 0 and column < 9:
        if bombfield[row - 1][column + 1] == 1:
          totalbombs = totalbombs + 1
      if row < 9 and column < 9:
        if bombfield[row + 1][column + 1] == 1:
          totalbombs = totalbombs + 1
      square.config(text=" " + str(totalbombs) + " ")
      squaresToClear = squaresToClear - 1
      score = score + 1
      if squaresToClear == 0:
        gameOver = True
        print("Well done! you found all the safe squares")
        print("Your scor was:", score)
        print(
          " -----------------------------------------Restart----------------------------------"
        )
