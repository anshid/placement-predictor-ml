import matplotlib.pyplot as plt
import pandas as pd
import joblib
from mlxtend.plotting import plot_decision_regions

# Load dataset
df = pd.read_csv("data/cleaned_placement_data.csv")

X = df[["cgpa", "iq"]].values
y = df["placement"].values

# Load scaler and model
scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/model.pkl")

# Scale features
X_scaled = scaler.transform(X)

plt.figure(figsize=(8,6))

plot_decision_regions(X_scaled, y, clf=model, legend=2)

plt.xlabel("Scaled CGPA")
plt.ylabel("Scaled IQ")
plt.title("Decision Boundary for Placement Prediction")

plt.savefig("decision_boundary.png")

plt.show()