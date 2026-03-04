import requests

url = "http://192.168.0.105:5000/api/predict"

data = {
    "cgpa": 8.2,
    "iq": 120
}

try:
    response = requests.post(url, json=data)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

except Exception as e:
    print("Error:", e)