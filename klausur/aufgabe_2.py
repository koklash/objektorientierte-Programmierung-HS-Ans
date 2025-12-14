import cv2
import numpy as np
from typing import List


def calculate_features(X: List[np.ndarray]) -> np.ndarray:
    """
    Calculate features for each image in X.
    
    Features are:
    1. Average pixel brightness of the whole image
    2. Aspect ratio of the foreground region (background is assumed to be black)
    
    Parameters:
    X (list of np.ndarray): List of images of shape (height, width, 3)
    
    Returns:
    np.ndarray: Array of shape (n_samples, 2) containing the features
    """

    features = np.empty((len(X), 2))  # Platzhalter, solange Sie noch keinen Code geschrieben haben
    #TODO  Ihr Code hier

    return features


if __name__ == "__main__":
    # Load data
    # ---------

    #from aufgabe_1 import load_data
    #X, _ = load_data()

    # Backup for data:
    import pickle
    def load_data_from_pickle(file_path="data.pkl"):
        with open(file_path, "rb") as f:
            data = pickle.load(f)
            X = data['X']
            y = data['y']
        return X, y
    X, y = load_data_from_pickle()

    # Calculate features
    # ------------------

    features = calculate_features(X)

    exit()  # Wenn Sie den Plot sehen wollen, entfernen Sie den exit()-Befehl, der das Programm beendet.

    # Plot feature space
    # ------------------
    class_idx = np.array(y)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(features[class_idx==1, 0], features[class_idx==1, 1], 'ob', label="Schuh", alpha=0.5)
    plt.plot(features[class_idx==0, 0], features[class_idx==0, 1], 'sr', label="nicht Schuh", alpha=0.5)
    plt.legend()
    plt.title("Feature Space of Images")
    plt.xlabel("Average Pixel Brightness")
    plt.ylabel("Aspect Ratio of Foreground Region")
    plt.grid()
    plt.show()

    # Die Figure muss geschlossen werden, damit das Programm fortfährt (bzw. hier: endet)