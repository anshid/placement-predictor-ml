from flask import Flask, request, render_template
import os
import joblib
import numpy as np

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    cgpa = float(request.form["cgpa"])
    iq = float(request.form["iq"])

    data = np.array([[cgpa, iq]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    result = "Placement Likely" if prediction[0] == 1 else "Placement Unlikely"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)