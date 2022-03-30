import random
import csv
CRED = '\033[91m'
CEND = '\033[0m'
D = '\033[36m'
def nokrisni():
  nejaus = random.randint(1, 2)
  if nejaus == 1:
    cela_garums = 80
    print("Pašreiz ārā līst lietus.")
  else:
    cela_garums = 140
    print("Pašreiz ārā spīd saule.")
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

def ievads():
  print("Spēles nosaukums - ", CRED + "Slapjie bandīti" + CEND)
  print("Autori - Ričards Plotnieks, Rainers Jānis Sprincis")
  print("Spēlē jāspiež tastatūras poga'Enter'.")
  noteikumi()
ievads()
def laiks():
  import time
  seconds = time.time()
  local_time = time.ctime(seconds)
  print(CRED + "Laiks, kad sākāt spēli:" + CEND, local_time)

laiks()
def valmiera():
  print("1. kontrolpunkts - Svētā Sīmaņu baznīca.")
  sleep()
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
    print("Nākamais kontrolpunkts - Cēsis,",str(rinda['k1'])+"km attālumā.")
  print("Jūs vēl varat nobraukt:", str(y) + "km.")
  sleep()
  jautajumi1.close()
  return y



def cesis():
  print("2. kontrolpunkts - Cēsu pils.")
  sleep()
  a = valmiera()
  print("Jūs esat nonākuši Cēsu pilī.")
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
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Sigulda,",str(39)+"km attālumā.")
  print("Jūs vēl varat nobraukt:", str(c) + "km")
  sleep()
  jautajumi1.close()
  return c


def sigulda():
  print("3. kontrolpunkts - Turaidas pils.")
  sleep()
  a = cesis()
  print("Jūs esat nonākuši Turaidas pilī.")
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k3'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    b = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Rīga,",str(52)+"km attālumā.")
  sleep()
  jautajumi1.close()
  return b



def riga():
  print("4. kontrolpunkts - Brīvības piemineklis.")
  sleep()
  a = sigulda()
  print("Jūs esat nonākuši pie Brīvības pieminekļā.")
  x1 = open("kontrolpunkti.csv","r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k4'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    v = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Jūrmala,",str(80)+"km attālumā.")
  sleep()
  jautajumi1.close()
  return v


def jurmala():
  print("5. kontrolpunkts - Majoru pludmale.")
  sleep()
  a = riga()
  print("Jūs esat nonākuši Majoru pludmalē.")
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k5'])
    if a - z < 0:
      print("Jūsu elektroauto ir vajadzīga uzlāde!")
      n = nokrisni() - z
      print("Uzlādēts!")
    else:
      print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Jelgava,",str(57)+"km attālumā.")
  sleep()
  jautajumi1.close()
  return n

def jelgava():
  print("6. kontrolpunkts - Kurzemes hercogu kapenes.")
  sleep()
  a = jurmala()
  print("Jūs esat nonākuši Kurzemes hercogu kapenēs.")
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k6'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    m = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Dobele,",str(28)+"km attālumā.")
  sleep()
  jautajumi1.close()
  return m

def dobele():
  print("7. kontrolpunkts - Dobeles pils.")
  sleep()
  a = jelgava()
  print("Jūs esat nonākuši Dobeles pilī.")
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k7'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    s = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Saldus,",str(54)+"km attālumā.")
  sleep()
  jautajumi1.close()
  return s

def saldus():
  print("8. kontrolpunkts - Kalnsētas parks.")
  sleep()
  a = dobele()
  print("Jūs esat nonākuši Kalnsētas parkā.")
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k8'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    d = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Skrunda,",str(32)+"km attālumā.")
  sleep()
  jautajumi1.close()
  return d

def skrunda():
  print("9. kontrolpunkts - Skrundas lokators.")
  sleep()
  a = saldus()
  print("Jūs esat nonākuši pie Skrundas lokatora.")
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k9'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    f = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Nākamais kontrolpunkts - Liepāja,",str(68)+"km attālumā.")
  sleep()
  jautajumi1.close()
  return f

def liepaja():
  print("10. kontrolpunkts - Koncertzāle 'Lielais dzintars'")
  sleep()
  a = skrunda()
  print("Jūs esat nonākuši pie koncertzāles 'Lielais dzintars'.")
  x1 = open("kontrolpunkti.csv", "r")
  lasa1 = csv.DictReader(x1)
  for rinda in lasa1:
    z = int(rinda['k8'])
  if a - z < 0:
    print("Jūsu elektroauto ir vajadzīga uzlāde!")
    g = nokrisni() - z
    print("Uzlādēts!")
  else:
    print("Uzpilde Jūsu elektroauto nav vajadzīga.")
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
  print("Jūs esat pabeiguši šo spēli! Punkti ir atlikušais kilometru skaits, ko Jūsu elektroauto var nobraukt!")
  f1 = open("saglabats.csv", "a")
  lauki = ["Vards","Punkti"] 
  raksta = csv.DictWriter(f1, fieldnames=lauki,delimiter=",") 
  for i in range(1):
    x=input(CRED + "Ievadi savu vārdu: " + CEND)
    raksta.writerow({"Vards": x,"Punkti": g})
  jautajumi1.close()
  f1.close()


liepaja()
def laiks2():
  import time
  seconds = time.time()
  local_time = time.ctime(seconds)
  print("Laiks, kad beidzāt spēli:", local_time)

laiks2()