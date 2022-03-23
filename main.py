import random
import csv

def x():
  x1 = open("kontrolpunkti.csv","r")
  lasa1 = csv.DictReader(x1)
  return lasa1

def nokrisni():
  nejaus = random.randint(1,2)
  if nejaus == 1:
    cela_garums = 80
  else:
    cela_garums = 140
  return cela_garums

def noteikumi():
  noteikumi1 = open("noteikumi.csv","r")
  lasa = csv.DictReader(noteikumi1)
  for rinda in lasa:
    print(rinda['noteikumi'])
  noteikumi1.close()
    
def jautajumi():
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)

def pareiza_atbilde():
  print("Tā bija pareizā atbilde! +5 bonusa punkti!")
  bonus_punkti += 5
  return bonus_punkti

def nepareiza_atbilde1():
  print("Tā bija nepareiza atbilde! Mēģiniet vēlreiz!")

def nepareiza_atbilde():
  print("Tā bija nepareiza atbilde! Mēģiniet vēlreiz! -1 bonusa punkts!")
  bonus_punkti -= 1
  return bonus_punkti

def valmiera():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['valmiera'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pareiza_atbilde()
      punkti += 1
    elif atbilde == '2':
      nepareiza_atbilde1()
      punkti += 0
    elif atbilde == '3':
      nepareiza_atbilde1()
      punkti += 0
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  x()
  for rinda in lasa1:
    y = nokrisni() - rinda['cesis']
    print(y)

def cesis():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['cesis'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def sigulda():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['sigulda'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pareiza_atbilde()
      punkti += 1
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def riga():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['riga'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def jurmala():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['jurmala'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def jelgava():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['jelgava'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def dobele():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['dobele'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def saldus():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['saldus'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def skrunda():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['skrunda'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0

def liepaja():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv","r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['liepaja'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      pass
    elif atbilde == '2':
      pass
    elif atbilde == '3':
      pass
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0



def attalumi():
  
def spele():
  

print(nokrisni())
