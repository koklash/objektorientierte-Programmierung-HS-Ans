
'''
Übungsaufgabe Teil 2: finale Übungsaufgabe (Vor der Klausuraufgabe)
    Bevor sie an die eigentliche Klausuraufgabe geht, lass sie diesen “Lückentext” ausfüllen. Das ist weniger einschüchternd als
    ein leeres Blatt.
    
    Aufgabe: Fülle die Lücken ___ aus.
'''

import os
import cv2
import numpy as np

import os
import cv2
import numpy as np

# --- HILFS-CODE (NICHT ÄNDERN) ---
# Dieser Teil erstellt automatisch Ordner und Bilder, 
# damit du den Code sofort testen kannst.
def setup_test_umgebung():
    print("🛠️  Erstelle Test-Umgebung...")
    os.makedirs("data/7", exist_ok=True)   # Ein "Schuh"-Ordner (Sneaker)
    os.makedirs("data/0", exist_ok=True)   # Ein "Nicht-Schuh"-Ordner (T-Shirt)
    # Erstelle zwei schwarze Dummy-Bilder
    cv2.imwrite("data/7/sneaker_test.png", np.zeros((28,28), dtype=np.uint8))
    cv2.imwrite("data/0/tshirt_test.png", np.zeros((28,28), dtype=np.uint8))
    print("✅ Test-Daten bereit!\n")
# ---------------------------------


# === DEINE AUFGABE BEGINNT HIER ===

def load_data_uebung():
    pfad_zu_daten = "data"
    alle_bilder = [] # X
    alle_labels = [] # y
    
    print(f"🚀 START: Suche nach Daten in '{pfad_zu_daten}'...")
    
    # 1. Liste alle Kategorien (Ordner 0-9) auf
    kategorien = os.listdir(pfad_zu_daten)
    
    for kat in kategorien:
        print(f"\n📂 Bearbeite Ordner: '{kat}'")
        
        # 2. Baue Pfad zum aktuellen Unterordner
        aktueller_ordner_pfad = os.path.join(pfad_zu_daten, kat)
        
        # --- LÜCKE 1: LOGIK ---
        # Aufgabenstellung: 5, 7, 9 sind Schuhe (Label 0). Alles andere ist Label 1.
        schuh_klassen = ['5', '7', '9']
        
        # Fülle aus: Wenn 'kat' in 'schuh_klassen' ist, dann 0, sonst 1
        label = ___ if ___ in ___ else ___
        
        print(f"   ➡ Entscheidung: Kategorie {kat} bekommt Label {label}")
        
        
        # 3. Liste alle Bilder in diesem Ordner
        bild_namen = os.listdir(aktueller_ordner_pfad)
        
        for bild_name in bild_namen:
            # --- LÜCKE 2: PFAD BAUEN ---
            # Wir brauchen den kompletten Pfad zur Datei (Ordner + Dateiname)
            voller_pfad = os.path.join(___, ___)
            
            # --- LÜCKE 3: BILD LADEN ---
            # Lade das Bild. WICHTIG: Achte auf Graustufen (Parameter 0)!
            bild = cv2.imread(___, ___)
            
            # --- LÜCKE 4: LISTEN FÜLLEN ---
            if bild is not None:
                # Füge das Bild zur Liste 'alle_bilder' hinzu
                alle_bilder.append(___)
                # Füge das Label zur Liste 'alle_labels' hinzu
                alle_labels.append(___)
            else:
                print(f"      ⚠️ Fehler beim Laden von: {bild_name}")

    return alle_bilder, alle_labels


# === HAUPTPROGRAMM (MAIN) ===
if __name__ == "__main__":
    # 1. Test-Daten erzeugen
    setup_test_umgebung()
    
    try:
        # 2. Deine Funktion aufrufen
        X, y = load_data_uebung()
        
        # 3. Ergebnis prüfen (Sanity Checks)
        print("\n🏁 ABSCHLUSS-BERICHT:")
        print(f"   Anzahl geladener Bilder: {len(X)}")
        
        if len(X) > 0:
            print(f"   Erstes Bild Form: {X[0].shape} (Sollte 28, 28 sein)")
            print(f"   Labels gefunden: {np.unique(y)}")
            print("\n🎉 HERZLICHEN GLÜCKWUNSCH! Code läuft fehlerfrei.")
        else:
            print("\n❌ ACHTUNG: Es wurden keine Bilder geladen. Prüfe Lücke 2 und 3!")
            
    except Exception as e:
        print(f"\n❌ FEHLER IM CODE: {e}")
        print("   Tipp: Hast du alle '___' Unterstriche durch Code ersetzt?")
