import joblib
import numpy as np
import os

# Resolve model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/model.pkl")
scaler_path = os.path.join(BASE_DIR, "../models/scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


def predict_placement(cgpa, iq):

    features = np.array([[cgpa, iq]])

    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    probability = model.predict_proba(features_scaled)[0][1]

    return prediction, probability