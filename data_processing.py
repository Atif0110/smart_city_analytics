# data_processing.py
import pandas as pd
from datetime import datetime, timedelta
import pytz

def process_traffic_data(traffic_json):
    if "error" in traffic_json:
        return None, None, {}, traffic_json["error"]

    try:
        flow_segment = traffic_json.get("flowSegmentData", {})
        current_speed = flow_segment.get("currentSpeed")
        free_flow = flow_segment.get("freeFlowSpeed")
        if current_speed is None:
            return None, None, {}, "Current speed data missing."

        # Last 1 hour data (12 points, 5-min intervals)
        ist = pytz.timezone("Asia/Kolkata")
        now_ist = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(ist)
        times = [now_ist - timedelta(minutes=5 * i) for i in range(12)][::-1]
        speeds = [max(0, current_speed * (0.8 + 0.04 * i)) for i in range(12)]
        df = pd.DataFrame({"time": times, "speed_kmph": speeds})

        # Predicted next 30 mins (6 points, 5-min intervals)
        future_times = [now_ist + timedelta(minutes=5 * i) for i in range(1, 7)]
        future_speeds = [max(0, current_speed * (0.9 - 0.02 * i)) for i in range(6)]
        df_future = pd.DataFrame({"time": future_times, "speed_kmph": future_speeds})

        return df, df_future, flow_segment, None
    except Exception as e:
        return None, None, {}, str(e)

def process_weather_data(weather_json):
    if "error" in weather_json:
        return None, weather_json["error"]
    try:
        main = weather_json.get("main", {})
        temp = main.get("temp")
        humidity = main.get("humidity")
        desc = weather_json.get("weather", [{}])[0].get("description", "N/A")
        if temp is None or humidity is None:
            return None, "Incomplete weather data."
        return {"temperature": temp, "humidity": humidity, "description": desc}, None
    except Exception as e:
        return None, str(e)

def process_pollution_data(pollution_json):
    if "error" in pollution_json:
        return None, pollution_json["error"]
    try:
        pm25 = pollution_json.get("pm25")
        if pm25 is None:
            return None, "PM2.5 data missing."
        return {"pm25": pm25}, None
    except Exception as e:
        return None, str(e)
