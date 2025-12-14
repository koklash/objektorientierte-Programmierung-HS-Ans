import cv2
import os
import numpy as np

# --- HILFSFUNKTION: SETUP (Ignorieren für die Klausur) ---
def setup_test_umgebung():
    """Erstellt einen Dummy-Ordner und ein Testbild, damit der Code läuft."""
    os.makedirs("test_daten", exist_ok=True)
    # Ein 28x28 Bild erstellen (zufälliges Rauschen)
    dummy = np.random.randint(0, 255, (28, 28), dtype=np.uint8)
    cv2.imwrite("test_daten/beispiel.png", dummy)
    print("[Setup] Testumgebung erstellt.\n")


'''
Phase 3
    Daten laden & Sanity Checks

    Jetzt kommt OpenCV und das Zusammenfügen.
'''

'''
Lektion 5 :Bilder laden mit OpenCV
    - Wichtig: cv2.imread braucht den vollen Pfad (siehe Lektion 2).
	- Stolperfalle: Wenn der Pfad falsch ist, gibt cv2 keinen Fehler zurück, sondern None. Das führt erst später zum Absturz.
	- Listen füllen: X sammelt die Bilder (Daten), y sammelt die Labels (Antworten). Beide Listen müssen am Ende exakt gleich 
      lang sein (Index 0 in X gehört zu Index 0 in y).
'''

# ==========================================
# LEKTION 5: Funktion zum Laden eines Bildes
# ==========================================
def lade_bild(dateipfad, als_graustufen=True):
    """
    Lädt ein Bild von einem Pfad.
    Parameter:
        dateipfad (str): Der volle Pfad zur Datei
        als_graustufen (bool): Wenn True, wird das Bild s/w geladen
    Rückgabe:
        Das Bild als numpy-Array oder None, wenn es nicht gefunden wurde.
    """
    
    # Entscheidung: Welcher Modus?
    # 0 = cv2.IMREAD_GRAYSCALE, 1 = cv2.IMREAD_COLOR
    flag = 0 if als_graustufen else 1
    
    # Laden
    bild = cv2.imread(dateipfad, flag)
    
    # Kurzer Check direkt beim Laden (optional, aber hilfreich)
    if bild is None:
        print(f"[Fehler] Konnte Bild nicht finden unter: {dateipfad}")
        return None
    
    print(f"[Info] Bild geladen. Shape: {bild.shape}")
    return bild

'''
Lektion 6: Sanity Checks (Warum machen wir das?)
	- Konzept: Vertrauen ist gut, Kontrolle ist besser. In der Klausur zeigt das, dass du professionell arbeitest.
	- Die 3 heiligen Checks:
	1.	len(X) > 0 : Haben wir überhaupt was geladen? (Oft ist der Pfad falsch).
	2.	len(X) == len(y) : Haben wir zu jedem Bild ein Label? (Muss immer wahr sein).
	3.	X.shape : Hat das Bild die richtige Form (z.B. 28x28)?
	4.	np.unique(y) : Haben wir wirklich nur 0en und 1en geladen? (Profi-Tipp).
'''

# ==========================================
# LEKTION 6: Funktion für Sanity Checks
# ==========================================
def mache_sanity_checks(X, y):
    """
    Prüft, ob die Listen X (Daten) und y (Labels) valide sind.
    """
    print("\n--- Starte Sanity Checks ---")
    
    # Check 1: Leere Listen?
    if len(X) == 0:
        print("!! FEHLER: Die Liste X ist leer. Wurden Daten geladen?")
        return False # Wir brechen hier ab, weil weitere Checks crashen würden

    # Check 2: Länge gleich?
    if len(X) != len(y):
        print(f"!! FEHLER: Listenlänge ungleich! X={len(X)}, y={len(y)}")
        return False

    # Check 3: Bildformate (Shape)
    # Wir prüfen stichprobenartig das erste Bild
    erstes_bild = X[0]
    erwartete_shape = (28, 28)
    
    if erstes_bild.shape != erwartete_shape:
        print(f"!! WARNUNG: Bild hat ungewöhnliche Form: {erstes_bild.shape}")
        # Hier kein 'False', vielleicht ist das ja gewollt, aber gut zu wissen.
    
    # Check 4: Labels prüfen
    unique_labels = np.unique(y)
    print(f"[OK] Checks bestanden. Gefundene Klassen: {unique_labels}")
    print(f"[OK] Anzahl geladener Beispiele: {len(X)}")
    return True


# ==========================================
# MAIN: Hier rufen wir alles auf
# ==========================================
def main():
    # 1. Erstmal die Umgebung vorbereiten
    setup_test_umgebung()

    # --- Testen von Lektion 5 (Laden) ---
    pfad_richtig = os.path.join("test_daten", "beispiel.png")
    pfad_falsch = os.path.join("test_daten", "gibt_es_nicht.png")

    print("1. Versuche Bild zu laden:")
    mein_bild = lade_bild(pfad_richtig, als_graustufen=True)
    
    print("2. Versuche kaputtes Bild zu laden:")
    kein_bild = lade_bild(pfad_falsch) # Sollte Fehler drucken


    # --- Testen von Lektion 6 (Checks) ---
    # Wir simulieren Listen, wie sie nach der 'load_data' Funktion aussehen würden
    
    # Fall A: Alles korrekt
    print("\nTestfall A (Korrekte Daten):")
    X_gut = [mein_bild, mein_bild, mein_bild] # 3 Bilder
    y_gut = [0, 1, 0]                         # 3 Labels
    mache_sanity_checks(X_gut, y_gut)

    # Fall B: Fehlerhafte Daten
    print("\nTestfall B (Kaputte Daten):")
    X_schlecht = [mein_bild, mein_bild]       # Nur 2 Bilder
    y_schlecht = [0, 1, 0]                    # Aber 3 Labels
    mache_sanity_checks(X_schlecht, y_schlecht)


if __name__ == "__main__":
    main()
