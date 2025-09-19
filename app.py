# app.py
import streamlit as st
import time
import pandas as pd
from data_collection import fetch_weather, fetch_traffic, fetch_pollution
from data_processing import process_traffic_data, process_weather_data, process_pollution_data
from alerts import show_alert
from visualization import plot_traffic_map
from utils.helpers import format_time
from streamlit import cache_data

st.set_page_config(page_title="Smart City Pro Dashboard", layout="wide")
st.title("🚦 Smart City Pro Analytics Dashboard")

# ---------------------
# Caching API calls
# ---------------------
@cache_data(ttl=60)
def get_weather(city):
    return fetch_weather(city)

@cache_data(ttl=60)
def get_traffic(city):
    return fetch_traffic(city)

@cache_data(ttl=60)
def get_pollution(city):
    return fetch_pollution(city)

# ---------------------
# Input two cities
# ---------------------
city1 = st.sidebar.text_input("Enter First City:", "Pune")
city2 = st.sidebar.text_input("Enter Second City:", "Lucknow")
cities = [city1, city2]

# ---------------------
# Loop for both cities
# ---------------------
for idx, city in enumerate(cities):
    st.subheader(f"City {idx+1}: {city}")

    with st.spinner(f"Fetching data for {city}..."):
        weather_raw = get_weather(city)
        traffic_raw = get_traffic(city)
        pollution_raw = get_pollution(city)

        lat = traffic_raw.get("lat") if "error" not in traffic_raw else None
        lon = traffic_raw.get("lon") if "error" not in traffic_raw else None

        traffic_df, traffic_future_df, flow, traffic_err = process_traffic_data(traffic_raw)
        weather_data, weather_err = process_weather_data(weather_raw)
        pollution_data, pollution_err = process_pollution_data(pollution_raw)

    # ---------------------
    # Display Weather, Pollution, Traffic
    # ---------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Weather**")
        if weather_err:
            st.error(weather_err)
        else:
            st.write(f"Temperature: {weather_data['temperature']} °C")
            st.write(f"Humidity: {weather_data['humidity']}%")
            st.write(f"Description: {weather_data['description']}")
    with col2:
        st.markdown("**Pollution**")
        if pollution_err:
            st.error(pollution_err)
        else:
            st.write(f"PM2.5: {pollution_data['pm25']} µg/m³")
    with col3:
        st.markdown("**Traffic**")
        if traffic_err:
            st.error(traffic_err)
        else:
            st.write(f"Current Speed: {flow.get('currentSpeed', 'N/A')} km/h")
            st.write(f"Free Flow Speed: {flow.get('freeFlowSpeed', 'N/A')} km/h")
            st.write(f"Confidence: {flow.get('confidence', 'N/A')}")

    # ---------------------
    # Alerts
    # ---------------------
    show_alert(weather_data, pollution_data, flow)

    st.markdown("---")

    # ---------------------
    # Real-time Traffic Graph
    # ---------------------
    st.markdown("**Real-time Traffic Speed (Last 1 Hour)**")
    placeholder = st.empty()
    traffic_data_list = []

    for _ in range(6):  # 6 updates, every 10 seconds
        traffic_raw = get_traffic(city)
        traffic_df, _, flow, traffic_err = process_traffic_data(traffic_raw)
        if traffic_err:
            st.error(traffic_err)
            break
        traffic_data_list.append(traffic_df.iloc[-1])
        df_live = pd.DataFrame(traffic_data_list)
        df_live = format_time(df_live)
        placeholder.line_chart(df_live.set_index('time')['speed_kmph'])
        time.sleep(10)

    st.markdown("**Traffic Speed Prediction (Next 30 mins)**")
    if traffic_future_df is not None:
        df_future = format_time(traffic_future_df)
        st.line_chart(df_future.set_index('time')['speed_kmph'])

    st.markdown("**City Map with Traffic Heat**")
    if lat and lon:
        plot_traffic_map(lat, lon, flow)
    else:
        st.warning("Map cannot be displayed due to missing coordinates.")

    st.markdown("=====================================")
