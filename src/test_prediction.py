from predict import predict_placement

try:
    prediction, probability = predict_placement(8, 120)

    if prediction == 1:
        result = "Placement Likely"
    else:
        result = "Placement Unlikely"

    print(result)
    print(f"Probability: {probability*100:.2f}%")

except ValueError as e:
    print("Error:", e)