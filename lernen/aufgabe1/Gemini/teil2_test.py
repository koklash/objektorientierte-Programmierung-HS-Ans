
'''
Übungsaufgabe Teil 2: finale Übungsaufgabe (Vor der Klausuraufgabe)
    Bevor sie an die eigentliche Klausuraufgabe geht, lass sie diesen “Lückentext” ausfüllen. Das ist weniger einschüchternd als
    ein leeres Blatt.
    
    Aufgabe: Fülle die Lücken ___ aus.
'''

import os
import cv2
import numpy as np

def uebung_laden():
    pfad_zu_daten = "data"
    alle_bilder = [] # X
    alle_labels = [] # y
    
    # 1. Liste alle Ordner auf
    kategorien = os.listdir(pfad_zu_daten)
    
    for kat in kategorien:
        # 2. Baue Pfad zum aktuellen Unterordner
        aktueller_ordner_pfad = os.path.join(pfad_zu_daten, kat)
        
        # 3. Bestimme Label: Ist es ein Schuh (5, 7, 9)?
        # Wenn ja label=0, sonst label=1
        ist_schuh_liste = ['5', '7', '9']
        label = ___ if ___ in ___ else ___
        
        # 4. Liste alle Bilder in diesem Unterordner
        bild_namen = os.listdir(aktueller_ordner_pfad)
        
        for bild_name in bild_namen:
            # 5. Baue vollen Pfad zum Bild
            voller_pfad = os.path.join(___, ___)
            
            # 6. Lade Bild
            bild = cv2.imread(voller_pfad)
            
            # 7. Speichere in Listen
            if bild is not None: # Kleiner Sicherheitscheck
                alle_bilder.append(___)
                alle_labels.append(___)
                
    return alle_bilder, alle_labels

# Testen
X, y = uebung_laden()

# Sanity Checks
print(f"Anzahl Bilder: {len(X)}")
if len(X) > 0:
    print(f"Form des ersten Bildes: {X[0].shape}")
    print(f"Label des ersten Bildes: {y[0]}")
