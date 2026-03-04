import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "../models/model.pkl")
scaler_path = os.path.join(BASE_DIR, "../models/scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


def predict_placement(cgpa, iq):

    # ---------- Input Validation ----------
    
    if not isinstance(cgpa, (int, float)):
        raise ValueError("CGPA must be a number")

    if not isinstance(iq, (int, float)):
        raise ValueError("IQ must be a number")

    if cgpa < 0 or cgpa > 10:
        raise ValueError("CGPA must be between 0 and 10")

    if iq < 70 or iq > 160:
        raise ValueError("IQ must be between 70 and 160")

    # ---------- Prediction ----------

    features = np.array([[cgpa, iq]])
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]

    return prediction, probability