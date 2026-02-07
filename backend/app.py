from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import json
import random

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load(r"C:\yash\coding\python\college\mental health awarness chatbot\backend\model.joblib")
vectorizer = joblib.load(r"C:\yash\coding\python\college\mental health awarness chatbot\backend\vectorizer.joblib")

# Load intents (same dataset used for training)
with open(r'C:\yash\coding\python\college\mental health awarness chatbot\dataset.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

# Helper to find responses
def get_responses(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return intent["responses"]
    return []

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get("message", "")

    if message.strip() == "":
        return jsonify({"error": "Empty message"}), 400

    # Vectorize
    X_vec = vectorizer.transform([message])

    # Predict
    tag = model.predict(X_vec)[0]

    # Pick a random response
    responses = get_responses(tag)
    bot_reply = random.choice(responses) if responses else "Sorry, I didn't understand."

    return jsonify({
        "tag": tag,
        "response": bot_reply
    })

if __name__ == "__main__":
    app.run(debug=True)
