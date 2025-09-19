# config.py
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Read API keys from environment variables
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")
TOMTOM_KEY = os.getenv("TOMTOM_KEY")
WAQI_KEY = os.getenv("WAQI_KEY")
