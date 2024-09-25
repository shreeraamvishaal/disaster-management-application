from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from flask_cors import CORS  # Import CORS
import re  # Import regular expressions for text processing

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
    formatted_response = format_response(response.text)
    return formatted_response

def format_response(text):
    # Split the text into lines
    lines = text.split('\n')

    # Format the response by removing URLs and adding clean bullet points and headings
    formatted_lines = []
    for line in lines:
        if "http" in line:
            continue  # Skip lines with URLs

        # Detect headings surrounded by '**' and replace with just bold effect (without <strong> tags)
        line = re.sub(r'\*\*(.*?)\*\*', r'\1', line)  # Remove Markdown-style asterisks
        line = re.sub(r'\*(.*?)\*', r'\1', line)  # Remove Markdown-style asterisks for bullets
        
        # Reformat bullet points with proper indentations
        if line.startswith("* "):
            line = "• " + line[2:]  # Replace '*' with a bullet

        formatted_lines.append(line.strip())

    # Join the cleaned lines back into a formatted string with line breaks
    formatted_response = '\n'.join(formatted_lines)

    return formatted_response.strip()

if __name__ == "__main__":
    app.run(debug=True)
