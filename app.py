from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Load your API key from Replit Secrets
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistral-saba-24b",
            "messages": [
                {"role": "system", "content": "You are an AI tutor helping users learn Artificial Intelligence."},
                {"role": "user", "content": user_input}
            ]
        }
    )

    data = response.json()
    bot_reply = data['choices'][0]['message']['content']
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
