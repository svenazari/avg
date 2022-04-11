#avg.py - GUI
#autor: Sven Azari
#http://www.github.com/svenazari

import PySimpleGUI as sg
from os.path import exists
import os

if exists('.avg_mem.txt') == False: #provjera da li postoji datoteka .avg_mem.txt - ako je nema, skripta ju kreira kako bi bio omogućen upis nakon kalkulacija
        f = open('.avg_mem.txt', 'w+')

sg.theme("DarkGrey")
layout = [  [sg.Text("Tk = "), sg.InputText(size=(4,1), key='tk'), sg.Text("Klasično mjerenje temperaure zraka", text_color='blue')],
	    [sg.Text("Ta = "), sg.InputText(size=(4,1), key='ta'), sg.Text("Automatsko mjerenje temperaure zraka", text_color='blue')],
	    [sg.Text('', text_color='yellow', key='sdt'), sg.Text('', text_color='red', key='Tlis')], #mjesto za ispis srednje razlike mjerenja temperature zraka
	    [sg.Text("* * *")],
	    [sg.Text("Uk = "), sg.InputText(size=(4,1), key='uk'), sg.Text("Klasično mjerenje vlage zraka", text_color='blue')],
	    [sg.Text("Ua = "), sg.InputText(size=(4,1), key='ua'), sg.Text("Automatsko mjerenje vlage zraka", text_color='blue')],
	    [sg.Text('', text_color='yellow', key='sdu'), sg.Text('', text_color='red', key='Ulis')], #mjesto za ispis srednje razlike mjerenja relativne vlage zraka
	    [sg.Text("Izračunane vrijednosti treba dodati vrijednosti automatskog mjerenja.", text_color='orange')],
	    [sg.Text("* * *")],
	    [sg.Button("Izračunaj"), sg.Button("Učitaj memoriju"), sg.Button("Pregled")],
	    [sg.Button("Očisti ekran"), sg.Button("Izbriši prvo"), sg.Button("Izbriši zadnje"), sg.Button("Izbriši memoriju")],
	    [sg.Button("Izlaz")]
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
                tkf = float(tk)
                taf = float(ta)
                ukf = float(uk)
                uaf = float(ua)
            except: #ako su svi podaci uneseni, ali ne u pravom obliku (, umjesto .)
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
    
    elif event == "Pregled": #pregled upisa u liste
        window['sdt'].update(Tsred)
        window['sdu'].update(Usred)
        window['Tlis'].update(Traz)
        window['Ulis'].update(Uraz)
window.close()
