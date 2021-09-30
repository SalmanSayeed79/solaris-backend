import json
from plan import (
    get_api, 
    getOptimumTiltAngle, 
    getOptimumPowerPerSqMeter, 
    getRegularPowerPerSqMeter, 
    getPercentProfit
)
import requests
from flask import Flask, request

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

@app.route('/api/temporal/daily/optimum')
def daily():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    data = get_api(longitude, latitude)
    api = {
        "optimum_tilt_angle": getOptimumTiltAngle(data),
        "optimum_power_per_sqmeter": getOptimumPowerPerSqMeter(data),
        "regular_power_per_sqmeter": getRegularPowerPerSqMeter(data),
        "profit_percentage": getPercentProfit(data)
    }
    return api