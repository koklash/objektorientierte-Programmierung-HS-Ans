
'''
Übungsaufgabe Teil 2: finale Übungsaufgabe (Vor der Klausuraufgabe)
    Bevor sie an die eigentliche Klausuraufgabe geht, lass sie diesen “Lückentext” ausfüllen. Das ist weniger einschüchternd als
    ein leeres Blatt.
    
    Aufgabe: Fülle die Lücken ___ aus.
'''


import os
import cv2
import numpy as np

def uebung_laden_mit_feedback():
    pfad_zu_daten = "data"
    alle_bilder = [] 
    alle_labels = [] 
    
    print(f"🚀 START: Suche nach Daten im Ordner '{pfad_zu_daten}'...")
    
    # 1. Liste alle Ordner auf
    if not os.path.exists(pfad_zu_daten):
        print(f"❌ FEHLER: Der Ordner '{pfad_zu_daten}' existiert nicht!")
        return [], []
        
    kategorien = os.listdir(pfad_zu_daten)
    print(f"ℹ️  Gefundene Ordner (Kategorien): {kategorien}")
    
    for kat in kategorien:
        print(f"\n📂 Öffne Ordner: '{kat}'")
        
        # 2. Baue Pfad zum aktuellen Unterordner
        aktueller_ordner_pfad = os.path.join(pfad_zu_daten, kat)
        
        # 3. Bestimme Label
        ist_schuh_liste = ['5', '7', '9']
        label = 0 if kat in ist_schuh_liste else 1
        
        # FEEDBACK ZUR ENTSCHEIDUNG
        text_entscheidung = "SCHUH (Label 0)" if label == 0 else "KEIN SCHUH (Label 1)"
        print(f"   ➡ Analyse: Kategorie '{kat}' ist in {ist_schuh_liste}? -> {text_entscheidung}")
        
        # 4. Liste alle Bilder
        bild_namen = os.listdir(aktueller_ordner_pfad)
        print(f"   Found {len(bild_namen)} Bilder in diesem Ordner.")
        
        for bild_name in bild_namen:
            # 5. Voller Pfad
            voller_pfad = os.path.join(aktueller_ordner_pfad, bild_name)
            
            # 6. Lade Bild (Hier als Graustufen simuliert für die Klausur)
            bild = cv2.imread(voller_pfad, 0) 
            
            # 7. Speichere & Feedback
            if bild is not None:
                alle_bilder.append(bild)
                alle_labels.append(label)
                # Kleines Feedback pro Bild (Vorsicht bei 10.000 Bildern, aber gut zum Üben)
                # print(f"      ✅ Bild '{bild_name}' geladen.") 
            else:
                print(f"      ⚠️ WARNUNG: Konnte '{bild_name}' nicht laden (beschädigt oder kein Bild).")
    
    print("\n🏁 FERTIG: Alle Ordner verarbeitet.")
    return alle_bilder, alle_labels

# --- TESTEN ---
# Damit das hier läuft, muss der Ordner "data" existieren. 
# Falls er nicht existiert, fangen wir das oben sauber ab.
X, y = uebung_laden_mit_feedback()

# ZUSAMMENFASSUNG
print("\n--- ZUSAMMENFASSUNG ---")
print(f"Gesamtanzahl geladener Bilder: {len(X)}")
if len(X) > 0:
    print(f"Beispiel - Erstes Label ist: {y[0]}")
    print(f"Beispiel - Erstes Bild Shape: {X[0].shape}")
