from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# הגדר את המפתח API
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Welcome to Flask AI App!"

@app.route("/ask", methods=["POST"])
def ask_ai():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    answer = response.choices[0].text.strip()
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

