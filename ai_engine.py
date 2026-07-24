import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API Key
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_patient(patient_data):

    prompt = f"""
You are an AI Clinical Decision Support Assistant.

You are assisting licensed doctors.

Analyze the following patient vital signs.

Patient ID : {patient_data['PatientID']}
Heart Rate : {patient_data['HeartRate']} BPM
SpO2 : {patient_data['SpO2']} %
Temperature : {patient_data['Temperature']} °C
Status : {patient_data['Status']}

Rules:
- Do NOT diagnose diseases with certainty.
- Do NOT prescribe medicines.
- Do NOT replace a doctor's judgement.

Provide:

1. Possible Clinical Condition
2. Clinical Reason
3. Recommended Clinical Assessment
4. Suggested Clinical Management
5. Risk Level

Keep the response under 150 words.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text