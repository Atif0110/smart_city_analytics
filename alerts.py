import streamlit as st

def show_alert(weather, pollution, traffic=None):

    messages = []

    if weather:
        if weather.get("temperature", 0) > 40:
            messages.append("🔥 Extreme heat detected")
        if weather.get("humidity", 0) > 90:
            messages.append("💧 Very high humidity")

    if pollution:
        if pollution.get("pm25", 0) > 100:
            messages.append("💨 Unhealthy air quality")

    if traffic:
        if traffic.get("currentSpeed", 0) < 20:
            messages.append("🚗 Severe congestion")

    if messages:
        st.warning(" | ".join(messages))
    else:
        st.success("✅ All conditions normal")
