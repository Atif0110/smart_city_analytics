import requests
from config import OPENWEATHER_KEY, TOMTOM_KEY, WAQI_KEY

session = requests.Session()

def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"
        response = session.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_traffic(city):
    try:
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={OPENWEATHER_KEY}"
        geo_resp = session.get(geo_url, timeout=5)
        geo_data = geo_resp.json()

        if not geo_data:
            return {"error": "City not found"}

        lat, lon = geo_data[0]['lat'], geo_data[0]['lon']

        traffic_url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat},{lon}&unit=KMPH&key={TOMTOM_KEY}"
        traffic_resp = session.get(traffic_url, timeout=5)
        traffic_data = traffic_resp.json()

        traffic_data['lat'] = lat
        traffic_data['lon'] = lon
        return traffic_data

    except Exception as e:
        return {"error": str(e)}

def fetch_pollution(city):
    try:
        url = f"https://api.waqi.info/feed/{city}/?token={WAQI_KEY}"
        response = session.get(url, timeout=5)
        data = response.json()

        if data.get("status") != "ok":
            return {"error": "Pollution data unavailable"}

        pm25 = data["data"]["iaqi"]["pm25"]["v"]
        return {"pm25": pm25}

    except Exception as e:
        return {"error": str(e)}
