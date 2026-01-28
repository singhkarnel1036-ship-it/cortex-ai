from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MASTER_PROMPT = """
You are Cortex, a smart, friendly, and reliable AI assistant.

You reply mainly in Hindi or Hinglish.
You talk like a helpful friend.
You explain things step by step.
If the user is confused, you simplify more.
"""

@app.route("/")
def home():
    return "Cortex AI is Live 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": MASTER_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    return jsonify({
        "reply": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
