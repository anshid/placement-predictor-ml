from flask import Flask, request, render_template
import os
import sys

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.predict import predict_placement

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    cgpa = float(request.form["cgpa"])
    iq = float(request.form["iq"])

    try:
        prediction, probability = predict_placement(cgpa, iq)

        result = "Placement Likely" if prediction == 1 else "Placement Unlikely"

        probability = round(probability * 100, 2)

        return render_template(
            "index.html",
            prediction=result,
            probability=probability
        )

    except ValueError as e:

        return render_template(
            "index.html",
            prediction=str(e),
            probability=None
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)