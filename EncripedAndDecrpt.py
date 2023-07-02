from cryptography.fernet import Fernet

def key():
  with open("key.key","wb") as key:
    key.write(Fernet.generate_key())

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
  decypt = f.decrypt(encrepted) #idk
  with open (name, "wb") as Pd:
    Pd.write(decypt)
""" if change anthing in this file you need to update the fuchson in Apps.bombgame.bombgame.py"""