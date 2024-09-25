from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Fetch data from the Open-Meteo API
def get_weather_data(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,dew_point_2m,apparent_temperature,precipitation_probability,rain,weather_code,surface_pressure,cloud_cover_low,cloud_cover_mid,cloud_cover_high,visibility,wind_speed_10m,wind_speed_80m,wind_speed_180m,wind_direction_80m,wind_direction_120m,wind_direction_180m,wind_gusts_10m,soil_temperature_0cm,soil_temperature_6cm,soil_temperature_54cm,soil_moisture_0_to_1cm,soil_moisture_1_to_3cm,soil_moisture_27_to_81cm",
        "timezone": "auto",
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extract only the first hour's data from the hourly forecast
    weather_data = {
        "location": f"Latitude: {latitude}, Longitude: {longitude}",
        "temperature_2m": data["hourly"]["temperature_2m"][0],
        "dew_point_2m": data["hourly"]["dew_point_2m"][0],
        "apparent_temperature": data["hourly"]["apparent_temperature"][0],
        "precipitation_probability": data["hourly"]["precipitation_probability"][0],
        "rain": data["hourly"]["rain"][0],
        "weather_code": data["hourly"]["weather_code"][0],
        "surface_pressure": data["hourly"]["surface_pressure"][0],
        "cloud_cover_low": data["hourly"]["cloud_cover_low"][0],
        "cloud_cover_mid": data["hourly"]["cloud_cover_mid"][0],
        "cloud_cover_high": data["hourly"]["cloud_cover_high"][0],
        "visibility": data["hourly"]["visibility"][0],
        "wind_speed_10m": data["hourly"]["wind_speed_10m"][0],
        "wind_speed_80m": data["hourly"]["wind_speed_80m"][0],
        "wind_speed_180m": data["hourly"]["wind_speed_180m"][0],
        "wind_direction_80m": data["hourly"]["wind_direction_80m"][0],
        "wind_direction_120m": data["hourly"]["wind_direction_120m"][0],
        "wind_direction_180m": data["hourly"]["wind_direction_180m"][0],
        "wind_gusts_10m": data["hourly"]["wind_gusts_10m"][0],
        "soil_temperature_0cm": data["hourly"]["soil_temperature_0cm"][0],
        "soil_temperature_6cm": data["hourly"]["soil_temperature_6cm"][0],
        "soil_temperature_54cm": data["hourly"]["soil_temperature_54cm"][0],
        "soil_moisture_0_to_1cm": data["hourly"]["soil_moisture_0_to_1cm"][0],
        "soil_moisture_1_to_3cm": data["hourly"]["soil_moisture_1_to_3cm"][0],
        "soil_moisture_27_to_81cm": data["hourly"]["soil_moisture_27_to_81cm"][0],
    }

    return weather_data

@app.route('/weather', methods=['GET'])
def weather():
    latitude = request.args.get('latitude', default=52.52, type=float)
    longitude = request.args.get('longitude', default=13.41, type=float)
    weather_data = get_weather_data(latitude, longitude)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
