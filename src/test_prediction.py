from predict import predict_placement

prediction, probability = predict_placement(8.0, 120)

if prediction == 1:
    result = "Placement Likely"
else:
    result = "Placement Unlikely"

print(result)
print(f"Probability: {probability*100:.2f}%")

