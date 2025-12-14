import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load data
# ---------

#from aufgabe_1 import load_data
#X, y = load_data()
#y = np.array(y)
#from aufgabe_2 import calculate_features
#features = calculate_features(X)
#X = features  # Ab diesem Schritt der Pipeline sind die Features unsere Input-Daten X

# Backup for data:
import pickle
def load_data_from_pickle(file_path="data.pkl"):
    with open(file_path, "rb") as f:
        data = pickle.load(f)
        X = data['X']
        y = data['y']
    return X, y
_, y = load_data_from_pickle()
def load_features_from_pickle(file_path="features.pkl"):
    with open(file_path, "rb") as f:
        data = pickle.load(f)
        features = data['features']
    return features
X = load_features_from_pickle() # Ab diesem Schritt der Pipeline sind die Features unsere Input-Daten X

# Prepare the data
# ----------------

# Split the data into train and test sets:
X_train, X_test, y_train, y_test = #TODO

# Make the model
# --------------

# Train a k-nearest neighbors classifier
model = #TODO

# Evaluate the model
# ------------------

# Predict on the test data
accuracy = #TODO
print(f"Test Accuracy: {accuracy:.2f}")