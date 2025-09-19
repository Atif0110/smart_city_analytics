# visualization.py
import streamlit as st
import pydeck as pdk
import pandas as pd

def plot_traffic_map(lat, lon, traffic_flow=None):
    """
    Display city map with subtle animated traffic heat effect.
    Congested areas appear as soft red/orange pulses.
    """
    view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=12, pitch=0)

    heat_data = []
    if traffic_flow and "currentSpeed" in traffic_flow:
        speed = traffic_flow.get("currentSpeed", 0)
        intensity = max(0, 100 - speed)  # slower speed = higher intensity
        heat_data.append({"lat": lat, "lon": lon, "intensity": intensity})

    heat_df = pd.DataFrame(heat_data)

    heat_layer = pdk.Layer(
        "HeatmapLayer",
        data=heat_df,
        get_position=["lon", "lat"],
        get_weight="intensity",
        radiusPixels=100,
        intensity=0.6,
        threshold=0.3
    )

    r = pdk.Deck(
        layers=[heat_layer],
        initial_view_state=view_state,
        map_style="light"
    )

    st.pydeck_chart(r)
