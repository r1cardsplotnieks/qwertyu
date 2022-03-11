import csv as csv
import numpy as np
from PIL import Image
#myImage = Image.open("filter(function, iterable).jpg");
#myImage.show();

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
    print("Tagad ārā līst lietus, zibeņi zibšņ - 80km")
    
  elif b == 2:
    print("Tagad ārā spīd skaista saulīte - 140km")
  else:
    print("Nogājusi kļūda, laikapstākļi šodienai nav pieejami!")
  fails1 = open("kontrolpunkti.csv","r")
  lasa = csv.DictReader(fails1)
  lauki = ['k1','k2','k3','k4','k5','k6','k7','k8','k9']

  
CRED = '\033[91m'
CEND = '\033[0m'
D = '\033[36m'

import os

def cls():
    import time
    time.sleep(5)
    os.system('cls' if os.name=='nt' else 'clear')
import csv
def rekinal():
  fails1 = open("kontrolpunkti.csv","r")
  lasa = csv.DictReader(fails1)
  for rinda in lasa:
    print(80-int(rinda['k1']))
rekinal()
def rekinas():
  fails1 = open("kontrolpunkti.csv","r")
  lasa = csv.DictReader(fails1)
  for rinda in lasa:
    print(140-int(rinda['k1']))
rekinas()
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

cls()
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
      lietus()
    else: 
      saule()
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
  cls()



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
def sveikini():
  import random
  j = random.randint(1, 3)
  if j == 1:
    return "59%"
  elif j == 2:
    return "68%"
  elif j == 3:
    return "79%"
  else:
    return "99,9%"

def laicins():
  import random
  h = random.randint(1, 3)
  if h == 1:
    return "14:34"
  elif h == 2:
    return "16:34"
  elif h == 3:
    return "11:50"
  else:
    return "99,9%"

  
def cesis():
  global punkti
  sleep()
  print(CRED +"Jums zvana spēlēs rīkotāji par telefonu! Viņi Jums stāsta: " + CEND)
  sleep()
  print("Heyā, heyā! Sveicināts Cēsīs, vienā no vecākajām Latvijas pilsētām!")
  sleep()
  print("Kā izskātas Cēsu pils? Vai tā tik nav smuka?")
  sleep()
  print("Tu jau zini, kas sagaida! Jāatbild uz mūsu izdomātu jautājumu. Šoreiz jautājums nav par apskates objektu, bet tāpat tas ir interesants! Atbildi kamēr vari. Pašreiz tev ir: ", punkti, "punktu")
  sleep()
  print("Kurā gadā Cēsis ieguva pilsētu tiesības?")
  print("(1) - 1245. gadā")
  print("(2) - 1323. gadā")
  k=0
  s=1
  while s != k:
    z = input("Atbilde: ")
    if z == "2":
      print("Precīza atbilde! Jums tiek piešķirts 1. punkts par atbildi")
      punkti += 1
      print("Pašreiz Jums ir:", punkti, "punkti/-s")
      k+=1
    elif z == "1":
      print("Diemžēl, atbilde nav pareiza. Mēģiniet vēlreiz! - 0,5p")
      punkti -= 0.5 
      print("Pašreiz Jums ir:", punkti, "punkti/-s")
      k+=0
    elif z == "n":
      noteikumi()
      k+=0
    else:
      print("Netika ievadīts neviens no piedāvātājiem skaitļiem!")
      k+=0  
  print("Jautājums ir atbildēts, varam turpināt spēli!")
  sleep()
  print("Pašreiz tavs akumulatora uzlādes daudzums ir:", sveikini())
  sleep()
  print("Pašreizējais laiks ir:", laicins())
  print("------------------------------------------------")  

def sigulda():
  sleep()
  print(CRED + "Jums zvana spēles rīkotaji, viņi stāsta: " + CEND)
  print("Sveicināts Siguldā!")

def uzladesstacija():
  print("Atceries, ka jaizvēlās pats tuvākais, jo var nesanākt akumulatora uzlādes daudzums")
  sleep()

def protams():
  print("Nu pienācis nākamais solis. Vai dosieties uz nākamo kontrolpunktu un riskēsiet, vai brauksiet uzlādēt savu akumulatoru?")
  sleep()
  print("Atgādinājums:", sveikini(), "palikuši akumulatora daudzums")
  sleep()
  print("(1) - Kontrolpunkts")
  print("(2) - Uzlādes stacija")
  k=0
  s=1
  while s != k:
    c = input("Atbilde: ")
    if c == "1":
      print("Labi, tad Jūsu otrais kontrolpunkts - Sigulda ! Lai Jums veiksmīgs brauciens! ")
      sigulda()
      k+=1
    elif c == "2":
      print("Izvēlaties lūdzu, uz kuru TUVĀKO uzlādes staciju brauksiet?(no 3-6): ")
      uzladesstacija()
      k+=1
    elif c == "n":
      noteikumi()
      k+=0
    else:
      print("Nesapratu atbildi, lūdzu mēģiniet vēlreiz!")
      k+=0
  

cesis()

protams()