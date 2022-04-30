#avg.py
#autor: Sven Azari
#http://www.github.com/svenazari
#naredbe: del, del1, izl, show, memload, memclear
#Kako bi se mogla koristiti naredba memload, u istom folderu kao i skripta mora biti i datoteka '.avg_mem.txt'

import sys
from os import system, name
from os.path import exists

def clear (): #čišćenje zaslona
  if name == 'nt':
      _ = system('cls')
  else:
      _ = system('clear')

def average ():
    clear ()
    if exists('.avg_mem.txt') == False: #provjera da li postoji datoteka .avg_mem.txt - ako je nema, skripta ju kreira kako bi bio omogućen upis nakon kalkulacija
        f = open('.avg_mem.txt', 'w+')
    Traz = [] #lista za razlike u temperaturi zraka
    Uraz = [] #lista za razlike u relativnoj vlazi zraka
    while True:
        Tk = input ("Tk = ") #temperatura zraka klasično
        if Tk == "show":
            print (Traz)
            print (Uraz)
            print ("* * * ")
            continue
        elif Tk == "del":
            clear()
            try:
                del Traz[-1]
                del Uraz[-1]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Tk == "del1":
            clear()
            try:
                del Traz[0]
                del Uraz[0]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Tk == "memload": #učitavanje spremljenih podataka razlike - memload će izbrisati svaki postojeći izračun
            clear()
            Traz.clear()
            Uraz.clear()
            meml = []
            memlf = [] #float od meml
            with open('.avg_mem.txt') as mem:
                meml = mem.readlines() #čitanje linija i upis u listu
            for line in meml: #upis u novu lisu kao float
                memlx = float(line)
                memlf.append(memlx)
            x = int(len(memlf) / 2) #polovina od memlf
            Tmem = memlf[:x] #učitavanje razlike temperature
            Umem = memlf[x:] #učitavanje razlike vlage
            Traz.extend(Tmem) #dodavanje memorije na listu razlike temperature
            Uraz.extend(Umem) #dodavanje memorije na listu razlike vlage
            try:
                Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
            except ZeroDivisionError: #ako je datoteka .avg_mem.txt prazna
                print ("Učitana memorija ne sadrži podatke!")
            else:
                #ispis
                print ("# dTs = " + Tsred + " #")
                print ("# dUs = " + Usred + " #")
                print ("(Srednju razliku treba dodati na podatak AMP-a)")
                print ("* * * ")
            continue
        elif Tk == "memclear": #čišćenje memorije skripte
            clear()
            Traz.clear()
            Uraz.clear()
            print ("Memorija skripte je očišćena!")
            continue
        elif Tk == "izl":
            clear()
            exit()
        Ta = input ("Ta = ") #temperatura zraka automatsko
        if Ta == "show":
            print (Traz)
            print (Uraz)
            continue
        elif Ta == "del":
            clear()
            try:
                del Traz[-1]
                del Uraz[-1]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Ta == "del1":
            clear()
            try:
                del Traz[0]
                del Uraz[0]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Ta == "memload": #učitavanje spremljenih podataka razlike - memload će izbrisati svaki postojeći izračun
            clear()
            Traz.clear()
            Uraz.clear()
            meml = []
            memlf = [] #float od meml
            with open('.avg_mem.txt') as mem:
                meml = mem.readlines() #čitanje linija i upis u listu
            for line in meml: #upis u novu lisu kao float
                memlx = float(line)
                memlf.append(memlx)
            x = int(len(memlf) / 2) #polovina od memlf
            Tmem = memlf[:x] #učitavanje razlike temperature
            Umem = memlf[x:] #učitavanje razlike vlage
            Traz.extend(Tmem) #dodavanje memorije na listu razlike temperature
            Uraz.extend(Umem) #dodavanje memorije na listu razlike vlage
            try:
                Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
            except ZeroDivisionError: #ako je datoteka .avg_mem.txt prazna
                print ("Učitana memorija ne sadrži podatke!")
            else:
                #ispis
                print ("# dTs = " + Tsred + " #")
                print ("# dUs = " + Usred + " #")
                print ("(Srednju razliku treba dodati na podatak AMP-a)")
                print ("* * * ")
            continue
        elif Ta == "memclear": #čišćenje memorije skripte
            clear()
            Traz.clear()
            Uraz.clear()
            print ("Memorija skripte je očišćena!")
            continue
        elif Ta == "izl":
            clear()
            exit()
        print ("*")
        Uk = input ("Uk = ") #vlaga zraka klasično
        if Uk == "show":
            print (Traz)
            print (Uraz)
            continue
        elif Uk == "del":
            clear()
            try:
                del Traz[-1]
                del Uraz[-1]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Uk == "del1":
            clear()
            try:
                del Traz[0]
                del Uraz[0]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Uk == "memload": #učitavanje spremljenih podataka razlike - memload će izbrisati svaki postojeći izračun
            clear()
            Traz.clear()
            Uraz.clear()
            meml = []
            memlf = [] #float od meml
            with open('.avg_mem.txt') as mem:
                meml = mem.readlines() #čitanje linija i upis u listu
            for line in meml: #upis u novu lisu kao float
                memlx = float(line)
                memlf.append(memlx)
            x = int(len(memlf) / 2) #polovina od memlf
            Tmem = memlf[:x] #učitavanje razlike temperature
            Umem = memlf[x:] #učitavanje razlike vlage
            Traz.extend(Tmem) #dodavanje memorije na listu razlike temperature
            Uraz.extend(Umem) #dodavanje memorije na listu razlike vlage
            try:
                Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
            except ZeroDivisionError: #ako je datoteka .avg_mem.txt prazna
                print ("Učitana memorija ne sadrži podatke!")
            else:
                #ispis
                print ("# dTs = " + Tsred + " #")
                print ("# dUs = " + Usred + " #")
                print ("(Srednju razliku treba dodati na podatak AMP-a)")
                print ("* * * ")
            continue
        elif Uk == "memclear": #čišćenje memorije skripte
            clear()
            Traz.clear()
            Uraz.clear()
            print ("Memorija skripte je očišćena!")
            continue
        elif Uk == "izl":
            clear()
            exit()
        Ua = input ("Ua = ") #vlaga zraka automatsko
        if Ua == "show":
            print (Traz)
            print (Uraz)
            continue
        elif Ua == "del":
            clear()
            try: 
                del Traz[-1]
                del Uraz[-1]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Ua == "del1":
            clear()
            try:
                del Traz[0]
                del Uraz[0]
            except: #ako su liste već prazne
                print ("Učitana memorija ne sadrži podatke!")
            else:
                try:
                    Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                    Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                except ZeroDivisionError: #ako je upravo izbrisan zadnji unos u list
                    print ("Učitana memorija ne sadrži podatke!")
                else:
                    #ispis
                    print ("# dTs = " + Tsred + " #")
                    print ("# dUs = " + Usred + " #")
                    print ("(Srednju razliku treba dodati na podatak AMP-a)")
                    print ("* * * ")
            continue
        elif Ua == "memload": #učitavanje spremljenih podataka razlike - memload će izbrisati svaki postojeći izračun
            clear()
            Traz.clear()
            Uraz.clear()
            meml = []
            memlf = [] #float od meml
            with open('.avg_mem.txt') as mem:
                meml = mem.readlines() #čitanje linija i upis u listu
            for line in meml: #upis u novu lisu kao float
                memlx = float(line)
                memlf.append(memlx)
            x = int(len(memlf) / 2) #polovina od memlf
            Tmem = memlf[:x] #učitavanje razlike temperature
            Umem = memlf[x:] #učitavanje razlike vlage
            Traz.extend(Tmem) #dodavanje memorije na listu razlike temperature
            Uraz.extend(Umem) #dodavanje memorije na listu razlike vlage
            try:
                Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
            except ZeroDivisionError: #ako je datoteka .avg_mem.txt prazna
                print ("Učitana memorija ne sadrži podatke!")
            else:
                #ispis
                print ("# dTs = " + Tsred + " #")
                print ("# dUs = " + Usred + " #")
                print ("(Srednju razliku treba dodati na podatak AMP-a)")
                print ("* * * ")
            continue
        elif Ua == "memclear": #čišćenje memorije skripte
            clear()
            Traz.clear()
            Uraz.clear()
            print ("Memorija skripte je očišćena!")
            continue
        elif Ua == "izl":
            clear()
            exit()
        clear ()
        try:
            Tkf = float (Tk)
            Taf = float (Ta)
            Ukf = float (Uk)
            Uaf = float (Ua)
        except ValueError: #ako su svi podaci uneseni, ali ne u pravom obliku (, umjesto .)
            try: #zamijeni decimalne zareze točkama i potom pretvaraj u float
                Tkx = Tk.replace(",",".")
                Tax = Ta.replace(",",".")
                Ukx = Uk.replace(",",".")
                Uax = Ua.replace(",",".")
                Tkf = float(Tkx)
                Taf = float(Tax)
                Ukf = float(Ukx)
                Uaf = float(Uax)
                Tra = round(Tkf - Taf,1)
                Ura = round(Ukf - Uaf)
                Traz.append(Tra) #dodavanje razlike na listu temperature zraka
                Uraz.append(Ura) #dodavanje razlike na listu relativne vlage zraka
                Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
                Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
                #ispis
                print ("# dTs = " + Tsred + " #")
                print ("# dUs = " + Usred + " #")
                print ("(Srednju razliku treba dodati na podatak AMP-a)")
                print ("* * * ") 
                #spremanje razlike za učitavanje kod novog pokretanja skripte 
                Trazs = []
                Urazs = []
                for line in Traz: #pretvaranje u str
                    lines = str(round(line,1))
                    Trazs.append(lines) #upis str u Trazs
                for line in Uraz:
                    lines1 = str(round(line))
                    Urazs.append(lines1) #upis str u Urazs
                upis = open(".avg_mem.txt", "w") #otvaranje datoteke za upis
                for line in Trazs: #upis razlike temperature
                    upis.write(line)
                    upis.write('\n')
                for line in Urazs: #upis razlike vlage
                    upis.write(line)
                    upis.write('\n')
                upis.close() #zatvaranje datoteke
            except ValueError: #ako nije moguće pretoviriti u float
                print ("Nedostaje podatak ili podaci nisu uneseni u odgovarajućem obliku!")
                continue
        else:
            Tra = round(Tkf - Taf,1)
            Ura = round(Ukf - Uaf)
            Traz.append(Tra) #dodavanje razlike na listu temperature zraka
            Uraz.append(Ura) #dodavanje razlike na listu relativne vlage zraka
            Tsred = str(round(sum(Traz) / len(Traz),1)) #izračun prosječne vrijednosti razlike temperature zraka (len(Traz) - dužina liste)
            Usred = str(round(sum(Uraz) / len(Uraz))) #izračun prosječne vrijednosti razlike relativne vlage zraka
            #ispis
            print ("# dTs = " + Tsred + " #")
            print ("# dUs = " + Usred + " #")
            print ("(Srednju razliku treba dodati na podatak AMP-a)")
            print ("* * * ") 
            #spremanje razlike za učitavanje kod novog pokretanja skripte 
            Trazs = []
            Urazs = []
            for line in Traz: #pretvaranje u str
                lines = str(round(line,1))
                Trazs.append(lines) #upis str u Trazs
            for line in Uraz:
                lines1 = str(round(line))
                Urazs.append(lines1) #upis str u Urazs
            upis = open(".avg_mem.txt", "w") #otvaranje datoteke za upis
            for line in Trazs: #upis razlike temperature
                upis.write(line)
                upis.write('\n')
            for line in Urazs: #upis razlike vlage
                upis.write(line)
                upis.write('\n')
            upis.close() #zatvaranje datoteke
        if Tk == "izl" or Ta == "izl" or Uk == "izl" or Ua == " izl":
            break
    exit ()

average()
