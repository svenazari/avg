#avg.py - GUI
#autor: Sven Azari
#http://www.github.com/svenazari

import PySimpleGUI as sg
from os.path import exists
import os
import random

if exists('.avg_mem.txt') == False: #provjera da li postoji datoteka .avg_mem.txt - ako je nema, skripta ju kreira kako bi bio omogućen upis nakon kalkulacija
        f = open('.avg_mem.txt', 'w+')

#Pomjena teme
#1 - DarkGrey
#2 - Black
#3 - Topanga
#4 - DarkPurple4
#tema = 1 #fiksni odabir teme
tema = random.randrange(1,5,1) #nasumični odabir teme prikom svakog pokretanja skirpte

if tema == 1:
    sg.theme("DarkGrey")
elif tema == 2:
    sg.theme("Black")
elif tema == 3:
    sg.theme("Topanga")
elif tema == 4:
    sg.theme("DarkPurple4")


layout = [  [sg.Text("Tk = "), sg.InputText(size=(4,1), key='tk'), sg.Text("Klasično mjerenje temperaure zraka", text_color='blue')],
	    [sg.Text("Ta = "), sg.InputText(size=(4,1), key='ta'), sg.Text("Automatsko mjerenje temperaure zraka", text_color='blue')],
	    [sg.Text('', text_color='yellow', key='sdt'), sg.Text('', text_color='red', key='Tlis')], #mjesto za ispis srednje razlike mjerenja temperature zraka
	    [sg.Text("* * *")],
	    [sg.Text("Uk = "), sg.InputText(size=(4,1), key='uk'), sg.Text("Klasično mjerenje vlage zraka", text_color='blue')],
	    [sg.Text("Ua = "), sg.InputText(size=(4,1), key='ua'), sg.Text("Automatsko mjerenje vlage zraka", text_color='blue')],
	    [sg.Text('', text_color='yellow', key='sdu'), sg.Text('', text_color='red', key='Ulis')], #mjesto za ispis srednje razlike mjerenja relativne vlage zraka
	    [sg.Text("Izračunane vrijednosti treba dodati vrijednosti automatskog mjerenja.", text_color='orange')],
        [sg.Button("Izračunaj"), sg.Button("Učitaj memoriju"), sg.Button("Pregled")],
        [sg.Button("Izbriši prvo"), sg.Button("Izbriši zadnje"), sg.Button("Izbriši memoriju")],
        [sg.Text("Izračun vrijednosti temperature i vlage zraka sa korekcijom", text_color="yellow")],
        [sg.Text("T = "), sg.InputText(size=(4,1), key='t'), sg.Text('', text_color='yellow', key='ti')],
        [sg.Text("U = "), sg.InputText(size=(4,1), key='u'), sg.Text('', text_color='yellow', key='ui')],
	    [sg.Button("Izračuaj T i U"), sg.Button("Očisti ekran"), sg.Button("Pomoć"), sg.Button("Izlaz")]
         ]

window = sg.Window("AVG.py").Layout(layout)

Traz = [] #lista razlika temperature zraka
Uraz = [] #lista razlika relativne vlage zraka
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Izlaz":
        break
   
    if event == "Izračunaj": #računanje srednjih razlika
        #preuzimanje vrijednosti
        try:
            tk = values['tk']
            ta = values['ta']
            uk = values['uk']
            ua = values['ua']
        except: #ako nije unesen neki od traženih podataka
            sg.Print("Nedostaje neki podatak!")
        else:
            try:
                #float vrijednosti
                tkf = float(tk.replace(",","."))
                taf = float(ta.replace(",","."))
                ukf = float(uk.replace(",","."))
                uaf = float(ua.replace(",","."))
            except: #ako nije moguća pretvorba u float
                sg.Print ("Nedostaje podatak ili podaci nisu uneseni u odgovarajućem obliku!")
            else:
                #računanje razlike
                dt = round(tkf - taf,1)
                du = round(ukf - uaf)
                #dodavanje na listu
                Traz.append(dt)
                Uraz.append(du)
                #računanje
                Tsred = round(sum(Traz) / len(Traz),1)
                Usred = round(sum(Uraz) / len(Uraz))
                #spremanje u .avg_mem.txt
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
                #ispis
                window['sdt'].update(Tsred)
                window['sdu'].update(Usred)
                window['tk'].update('')
                window['ta'].update('')
                window['uk'].update('')
                window['ua'].update('')
                window['Tlis'].update('')
                window['Ulis'].update('')
    
    elif event == "Izbriši prvo": #brisanje najstarijeg unosa
        try:
            del Traz[0]
            del Uraz[0]
        except: #ako su liste već prazne
            window['sdt'].update('')
            window['sdu'].update('')
            window['tk'].update('')
            window['ta'].update('')
            window['uk'].update('')
            window['ua'].update('')
            window['Tlis'].update('')
            window['Ulis'].update('')
        else: #ako u listama nečega još ima
            try:
                Tsred = round(sum(Traz) / len(Traz),1)
                Usred = round(sum(Uraz) / len(Uraz))
            except: #ako su liste prazne nakon brisanja
                window['sdt'].update('')
                window['sdu'].update('')
                window['tk'].update('')
                window['ta'].update('')
                window['uk'].update('')
                window['ua'].update('')
                window['Tlis'].update('')
                window['Ulis'].update('')
            else:
                #ispis
                window['sdt'].update(Tsred)
                window['sdu'].update(Usred)
                window['tk'].update('')
                window['ta'].update('')
                window['uk'].update('')
                window['ua'].update('')
                window['Tlis'].update('')
                window['Ulis'].update('')
    
    elif event == "Izbriši zadnje": #brisanje zadnjeg unosa
        try:
            del Traz[-1]
            del Uraz[-1]
        except: #ako su liste već prazne
            window['sdt'].update('')
            window['sdu'].update('')
            window['tk'].update('')
            window['ta'].update('')
            window['uk'].update('')
            window['ua'].update('')
            window['Tlis'].update('')
            window['Ulis'].update('')
        else: #ako u listama nečega još ima
            try:
                Tsred = round(sum(Traz) / len(Traz),1)
                Usred = round(sum(Uraz) / len(Uraz))
            except: #ako su liste prazne nakon brisanja
                window['sdt'].update('')
                window['sdu'].update('')
                window['tk'].update('')
                window['ta'].update('')
                window['uk'].update('')
                window['ua'].update('')
                window['Tlis'].update('')
                window['Ulis'].update('')
            else:
                #ispis
                window['sdt'].update(Tsred)
                window['sdu'].update(Usred)
                window['tk'].update('')
                window['ta'].update('')
                window['uk'].update('')
                window['ua'].update('')
                window['Tlis'].update('')
                window['Ulis'].update('')
        
    elif event == "Učitaj memoriju": #učitavanje iz .avg_mem.txt datoteke
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
            sg.Print ("Učitana memorija ne sadrži podatke!")
        else:
            #ispis
            window['sdt'].update(Tsred)
            window['sdu'].update(Usred)
            window['tk'].update('')
            window['ta'].update('')
            window['uk'].update('')
            window['ua'].update('')
            window['Tlis'].update('')
            window['Ulis'].update('')
        
    elif event == "Izbriši memoriju": #brisanje memorije skripte
        Traz.clear()
        Uraz.clear()
        Tsred = 0
        Usred = 0
        window['sdt'].update('')
        window['sdu'].update('')
        window['tk'].update('')
        window['ta'].update('')
        window['uk'].update('')
        window['ua'].update('')
        window['Tlis'].update('')
        window['Ulis'].update('')
        
    elif event == "Očisti ekran": #povratak ekrana na prazne vrijednost
        window['sdt'].update('')
        window['sdu'].update('')
        window['tk'].update('')
        window['ta'].update('')
        window['uk'].update('')
        window['ua'].update('')
        window['Tlis'].update('')
        window['Ulis'].update('')
        window['t'].update('')
        window['ti'].update('')
        window['u'].update('')
        window['ui'].update('')
    
    elif event == "Pregled": #pregled upisa u liste
        try:
            window['sdt'].update(Tsred)
            window['sdu'].update(Usred)
            window['Tlis'].update(Traz)
            window['Ulis'].update(Uraz)
        except NameError: #ako skripta nema podataka za prikazati
            window['sdt'].update("Memorija skripte je prazna!")
            window['sdu'].update("Memorija skripte je prazna!")
    
    elif event == "Izračuaj T i U": #izračunavanje vrijednosti temperature i vlage izraka iz podataka automatske postaje i prosječnog odstupanja
        if len(Traz) == 0 or len(Uraz) == 0:
            window['ti'].update("Nema podataka o razlikama.")
            window['ui'].update("Nema podataka o razlikama.")
        else:
            try:
                tx = values['t']
                ux = values['u']
                txx = float(tx.replace(",","."))
                uxx = float(ux.replace(",","."))
                ty = round(sum(Traz) / len(Traz),1) #srednja razlika temperature zraka
                uy = round(sum(Uraz) / len(Uraz)) #srednja razlika vlage zraka
                #računanje
                tizra = round(txx + ty,1)
                uizra = round(uxx + uy)
                #ispis
                window['ti'].update(tizra)
                window['ui'].update(uizra)
            except ValueError:
                window['ti'].update("Potrebno upisati ovu vrijednost.")
                window['ui'].update("Potrebno upisati ovu vrijednost.")

        
    elif event == "Pomoć": #otvaranje ekrana sa tekstom kako koristiti skriptu
        sg.Print("AVG - GUI verzija")
        sg.Print("")
        sg.Print("UPUTE ZA KORIŠTENJE:")
        sg.Print("")
        sg.Print("POLJA ZA UNOS:")
        sg.Print("Tk - Unosi se podatak o temperaturi zraka dobiven klasičnim mjerenjem. Potrebno je koristiti decimalnu točku.")
        sg.Print("Ta - Unosi se podatak o temperaturi zraka dobiven mjerenjem automatske meteorološke postaje. Potrebno je koristiti decimalnu točku.")
        sg.Print("Uk - Unosi se podatak o relativnoj vlazi zraka dobiven klasičnim mjerenjem.")
        sg.Print("Ua - Unosi se podatak o relativnoj vlazi zraka dobiven mjerenjem automatske meteorološke postaje.")
        sg.Print("T - Unosi se podatak trenutne temperature zraka na automatskoj postaji kojem se zatim dodaje srednja vrijednost odstupanja.")
        sg.Print("U - Unosi se podatak trenutne relativne zraka na automatskoj postaji kojem se zatim dodaje srednja vrijednost odstupanja.")
        sg.Print("")
        sg.Print("GUMBI ZA NAREDBE:")
        sg.Print("IZRAČUNAJ - Izračunava razliku između mjerenja. Podatke o razlikama unosi u memoriju skripte te potom računa prosječnu razliku i ispisuje je na ekranu. Prilikom korištenja ove naredbe, nove izračunate vrijednosti razlika se automatski upisuju u .avg_mem.txt datoteku.")
        sg.Print("UČITAJ MEMORIJU - Učitava podatke iz .avg_mem.txt datoteke koja se treba nalaziti u istoj mapi kao i skripta ili u mapi iz koje se pokreće terminal. Ova naredba će izbrisati postojeću memoriju skripte.")
        sg.Print("PREGLED - Prikazuje sadržaj listi u koje su spremljene razlike vrijednosti mjerenja.")
        sg.Print("OČISTI EKRAN - Čisti sadržaj ekrana i pokazuje grafičko sučelje prazno kao pri pokretanju skripte. Ne briše sadržaj memorije.")
        sg.Print("IZBRIŠI PRVO - Briše najstariji unos u liste memorije skripte.")
        sg.Print("IZBRIŠI ZADNJE - Briše najstariji unos u liste memorije skripte.")
        sg.Print("IZBRIŠI MEMORIJU - Briše sav sadržaj lista memorije skripte, ali ne briše memoriju spremljenu u .avg_mem.txt datoteku.")
        sg.Print("IZRAČUNAJ U i I - dodavanje srednje vrijednosti odstupanja na upisane trenitne vrijednosti sa automatske meteorološke postaje.")

window.close()
