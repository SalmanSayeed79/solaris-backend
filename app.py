from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/api/temporal/monthly/point')
def monthly():
    parameters = request.args.get('parameters')
    community = request.args.get('community')
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    format = request.args.get('format')
    start= request.args.get('start')
    end = request.args.get('end')

    query = {
        'parameters': parameters,
        'community': community,
        'longitude': longitude,
        'latitude': latitude,
        'format': format,
        'start': start,
        'end': end
    }
    response = requests.get("https://power.larc.nasa.gov/api/temporal/monthly/point", params=query)
    return response.json()