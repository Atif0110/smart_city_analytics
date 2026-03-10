🚦 Smart City Analytics Dashboard

Real-time intelligence for traffic, weather, and air quality — built with Python & Streamlit.

Show Image
Show Image
Show Image
Show Image
An interactive dashboard for city authorities and citizens to monitor live traffic conditions, environmental data, and receive instant alerts — all from a single, clean interface. Supports simultaneous comparison of two cities.

✨ Features
CategoryHighlights🚗 TrafficLive speed metrics, 30-min forecast, TomTom flow map overlay🌤 WeatherTemperature, humidity, and weather description via OpenWeatherMap🌫 Air QualityReal-time PM2.5 levels with unhealthy-air alerts🔔 AlertsAuto-triggered warnings for heat, congestion, and pollution🗺 MapsInteractive pydeck maps with live traffic tile overlay🏙 Multi-CityCompare any two cities side-by-side simultaneously

🖥 Demo
<!-- Replace with actual screenshots -->
OverviewTraffic TrendsLive Map(screenshot)(screenshot)(screenshot)

🏗 Project Structure
smart_city_analytics/
│
├── app.py               # Main Streamlit dashboard & UI layout
├── data_collection.py   # API calls: OpenWeatherMap, TomTom, WAQI
├── data_processing.py   # Data cleaning, merging, and forecasting
├── visualization.py     # pydeck traffic map rendering
├── alerts.py            # Conditional alert logic
├── config.py            # Loads API keys from .env
├── utils/
│   └── helpers.py       # Shared utility functions
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed to Git)
└── .gitignore

⚙️ Setup & Installation
Prerequisites

Python 3.8+
API keys from three free services (links below)

1. Clone the repository
bashgit clone https://github.com/Atif0110/smart_city_analytics.git
cd smart_city_analytics
2. Create and activate a virtual environment
bash# Create
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
3. Install dependencies
bashpip install -r requirements.txt
4. Configure API keys
Create a .env file in the project root:
envOPENWEATHER_KEY=your_openweather_key_here
TOMTOM_KEY=your_tomtom_key_here
WAQI_KEY=your_waqi_key_here
APIServiceFree TierOpenWeatherMapWeather + Geocoding✅ 1,000 calls/dayTomTomTraffic flow data✅ 2,500 calls/dayWAQIAir quality index✅ Unlimited
5. Run the dashboard
bashstreamlit run app.py
Open your browser at http://localhost:8501.

🔧 How It Works

Data Collection — data_collection.py fetches live data from three APIs in parallel using a shared requests.Session for efficiency.
Processing & Forecasting — data_processing.py normalizes API responses and generates a 30-minute traffic speed forecast using trend extrapolation from the current speed.
Visualization — visualization.py renders an interactive map via pydeck, layering OpenStreetMap tiles with TomTom's live traffic flow overlay.
Alerts — alerts.py evaluates thresholds (temperature > 40°C, PM2.5 > 100 µg/m³, speed < 20 km/h) and surfaces warnings in the UI.
Caching — Streamlit's @st.cache_data(ttl=180) ensures API calls are refreshed every 3 minutes, not on every interaction.


🛠 Tech Stack

Frontend — Streamlit
Maps — pydeck + OpenStreetMap + TomTom Traffic Tiles
Data — pandas, pytz
APIs — OpenWeatherMap, TomTom Traffic, WAQI Air Quality


🚀 Possible Enhancements

 Historical trend analysis with time-series storage
 Push notifications via email or Telegram
 AQI breakdown (PM10, NO₂, CO, O₃)
 Exportable PDF/CSV reports
 Multi-city ranking leaderboard


👤 Author
Atif — GitHub

📄 License
This project is licensed under the MIT License.
