print("------------------------------------------------")
print("------------------------------------------------")
print("------------------------------------------------")
CRED = '\033[91m'
CEND = '\033[0m'
D = '\033[36m'
def janis():
  print("Spēles nosaukums - ", CRED + "Slapjie bandīti" + CEND)
  print("Autori - Ričards Plotnieks, Rainers Jānis Sprincis")
def noteikumi():
  print("Spēles noteikumi:")
  print("1. Elektroauto bez uzlādes, labos apstākļos, spēj nobraukt 140km, bet lietus laikā 80km;")
  print("2. Spēle sākas Valmierā;")
  print("3. Katrā uzlādes stacijā tiks uzdots jautājums;")
  print("4. Spēlei sākoties, spēlētājam ir 0 punkti;")
  print("5. Uzpildoties katrā uzlādes stacijā tiek pieskaitīti 5 punkti;")
  print("6. Atbildot nepareizi uz jautājumu kontrolpunktā tiek pieskaitīts 1 punkts, kamēr nav atbildēts pareizi;")
  print("8. Spēle beidzās Liepājā;")
  print("9. Uzvar spēlētājs ar vismazāko punktu skaitu.")
  print("P.S Ja vēlies zināt noteikumus spēles laikā, kad Jums tiek prasīta atbilde, ievadiet mazo burtu", CRED + "n" + CEND)

punkti = 0
  
janis()
noteikumi()
print("------------------------------------------------")
print("------------------------------------------------")
print("------------------------------------------------")

def laikap():
  import random
  b = random.randint(1, 2)
  if b == 1:
    print("Šodien ārā līst lietus, zibeņi zibšņ")
  elif b == 2:
    print("Šodien ārā spīd skaista saulīte!")
  else:
    print("Nogājusi kļūda, laikapstākļi šodienai nav pieejami!")

CRED = '\033[91m'
CEND = '\033[0m'
D = '\033[36m'

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
import csv
def prasa():
  fails1 = open("kontrolpunkti.csv","r")
  lasa = csv.DictReader(fails1)
  lauki = ['pilseta','k1','k2','k3','k4','k5','k6','k7','k8','k9','k0',]
  for rinda in lasa:
    print(rinda[input('')])
prasa()
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def sleep():
  import time
  time.sleep(4)

def gulet():
  import time
  time.sleep(2)

def valmiera():
  gulet()
  print("Sveicināti", CRED + "Valmierā", CEND + "un savā pirmajā robežpunktā!", D + "Sv. Sīmaņu baznīca" + CEND, "ir tik skaista!")
  gulet()
  print("Labi, ka baznīca neatrodas tālu no mūsu skolas! Nebija tālu jāiet. ")
  gulet()
  print("Lai Jūs varētu doties uz nākamo robežpunktu, Jums jāatbild uz mūsu sagatavotu jautājumu!")
  gulet()
  print("Kurā gadā tika uzcelta Sv.Sīmaņu baznīca?")
  print("(1) - 1283. gadā")
  print("(2) - 1285. gadā")
  print("(3) - 1281. gadā")
  k=0
  s=1
  global punkti
  while s != k:
    a = input("Atbilde: ")
    if a == "1":
      print("Precīza atbilde! Jums tiek piešķirts 1. punkts par atbildi")
      punkti += 1
      print("Pašreiz Jums ir:", punkti, "punkti/-s")
      k+=1
    elif a == "2":
      print("Diemžēl, atbilde nav pareiza. Mēģiniet vēlreiz! - 0,5p")
      punkti -= 0.5 
      print("Pašreiz Jums ir:", punkti, "punkti/-s")
      k+=0
    elif a == "3":
      print("Diemžēl, atbilde nav pareiza. Mēģiniet vēlreiz! - 0,5p")
      punkti -= 0.5 
      print("Pašreiz Jums ir:", punkti, "punkti/-s")
      k+=0
    elif a == "n":
      noteikumi()
      k+=0
    else:
      print("Netika ievadīts neviens no piedāvātājiem skaitļiem!")
      k+=0
  print("------------------------------------------------")
  print("Labs darbs, kas padarīts! Jautājums ir atbildēts pareizi, varam doties tālāk!")

valmiera()

def vidusp():
  gulet()
  print("Pirms dodaties uz Cēsis, vai vēlaties uzzināt spēles noteikumus vēlreiz?")
  gulet()
  print("(1) - Jā")
  print("(2) - Nē")
  d = input("Atbilde: ")
  if d == "1":
    noteikumi()
  else:
    print("Labi, tad varam turpināt!")
  gulet()
  print("Šodien laikapstākļi prognozējami:")
  gulet()
  if laikap() == 1:
    print("Tā kā ārā līst lietus, elektroauto varēs nobraukt 80km, kas nozīmē, vajadzēs braukt bieži uzlādes stacijās. Ja nepieciešams, atveriet karti, lai redzētu, kur atrodas šīs stacijas!")
  else:
    print("Tā kā ārā spīd skaista saulīte, Jūsu elektroauto varēs veikt maksimālo distanci!")
  print("------------------------------------------------")
  
vidusp()


def redzams():
  import random
  y = random.randint(1, 3)
  if y == 1:
    return "zirgs"
  elif y == 2:
    return "zaķis"
  elif y == 3:
    return "stirna"
  else:
    return "kaķis"
def lietus():
  import random
  ll = random.randint(1, 3)
  if ll == 1:
    return D + "78%" + CEND, ",Jūsu atrašanās vieta - blakus Sapas"
  elif ll == 2:
    return D + "75%" + CEND, ",Jūsu atrašanās vieta - blakus Penderi"
  elif ll == 3:
    return D + "70%" + CEND, ",Jūsu atrašanās vieta - blakus Bušugrava"

def saule():
  import random
  dd = random.randint(1, 3)
  if dd == 1:
    return D + "95%" + CEND + ", Jūsu atrašanās vieta - blakus Sapas"
  elif dd == 2:
    return D + "96%" + CEND + ", Jūsu atrašanās vieta - blakus Penderi"
  elif dd == 3:
    return D + "93%" + CEND + ", Jūsu atrašanās vieta - blakus Bušugrava"
    
def us1():
  sleep()
  print("Izbraucāt no Valmieras... kāds, nu smuks skats...")
  sleep()
  print("Vai vēlaties paskatīties, cik akumulatora procentuāls daudzums palicis un kur Jūs pašreiz atrodaties (1), vai turpināt vērot brīnišķīgo skatu? (2)")
  g = input("Atbilde: ")
  if g == "1":
    print("Jūsu akumulatora daudzums ir: ")
    if laikap() == 1:
      print(lietus())
    else: 
      print(saule())
  elif g == "n":
    noteikumi()
  else:
    print("Paskaties, vai tas tik nav -", redzams())
  sleep()
  print("Braucat.. braucat...")
  sleep()
  print("Pabraucāt garām Jaunkalne, nozīmē, ka tuvojaties!")
  sleep()
  print("------------------------------------------------")
  print(CRED + "Esat veiksmīgi iebraukuši Cēsīs!" + CEND)
  print("------------------------------------------------")

def viens1():
    s = 1
    k = 0
    while s != k:
      e = input("Atbilde: ")
      if e == "1":
        print("Jūsu galamērķis - uzlādes stacija 1")
        print("Braukšanas distance - 45km")
        k +=1
      elif e == "2":
        print("Jūsu galamērķis - uzlādes stacija 2")
        print("Braukšanas distance - 50km")
        k +=1
      elif e == "3":
        print ("Jūsu galamērķis - uzlādes stacija 3")
        print("Braukšanas distance - 55km")
        k +=1
      elif e == "n":
        noteikumi()
        k +=0
      else:
        print("Lūdzu atbildiet vēlreiz!")
        k += 0

def viens():
  print("Vai Jūs vēlaties doties uz tuvāko uzlādes staciju vai braukt uz Jūsu izvēlēto kontrolpunktu?")
  print("Jūsu pašreizējais akumulatora uzlādes līmenis ir: 100%")
  print("(1) - Kontrolpunktu")
  print("(2) - Uzlādes staciju")
  k=0
  s=1
  while s != k:
    c = input("Atbilde: ")
    if c == "1":
      print("Labi, tad Jūsu pirmais robežpunkts - Cēsis! Lai Jums ir veiksmīgs brauciens. ")
      us1()
      k+=1
    elif c == "2":
      print("Izvēlaties lūdzu, uz kuru TUVĀKO uzlādes staciju brauksiet?(no 1-3): ")
      viens1()
      k+=1
    elif c == "n":
      noteikumi()
      k+=0
    else:
      print("Nesapratu atbildi, lūdzu mēģiniet vēlreiz!")
      k+=0

viens()
