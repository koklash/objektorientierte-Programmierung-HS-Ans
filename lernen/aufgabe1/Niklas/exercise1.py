'''
Lektion 1

    Als erstes schauen wir uns an, wie man for-Schleifen in Python schreibt (achte auf die Syntax).

    Bsp:
        zahlen = [1][2][3][4][5][6][7]          # Liste initialisieren, durch die wir iterieren wollen (Liste = Array)
        for zahl in zahlen:                     # Anfang der Schleife (wiederhole für jedes Element in 'zahlen')
            print(zahl)                         # Hier geben wir jede einzelne Zahl aus


    Hier, falls du einen tieferen Einblick haben möchtest: https://www.w3schools.com/python/python_for_loops.asp


Lektion 2
    
    Als nächstes schauen wir uns an, wie wir Dateien in einem Ordner auflisten können.
    Dafür benutzen wir das eingebaute Modul ‘os’, das mit Python mitgeliefert wird

    Bsp:
        import os                                 # Modul importieren

        dateien = os.listdir("data/7")            # Liste aller Dateinamen im Ordner mit dem relativen Pfad "data/7" als Liste in der Variable 'dateien' speichern
        print(dateiname[0])                       # Ersten Dateinamen ausgeben (Index 0 = erstes Element)

        
Mini-Aufgabe 1

Kombiniere jetzt das Wissen aus beiden Lektionen:
Schreibe Code, der:
	1.	Das os Modul importiert
	2.	Alle Dateien in einer Variable speichert
	3.	Mit einer for-Schleife durch diese Liste iteriert und jeden Dateinamen mit print() ausgibt
            
'''

import os


datein = os.listdir("data/7")
for datei in datein:
    print(datei)




