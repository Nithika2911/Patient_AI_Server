import requests

url = "http://127.0.0.1:5000/ask"

data = {
    "question": "Patient has Heart Rate 110 BPM, SpO2 94%, Temperature 38.5°C. Analyze the condition."
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())