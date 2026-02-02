import os

# Only load .env locally
try:
    from dotenv import load_dotenv
    load_dotenv()  # Loads .env for local development
except ImportError:
    pass  # Ignore if dotenv is not installed (on Streamlit Cloud)

# Read API keys from environment variables (works locally and on Streamlit Cloud)
OPENWEATHER_KEY = os.getenv("36e241903526674f8d73881965d8c1e1")
TOMTOM_KEY = os.getenv("yJfFrSrspOxsP7RGfXeWxVa1GbgSDw0e")
WAQI_KEY = os.getenv("0cf65086093d99a6ee4278f7b902d41066d7034e")

