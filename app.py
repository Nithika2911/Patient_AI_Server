from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return "Smart Patient AI Server Running"


@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        question = data["question"]

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        return jsonify({
            "answer": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500




if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )