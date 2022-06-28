# avg.py
Skripta za računanje srednje vrijednosti odstupanja mjerenja automatke postaje od klaisčnih mjerenja (za temperaturu zraka i relativnu vlagu zraka).
<pre>
Autor: Sven Azari
http://www.github.com/svenazari
Potrebni programi: Python3, PySimpleGUI (za GUI verziju)
Naredbe (za CLI verziju): 
   del - brisanje zadnjeg unosa (briše zadnji upis razlike i temperature zraka i relativne vlage zraka)
   del1 - brisanje prvog unosa (briše najstariji upis razlike i temperature zraka i relativne vlage zraka)
   izl - izlaz iz skripte
   show - prikaži sve spremljenje razlike (prvi red su razlike temperature zraka, a drugi red su razlike relativne vlage zraka)
   memload - učitaj memoriju (memorija se sprema u datoteku .mem_avg.py koju će skripta kreirati prilikom prvog korištenja te koja mora biti prisutna u
             istom folderu kao i skripta prilikom učitavanja memorije)
   memclear - oćisti memoriju skripte
</pre>

NOVO:<br>
28.06.2022. - U GUI verziju dodana mogućnost upis podataka o temeraturi i vlagi zraka sa automatske meteorološke postaje kako bi skripta na te vrijednosti dodala vrijednosti srednjeg odstupanja<br>
16.06.2022. - U GUI verziji popravljen dio koda za pregled razlika u slučaju da su liste prazne. Skripta u tom slučaju se više ne ruši, već daje obavijest da su liste prazne.
