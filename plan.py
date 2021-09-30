#AKA elevation angle
import json
import requests
from math import sin, cos, exp
from datetime import datetime
def get_api(longitude, latitude):
    now = datetime.now()
    timeline = f"{now.year-1}{now.month}{now.day}"
    parameters = {
        'parameters': "ALLSKY_SFC_SW_DWN,CLRSKY_SFC_SW_DWN,ALLSKY_KT",
        'community': "RE",
        'longitude': longitude,
        'latitude': latitude,
        'start': timeline,
        'end': timeline,
        'format': "JSON"
    }
    data = requests.get("https://power.larc.nasa.gov/api/temporal/daily/point", params=parameters)
    return data.json()

def get_location(data):
    longitude = data['geometry']['coordinates'][0]
    latitude = data['geometry']['coordinates'][1]
    return (latitude, longitude)

def getSolarZenithAngle(data, noOfDay = datetime.now().timetuple().tm_yday):
    latitude, longitude = get_location(data)
    declinationAngle =  23.45*sin(360*( 284 + noOfDay) / 365 )
    return 90 - latitude + declinationAngle

#if this value is < 0.3 we say it's overcast
def getModifiedClearnessIndex(clearnessIndex, solarZenithAngle):
    return solarZenithAngle / (.1 + 1.031*exp(-1.4/(.9 + 9.4*cos(solarZenithAngle))))
    
def getOptimumPowerPerSqMeter(data):
    clearnessIndex = list(data["properties"]["parameter"]["ALLSKY_KT"].values())[0]
    solarZenithAngle = getSolarZenithAngle(data)
    if getModifiedClearnessIndex(clearnessIndex, solarZenithAngle) < 0.3:
        return getDiffuseIrradiation(data)
    else:
        return getGlobalIrradiation(data) / sin(solarZenithAngle)
        
def getOptimumTiltAngle(data):
    clearnessIndex = list(data["properties"]["parameter"]["ALLSKY_KT"].values())[0]
    solarZenithAngle = getSolarZenithAngle(data)
    
    if getModifiedClearnessIndex(clearnessIndex, solarZenithAngle) < 0.3:
        return 0
    else: 
        return 90 - solarZenithAngle
        
def getDiffuseIrradiation(data):
    allsky = list(data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].values())[0]
    clrsky = list(data["properties"]["parameter"]["CLRSKY_SFC_SW_DWN"].values())[0]
    return float(clrsky) - float(allsky)

    
def getGlobalIrradiation(data):
    allsky = list(data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].values())[0]
    return allsky
   
def getRegularPowerPerSqMeter(data):
    latitude, longitude = get_location(data)
    solarZenithAngle = getSolarZenithAngle(data)
    return abs((getGlobalIrradiation(data) - getDiffuseIrradiation(data)) * sin(latitude + solarZenithAngle) / sin(solarZenithAngle))
    
def getPercentProfit(data):
    return (getOptimumPowerPerSqMeter(data) - abs(getRegularPowerPerSqMeter(data))) * 100 / abs(getRegularPowerPerSqMeter(data))