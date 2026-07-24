import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase Connection
cred = credentials.Certificate(
    "vitalwatch-38574-firebase-adminsdk-fbsvc-d6c4fea460.json"
)

firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://vitalwatch-38574-default-rtdb.europe-west1.firebasedatabase.app/"
    }
)

print("✅ Firebase Connected Successfully")

# Read Patient Data
ref = db.reference("sensor/patient1/Patient")

data = ref.get()

heart_rate = data["HeartRate"]
spo2 = data["SpO2"]
temperature = data["Temperature"]
status = data["Status"]
patient_id = data["PatientID"]

print("\n========== PATIENT DATA ==========")

print(f"Patient ID  : {patient_id}")
print(f"Heart Rate  : {heart_rate}")
print(f"SpO2        : {spo2}")
print(f"Temperature : {temperature}")
print(f"Status      : {status}")

print("==================================")