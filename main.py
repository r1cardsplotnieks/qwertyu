import random
import csv

CRED = '\033[91m'
CEND = '\033[0m'
D = '\033[36m'
def janis():
  print("Spēles nosaukums - ", CRED + "Slapjie bandīti" + CEND)
  print("Autori - Ričards Plotnieks, Rainers Jānis Sprincis")

janis()

def nokrisni():
  nejaus = random.randint(1, 2)
  if nejaus == 1:
    cela_garums = 80
    print("Pašreiz ārā līst lietus. Var nobraukt 80km.")
  else:
    cela_garums = 140
    print("Pašreiz ārā spīd saule. Var nobraukt 140km.")
  return cela_garums

def sleep():
  import time
  time.sleep(1)

def noteikumi():
    noteikumi1 = open("noteikumi.csv", "r")
    lasa = csv.DictReader(noteikumi1)
    for rinda in lasa:
        print(rinda['noteikumi'])
    noteikumi1.close()



def laiks():
  import time
  seconds = time.time()
  local_time = time.ctime(seconds)
  print(CRED + "Laiks, kad sākāt spēli:" + CEND, local_time)

laiks()


def valmiera():
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['valmiera'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Pareiza atbilde!")
      punkti += 1
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    y = nokrisni() - int(rinda['k1'])
  print("Jūs vēl varat nobraukt:", str(y) + "km.")
  print("Nākamais kontrolpunkts - Cēsis!")
  sleep()
  jautajumi1.close()
  return y



def cesis():
  a = valmiera()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k2'])
    if (a - z) < 0:
      print()
      print("Jūsu elektroauto ir vajadzīga uzlāde!")
      c = nokrisni() - int(z)
      print("Uzlādēts!")
    else:
      print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
      c = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['cesis'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Nepareiza atbilde!")
    elif atbilde == '2':
      print("Pareiza atbilde!")
      punkti += 1
    elif atbilde == '3':
      print("Nepareiza atbilde!")
      punkti += 1
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(c) + "km")
  sleep()
  jautajumi1.close()
  return c


def sigulda():
  a = cesis()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k3'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    b = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
    b = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['sigulda'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Pareiza atbilde!")
      punkti += 1
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(b) + "km.")
  sleep()
  jautajumi1.close()
  return b
#skaititajs()


def riga():
  a = sigulda()
  x1 = open("kontrolpunkti.csv","r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k4'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    v = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
    v = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['riga'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      punkti += 1
      print("Pareizā atbilde!")
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(v) + "km.")
  sleep()
  jautajumi1.close()
  return v


def jurmala():
  a = riga()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k5'])
    if a - z < 0:
      print("Jūsu elektroauto ir vajadzīga uzlāde!")
      n = nokrisni() - z
      print("Uzlādēts!")
    else:
      print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
      n = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['jurmala'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      punkti += 1
      print("Atbilde pareiza!")
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(n) + "km.")
  sleep()
  jautajumi1.close()
  return n

def jelgava():
  a = jurmala()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k6'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    m = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
    m = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['jelgava'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Pareiza atbilde!")
      punkti += 1
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(m) + "km.")
  sleep()
  jautajumi1.close()
  return m

def dobele():
  a = jelgava()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k7'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    s = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
    s = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['dobele'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '2':
      print("Atbilde pareiza!")
      punkti += 1
    elif atbilde == '3':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(s) + "km.")
  sleep()
  jautajumi1.close()
  return s

def saldus():
  a = dobele()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k8'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    d = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
    d = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['saldus'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      punkti += 1
      print("Atbilde pareiza!") 
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(d) + "km.")
  sleep()
  jautajumi1.close()
  return d

def skrunda():
  a = saldus()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k9'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    f = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
    f = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['skrunda'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      print("Atbilde pareiza!")
      punkti += 1
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs vēl varat nobraukt:", str(f) + "km.")
  sleep()
  jautajumi1.close()
  return f

def liepaja():
  a = skrunda()
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k8'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    g = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde nav Jūsu elektroauto nav vajadzīga.")
    g = a - z
  punkti = 0
  skaits = 1
  jautajumi1 = open("jautajumi.csv", "r")
  lasa = csv.DictReader(jautajumi1)
  for rinda in lasa:
    print(rinda['liepaja'])
  while punkti != skaits:
    atbilde = input("Ievadiet atbildi: ")
    if atbilde == '1':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '2':
      print("Nepareiza atbilde!")
      punkti += 0
    elif atbilde == '3':
      punkti += 1
      print("Atbilde pareiza!")
    elif atbilde == 'noteikumi':
      noteikumi()
      punkti += 0
    else:
      print("Ievadīts nepareizs simbols/atbilde!")
      punkti += 0
  print("Jūs esat pabeiguši šo spēli!")
  f1 = open("saglabats.csv", "w")
  lauki = ["Vards","Punkti"] 
  raksta = csv.DictWriter(f1, fieldnames=lauki,delimiter=",") 
  for i in range(1):
    x=input(CRED + "Ievadi savu vārdu: " + CEND)
    y=input(a)
    raksta.writerow({"Vards": x,"Punkti": y})
  jautajumi1.close()
  f1.close()


liepaja()


def laiks2():
  import time
  seconds = time.time()
  local_time = time.ctime(seconds)
  print("Laiks, kad beidzāt spēli:", local_time)




laiks2()