# 🚦 Smart City Analytics Dashboard

> Real-time intelligence for traffic, weather, and air quality — built with Python & Streamlit.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

An interactive dashboard for city authorities and citizens to monitor live traffic conditions, environmental data, and receive instant alerts — all from a single, clean interface. Supports simultaneous comparison of two cities.

---

## ✨ Features

| Category | Highlights |
|---|---|
| 🚗 **Traffic** | Live speed metrics, 30-min forecast, TomTom flow map overlay |
| 🌤 **Weather** | Temperature, humidity, and weather description via OpenWeatherMap |
| 🌫 **Air Quality** | Real-time PM2.5 levels with unhealthy-air alerts |
| 🔔 **Alerts** | Auto-triggered warnings for heat, congestion, and pollution |
| 🗺 **Maps** | Interactive pydeck maps with live traffic tile overlay |
| 🏙 **Multi-City** | Compare any two cities side-by-side simultaneously |

---

## 🖥 Demo

<!-- Replace with actual screenshots -->
| Overview | Traffic Trends | Live Map |
|---|---|---|
| _(screenshot)_ | _(screenshot)_ | _(screenshot)_ |

---

## 🏗 Project Structure
```
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
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- API keys from three free services (links below)

### 1. Clone the repository
```bash
git clone https://github.com/Atif0110/smart_city_analytics.git
cd smart_city_analytics
```

### 2. Create and activate a virtual environment
```bash
# Create
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:
```env
OPENWEATHER_KEY=your_openweather_key_here
TOMTOM_KEY=your_tomtom_key_here
WAQI_KEY=your_waqi_key_here
```

| API | Service | Free Tier |
|---|---|---|
| [OpenWeatherMap](https://openweathermap.org/api) | Weather + Geocoding | ✅ 1,000 calls/day |
| [TomTom](https://developer.tomtom.com/) | Traffic flow data | ✅ 2,500 calls/day |
| [WAQI](https://aqicn.org/api/) | Air quality index | ✅ Unlimited |

### 5. Run the dashboard
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## 🔧 How It Works

1. **Data Collection** — `data_collection.py` fetches live data from three APIs using a shared `requests.Session` for efficiency.
2. **Processing & Forecasting** — `data_processing.py` normalizes API responses and generates a 30-minute traffic speed forecast via trend extrapolation.
3. **Visualization** — `visualization.py` renders an interactive map via `pydeck`, layering OpenStreetMap tiles with TomTom's live traffic flow overlay.
4. **Alerts** — `alerts.py` evaluates thresholds (temperature > 40°C, PM2.5 > 100 µg/m³, speed < 20 km/h) and surfaces warnings in the UI.
5. **Caching** — Streamlit's `@st.cache_data(ttl=180)` ensures API calls refresh every 3 minutes, not on every interaction.

---

## 🛠 Tech Stack

- **Frontend** — [Streamlit](https://streamlit.io/)
- **Maps** — [pydeck](https://deckgl.readthedocs.io/) + OpenStreetMap + TomTom Traffic Tiles
- **Data** — pandas, pytz
- **APIs** — OpenWeatherMap, TomTom Traffic, WAQI Air Quality

---

## 🚀 Possible Enhancements

- [ ] Historical trend analysis with time-series storage
- [ ] Push notifications via email or Telegram
- [ ] AQI breakdown (PM10, NO₂, CO, O₃)
- [ ] Exportable PDF/CSV reports
- [ ] Multi-city ranking leaderboard

---

## 👤 Author

**Atif** — [GitHub](https://github.com/Atif0110)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
