import cv2, os


def load_data():
    X = []
    y = []

    folder = "data"
    categories = os.listdir(folder)

    for category in categories:
        shoes = ['5', '7', '9']
        fullPathCategory = os.path.join(folder, category)
        productNames = os.listdir(fullPathCategory)

        # Bestimme das Label: Schuh = 0, nicht Schuh = 1
        productType = 0 if category in shoes else 1

        # Bild als Graustufen laden (0 entspricht cv2.IMREAD_GRAYSCALE)
        for productName in productNames:
            fullPathProduct = os.path.join(fullPathCategory, productName)
            loadedFile = cv2.imread(fullPathProduct)
            X.append(loadedFile)
            y.append(productType)
    
    # Gib zwei separate Listen zurück, wie gefordert
    return X,y



def main():
    X, y = load_data()

    # Sanity Checks
    
    print(f"Anzahl geladener Bilder: {len(X)}")
    print(f"Erstes Label: {"Schuh" if y[0]== 0 else "nicht-Schuh"}")

    # Optional: Überprüfen der Shape eines Bildes (sollte 28x28 sein)
    if len(X) > 0:
        print(f"Bild-Dimensionen: {X[0].shape}")



if __name__ == "__main__":
    main()