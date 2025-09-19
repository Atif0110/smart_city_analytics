import os

# Only load .env locally
try:
    from dotenv import load_dotenv
    load_dotenv()  # Loads .env for local development
except ImportError:
    pass  # Ignore if dotenv is not installed (on Streamlit Cloud)

# Read API keys from environment variables (works locally and on Streamlit Cloud)
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")
TOMTOM_KEY = os.getenv("TOMTOM_KEY")
WAQI_KEY = os.getenv("WAQI_KEY")
