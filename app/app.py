from flask import Flask, request, render_template, jsonify
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


# Web form prediction
@app.route("/predict", methods=["POST"])
def predict():

    try:
        cgpa = float(request.form["cgpa"])
        iq = float(request.form["iq"])

        prediction, probability = predict_placement(cgpa, iq)

        result = "Placement Likely" if prediction == 1 else "Placement Unlikely"

        return render_template(
            "index.html",
            prediction=result,
            probability=round(probability * 100, 2)
        )

    except ValueError as e:

        return render_template(
            "index.html",
            prediction=str(e),
            probability=None
        )


# JSON API prediction
@app.route("/api/predict", methods=["POST"])
def api_predict():

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        cgpa = float(data.get("cgpa"))
        iq = float(data.get("iq"))

        prediction, probability = predict_placement(cgpa, iq)

        result = "Placement Likely" if prediction == 1 else "Placement Unlikely"

        return jsonify({
            "prediction": result,
            "probability": round(probability * 100, 2)
        })

    except ValueError as e:

        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)