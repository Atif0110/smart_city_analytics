import streamlit as st
import pandas as pd

from data_collection import fetch_weather, fetch_traffic, fetch_pollution
from data_processing import (
    process_traffic_data,
    process_weather_data,
    process_pollution_data,
)
from alerts import show_alert
from visualization import plot_traffic_map
from utils.helpers import format_time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart City Analytics",
    page_icon="🚦",
    layout="wide",
)

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f6f8;
}

.block-container {
    padding-top: 1.5rem;
}

[data-testid="metric-container"] {
    background-color: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    text-align: center;
}

h1, h2, h3 {
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🚦 Smart City Analytics Platform")
st.caption("Real-time intelligence for traffic, weather, and air quality")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🌍 City Selection")

city1 = st.sidebar.text_input("City 1", "Pune")
city2 = st.sidebar.text_input("City 2", "Lucknow")

cities = [city1, city2]

# ---------------- CACHE ----------------
@st.cache_data(ttl=180)
def load_city(city):
    weather = fetch_weather(city)
    traffic = fetch_traffic(city)
    pollution = fetch_pollution(city)

    traffic_df, future_df, flow, t_err = process_traffic_data(traffic)
    weather_data, w_err = process_weather_data(weather)
    pollution_data, p_err = process_pollution_data(pollution)

    return (
        weather_data, pollution_data, flow,
        traffic_df, future_df,
        t_err, w_err, p_err,
        traffic
    )

# ---------------- MAIN ----------------
for city in cities:

    st.divider()
    st.subheader(f"📍 {city}")

    with st.spinner("Loading data..."):
        (
            weather_data, pollution_data, flow,
            traffic_df, future_df,
            t_err, w_err, p_err,
            traffic_raw
        ) = load_city(city)

    tab1, tab2, tab3 = st.tabs(
        ["📊 Overview", "🚗 Traffic Trends", "🗺 Live Map"]
    )

    # -------- OVERVIEW --------
    with tab1:

        c1, c2, c3 = st.columns(3)

        with c1:
            if not w_err:
                st.metric("🌡 Temperature", f"{weather_data['temperature']} °C")
                st.metric("💧 Humidity", f"{weather_data['humidity']}%")

        with c2:
            if not p_err:
                st.metric("🌫 PM2.5", f"{pollution_data['pm25']} µg/m³")

        with c3:
            if not t_err:
                st.metric("🚗 Speed", f"{flow.get('currentSpeed','N/A')} km/h")
                st.metric("🛣 Free Flow", f"{flow.get('freeFlowSpeed','N/A')} km/h")

        st.divider()
        show_alert(weather_data, pollution_data, flow)

    # -------- TRAFFIC --------
    with tab2:

        if traffic_df is not None:
            st.markdown("### Live Traffic Trend")
            df_live = format_time(traffic_df.copy())
            st.line_chart(df_live.set_index("time")["speed_kmph"])

        if future_df is not None:
            st.markdown("### 30-Minute Forecast")
            df_future = format_time(future_df.copy())
            st.line_chart(df_future.set_index("time")["speed_kmph"])

    # -------- MAP --------
    with tab3:

        lat = traffic_raw.get("lat") if "error" not in traffic_raw else None
        lon = traffic_raw.get("lon") if "error" not in traffic_raw else None

        if lat and lon:
            plot_traffic_map(lat, lon, flow)
        else:
            st.warning("Map unavailable")
