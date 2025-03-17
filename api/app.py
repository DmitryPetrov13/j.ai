from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with your OpenRouter API key
API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    data = {
        "model": "google/gemma-3-1b-it:free",
        "messages": [{"role": "user", "content": user_message}]
    }
    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data from API"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
