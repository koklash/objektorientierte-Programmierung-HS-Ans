import os

'''
Phase 1
    Die Grundlagen (Dateien & Pfade)

    Hier geht es nur darum, die Dateien überhaupt zu finden.
'''

'''
    Um die Beispiele auszuführen, müss der jeweilige Funktionsaufruf einkommentiert werden. 
    Diesen findest du unter den Funktionsdefinitionen.
    Bsp:

    Before:
    # lektion1()  

    After:
    lektion1()

    Wenn du fertig mit der Lektion bist, einfach wieder mit # auskommentieren
'''


'''
Lektion 1: Listen & For-Schleifen (Wiederholung)
    - Konzept: Eine Liste ist wie ein Einkaufszettel. Die Schleife geht Zeile für Zeile durch.
    - Wichtig für die Klausur: Du musst durch Ordner iterieren.
'''


# Beispiel
def lektion1():
    kategorien = ["0", "1", "2", "3"] # Das sind Ordnernamen
    for kat in kategorien:
        print("Ich prüfe Ordner:", kat)

#lektion1()


'''
Lektion 2: Das os Modul & Pfade bauen
    - Konzept: Der Computer ist dumm. Er weiß nicht, dass “bild.jpg” im Ordner “data” liegt. Wir müssen den Weg bauen.
    - Funktion: os.path.join(ordner, datei) ist sicherer als ordner + "/" + datei (funktioniert auf Windows & Mac gleich).
'''


def lektion2():

    hauptordner = "data"
    unterordner = "7"
    datei = "schuh.png"

    pfad = "data/7/schuh.png"                               # FALSCH (oft Punktabzug in Klausuren wegen Plattformunabhängigkeit):

    # RICHTIG:
    pfad = os.path.join(hauptordner, unterordner, datei)    # os import am Anfang der Datei!
    print(pfad)                                             # Ausgabe: data/7/schuh.png (oder data\7\schuh.png auf Windows)


#lektion2()                                                


'''
PHASE 2
    Die Logik (Labels & Verschachtelung)

    Das ist der schwierigste Teil für Anfänger: Zwei Schleifen ineinander.
'''

'''
Lektion 3: Verschachtelte Schleifen (Nested Loops)
    - Konzept:  Stell dir vor, du hast mehrere Schubladen (Ordner), und in jeder Schublade sind Socken (Dateien). 
                Du musst jede Schublade öffnen und dann jede Socke einzeln anfassen.
    - Struktur:
        1.	Außen: Gehe durch alle Ordner (Kategorien 0-9).
        2.	Innen: Gehe durch alle Bilder in diesem einen Ordner.
'''

def lektion3():
    kategorien = ["0", "1"] # Nur zwei zum Testen
    for kat in kategorien:
        print(f"--- Öffne Ordner {kat} ---")
        # Simulation von Dateien
        dateien = ["bild_a.png", "bild_b.png"] 
        for d in dateien:
            print(f"  Verarbeite {d} in Ordner {kat}")

#lektion3()

'''
Lektion 4: If/Else Logik für Labels (Das “Schuh”-Problem)
    •	Aufgabe: Die Klausur verlangt eine binäre Klassifikation (0 oder 1).
    •	Logik: Wir brauchen eine Liste von “guten” Kategorien. Wenn der Ordnername in der Liste ist -> 0, sonst -> 1.
'''
def lektion4():
    kategorie = "7" # Das ist ein Sneaker
    schuhe = ["5", "7", "9"] # Sandale, Sneaker, Stiefel

    # Kurzschreibweise (Ternary Operator) - sehr beliebt in Klausuren!
    label = 0 if kategorie in schuhe else 1

    print(f"Kategorie {kategorie} bekommt Label {label}")

#lektion4()

