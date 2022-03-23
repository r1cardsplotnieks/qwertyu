import random
import csv


def nokrisni():
    nejaus = random.randint(1, 2)
    if nejaus == 1:
        cela_garums = 80
    else:
        cela_garums = 140
    return cela_garums

def noteikumi():
    noteikumi1 = open("noteikumi.csv", "r")
    lasa = csv.DictReader(noteikumi1)
    for rinda in lasa:
        print(rinda['noteikumi'])
    noteikumi1.close()


def jautajumi():
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)


#def pareiza_atbilde():
    #print("upenu saldejums xD")
    #bonus_punkti += 5


def nepareiza_atbilde1():
    print("Tā bija nepareiza atbilde! Mēģiniet vēlreiz!")


def nepareiza_atbilde():
  pass
  #print("Tā bija nepareiza atbilde! Mēģiniet vēlreiz! -1 bonusa punkts!")
  #bonus_punkti -= 1
  #return bonus_punkti


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
            #pareiza_atbilde()
            punkti += 1
        elif atbilde == '2':
            #nepareiza_atbilde1()
            punkti += 0
        elif atbilde == '3':
            #nepareiza_atbilde1()
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
    return y


def cesis():
    a = valmiera()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k2'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        c = nokrisni() - z
        print(c)
    else:
        print("uzpilde nav vajadziga")
        c = a - z
        print(c)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['cesis'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            pass
        elif atbilde == '2':
            punkti += 1
        elif atbilde == '3':
            pass
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(c) + "km")
    return c


def sigulda():
    a = cesis()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k3'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        b = nokrisni() - int(z)
        print(b)
    else:
        print("uzpilde nav vajadziga")
        b = a - z
        print(b)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['sigulda'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
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
    print("Jūs vēl varat nobraukt:", str(b) + "km.")
    return (b)


def riga():
    a = sigulda()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k4'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        v = int(nokrisni()) - z
        print(v)
    else:
        print("uzpilde nav vajadziga")
        v = a - z
        print(v)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['riga'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            print("Atbilde nav pareiza - p")
            punkti += 0
        elif atbilde == '2':
            print("Atbilde nav pareiza -p")
            punkti += 0
        elif atbilde == '3':
            punkti += 1
            print("Pareizā atbilde + 5p ")
            #pareiza_atbilde()
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(v) + "km.")
    return v


def jurmala():
    a = riga()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k5'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        n = int(nokrisni()) - z
        print(n)
    else:
        print("uzpilde nav vajadziga")
        n = a - z
        print(n)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['jurmala'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            print("Atbilde nav pareiza -p")
            punkti += 0
        elif atbilde == '2':
            print("Atbilde nav pareiza -p")
            punkti += 0
        elif atbilde == '3':
            punkti += 1
            print("Atbilde pareiza + 5p")
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(n) + "km.")
    return n


def jelgava():
    a = jurmala()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k6'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        m = int(nokrisni()) - z
        print(m)
    else:
        print("uzpilde nav vajadziga")
        m = a - z
        print(m)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['jelgava'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            punkti += 1
        elif atbilde == '2':
            print("Atbilde nav pareiza -p")
            punkti += 0
        elif atbilde == '3':
            print("Atbilde nav pareiza -p")
            punkti += 0
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(m) + "km.")
    return m


def dobele():
    a = jelgava()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k7'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        s = int(nokrisni()) - z
        print(s)
    else:
        print("uzpilde nav vajadziga")
        s = a - z
        print(s)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['dobele'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            print("Atbilde nepareiza - p")
            punkti += 0
        elif atbilde == '2':
            print("Atbilde pareiza + 5p")
            punkti += 1
        elif atbilde == '3':
            print("Atbilde nepareiza - p")
            punkti += 0
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(s) + "km.")
    return s


def saldus():
    a = dobele()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k8'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        d = int(nokrisni()) - z
        print(d)
    else:
        print("uzpilde nav vajadziga")
        d = a - z
        print(d)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['saldus'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            punkti += 0
            print("Atbilde nepareiza - p")
        elif atbilde == '2':
            punkti += 0
            print("Atbilde nepareiza - p")
        elif atbilde == '3':
            punkti += 1
            print("Atbilde pareiza + 5p")
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(d) + "km.")
    return d


def skrunda():
    a = saldus()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k9'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        f = int(nokrisni()) - z
        print(f)
    else:
        print("uzpilde nav vajadziga")
        f = a - z
        print(f)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['skrunda'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            print("Atbilde nepareiza - p")
            punkti += 0
        elif atbilde == '2':
            print("Atbilde mepareiza - p")
            punkti += 0
        elif atbilde == '3':
            print("Atbilde pareiza + 5p")
            punkti += 1
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(f) + "km.")
    return f


def liepaja():
    a = skrunda()
    x1 = open("kontrolpunkti.csv", "r")
    lasa1 = csv.DictReader(x1)
    for rinda in lasa1:
        z = int(rinda['k8'])
    if a - z < 0:
        print("vajadziga uzpilde")
        nokrisni()
        g = int(nokrisni()) - z
        print(g)
    else:
        print("uzpilde nav vajadziga")
        g = a - z
        print(g)
    punkti = 0
    skaits = 1
    jautajumi1 = open("jautajumi.csv", "r")
    lasa = csv.DictReader(jautajumi1)
    for rinda in lasa:
        print(rinda['liepaja'])
    while punkti != skaits:
        atbilde = input("Ievadiet atbildi: ")
        if atbilde == '1':
            punkti += 0
            print("Nav")
        elif atbilde == '2':
            punkti += 0
            print("Nav -p")
        elif atbilde == '3':
            punkti += 1
            print("Atbilde pareiza + 5p")
        elif atbilde == 'noteikumi':
            noteikumi()
            punkti += 0
        else:
            print("Ievadīts nepareizs simbols/atbilde!")
            punkti += 0
    print("Jūs vēl varat nobraukt:", str(g) + "km.")
    return g


def attalumi():
    pass


def spele():
    pass


liepaja()
