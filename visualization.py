import streamlit as st
import pydeck as pdk

def plot_traffic_map(lat, lon, traffic_flow=None):

    # TomTom Traffic Flow Tile Layer
    TOMTOM_TILE = "https://api.tomtom.com/traffic/map/4/tile/flow/relative/{z}/{x}/{y}.png?key=yJfFrSrspOxsP7RGfXeWxVa1GbgSDw0e"

    view_state = pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=12,
        pitch=0
    )

    # Base map (clean)
    base_map = pdk.Layer(
        "TileLayer",
        data="https://c.tile.openstreetmap.org/{z}/{x}/{y}.png",
        min_zoom=0,
        max_zoom=19,
        tile_size=256,
    )

    # Traffic overlay
    traffic_layer = pdk.Layer(
        "TileLayer",
        data=TOMTOM_TILE,
        min_zoom=0,
        max_zoom=19,
        tile_size=256,
        opacity=0.7
    )

    deck = pdk.Deck(
        layers=[base_map, traffic_layer],
        initial_view_state=view_state,
        tooltip={"text": "Traffic Flow Map"}
    )

    st.pydeck_chart(deck)

