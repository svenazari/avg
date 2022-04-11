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
