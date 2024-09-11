from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the API key
genai.configure(api_key="AIzaSyBoMBFASXoHDgfhOtvIUq_3PXtYj6n2vNI")

# Route to serve the HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt', '')
    if prompt:
        response = chat_with_gemini(prompt)
        return jsonify({'response': response})
    return jsonify({'response': 'No prompt provided'})

def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    app.run(debug=True)
