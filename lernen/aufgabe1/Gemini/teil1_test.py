'''
Übungsaufgabe Teil 1: (Trockenübung ohne Bilder)
        Schreibe eine verschachtelte Schleife, die durch Ordner “0” bis “9” geht. Wenn der Ordner 5, 7 oder 9 ist, drucke “Schuh”, sonst “Kein Schuh”.
'''

# Wir simulieren die Ordnernamen als Strings (weil os.listdir Strings zurückgibt)
kategorien = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Das sind die "Schuh"-Klassen aus der Aufgabe
schuh_klassen = ["5", "7", "9"]

# 1. Äußere Schleife: Gehe durch jeden Ordner
for kategorie in kategorien:
    
    # Simulation: Wir tun so, als wären in jedem Ordner 2 Dateien
    # (In der Klausur kommt das aus os.listdir)
    meine_dateien = ["bild_a.png", "bild_b.png"]
    
    # 2. Innere Schleife: Gehe durch jede Datei in diesem Ordner
    for datei in meine_dateien:
        
        # Die Entscheidung (Logik):
        if kategorie in schuh_klassen:
            print(f"Ordner {kategorie} ({datei}): Schuh")
        else:
            print(f"Ordner {kategorie} ({datei}): Kein Schuh")
            
    print("--- Nächster Ordner ---") # Nur zur Übersicht
