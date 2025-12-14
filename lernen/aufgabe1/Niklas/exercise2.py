'''
Lektion 3

    Jetzt schauen wir uns an, wie man einen vollständigen Dateipfad erstellt. 

    Bsp:
        import os

        ordner = "data/7"
        dateiname = "sneaker_01.png"

        vollständiger_pfad = os.path.join(ordner, dateiname)        # kombiniert Ordnername und Dateinam

        print(vollständiger_pfad)                                   # Ausgabe: "data/7/sneaker_01.png"

        
Lektion 4
    
    Mit OpenCV (cv2) können wir Bilder laden. Das geladene Bild ist automatisch ein NumPy-Array.
    !!! os.listdir("ordner") speichert nur die dateinamen in einem Array, nicht die Datein selbst!!!

    Bsp:
        import cv2

        bild = cv2.imread("data/7/image_009.png")       # !ACHTUNG! csv.imread benötigt den GANZEN Pfad!!!
        print(type(bild))                               # Ausgabe: <class 'numpy.ndarray'>
        print(bild.shape)                               # Ausgabe: z.B.: (28, 28) für 28x28 Pixel
    
        
    Was passiert beim “Laden” mittels cv2.imread()?
        Vorher:
            -	Die Datei image_009.png liegt auf deiner Festplatte
            -	Python kann damit noch nichts machen
        Nachher:
            -	Das Bild wird in ein NumPy-Array umgewandelt 
            -	Die Pixel werden als Zahlen gespeichert (z.B. 28x28 = 784 Zahlen für Fashion-MNIST)
            -	Jetzt kannst du mit dem Bild arbeiten (anzeigen, verarbeiten, etc.) 

    Vorteile eines NumPy-Array zu einem gewöhnlichen Array sind NumPy:
            - Schneller (Vektorisierung in C).
            - Speichereffizienter (homogene Daten, geringer Overhead).
            - Für Matrix-Operationen und wissenschaftliche Funktionen optimiert.
            - Umfassende Bibliothek für mathematische und wissenschaftliche Operationen


Lektion 5
    Leere Listen erstellen und Elemente hinzufügen mit .append()

    Bsp:
        meinArray = []              # Leeres Array initialisieren

        meinArray.append(123)       # 123 an das Array anhängen
        meinArray.append(543)       # 543 an das Array anhängen

        print(meinArray)


Mini-Aufgabe 2
Kombiniere alle bisherigen Lektionen:
Schreibe Code, der:
	1. os und cv2 importiert
    2. alle BILDER aus "data/7" im array x speichert
    3. Den Dateinamen + die Form(shape) der Datei ausgibt
    4. Am Ende die Länge von x ausgibt: print(len(x))
        
'''

import os, cv2

x = []
y = []

pathName = "data/7"
files = os.listdir(pathName)
for file in files:
    loadedFile = cv2.imread(os.path.join(pathName, file))
    print (file)
    print (loadedFile.shape)
    x.append(loadedFile)
    y.append(file)
print(len(x))


'''
    Herzlichen Glückwunsch, du bist bereit für die erste Aufgabe der Klausur 
'''