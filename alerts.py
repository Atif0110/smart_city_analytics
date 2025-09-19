# alerts.py
import streamlit as st

def show_alert(weather, pollution, traffic=None):
    messages = []

    if weather:
        if weather.get("temperature", 0) > 40:
            messages.append("⚠️ High temperature!")
        if weather.get("humidity", 0) > 90:
            messages.append("⚠️ High humidity!")

    if pollution:
        if pollution.get("pm25", 0) > 100:
            messages.append("⚠️ PM2.5 pollution high!")

    if traffic:
        if traffic.get("currentSpeed", 0) < 20:
            messages.append("⚠️ Heavy traffic congestion!")

    if messages:
        st.warning(" | ".join(messages))
    else:
        st.success("✅ All conditions normal")
