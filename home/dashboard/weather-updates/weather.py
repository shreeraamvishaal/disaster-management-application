from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

API_KEY = '30171c531fe95eae5a7d514693ea4da0'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location parameter is required'}), 400

    response = requests.get(BASE_URL, params={
        'q': location,
        'appid': API_KEY,
        'units': 'metric'
    })

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': f"Failed to fetch weather data. Status code: {response.status_code}"}), response.status_code

@app.route('/forecast', methods=['GET'])
def get_forecast():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location parameter is required'}), 400

    response = requests.get(FORECAST_URL, params={
        'q': location,
        'appid': API_KEY,
        'units': 'metric'
    })

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': f"Failed to fetch forecast data. Status code: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5001)
