import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")
TOMTOM_KEY = os.getenv("TOMTOM_KEY")
WAQI_KEY = os.getenv("WAQI_KEY")
