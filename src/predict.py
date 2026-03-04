import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def predict_placement(cgpa, iq):

    data = np.array([[cgpa, iq]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        return "Placement Likely"
    else:
        return "Placement Unlikely"