# 🚦 Smart City Analytics Dashboard – Pro Version

An **interactive, real-time Smart City Dashboard** for monitoring traffic, weather, and air pollution. Built for city authorities and citizens, it helps visualize traffic flow, forecast speeds, monitor environmental conditions, and receive alerts—all in a clean, user-friendly interface.

---

## 🌟 Features

### **Traffic**
- Live traffic maps with animated heat effects for congestion.
- Real-time traffic speed graph updating every 10 seconds.
- 30-minute traffic speed forecast based on current trends.
- Side-by-side city comparison: monitor two cities at once.
- Color gradients indicate traffic intensity (moderate/high congestion).

### **Weather**
- Displays temperature, humidity, and weather description.
- City-wise side-by-side comparison.

### **Air Pollution**
- Real-time AQI display.
- PM2.5 levels for each city.
- Alerts for unhealthy pollution levels.

### **Alerts & Notifications**
- Dynamic alerts at the bottom of the dashboard.
- Triggers for extreme weather, traffic congestion, or high pollution.
- No alert shown if all conditions are normal.

### **Maps**
- Clean, interactive maps without unnecessary markers or grids.
- Subtle animated traffic heat overlay.
- Optimized for fast loading and smooth performance.

### **Other Enhancements**
- Two-city layout: first city on top, second below.
- Optimized API calls for faster data fetching.
- Interactive, visually appealing charts and heatmaps.

---

## 📷 Screenshots
*(Add screenshots after running the app)*  

- Dashboard overview  
- Real-time traffic heat animation  
- Pollution & Weather summary  
- Alerts panel  

---

## ⚙️ Installation & Setup

### **1. Clone the repository**
```bash
git clone https://github.com/Atif0110/smart_city_analytics.git
cd smart_city_analytics

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Create a .env file in the root and add your API keys:
OPENWEATHER_KEY=your_openweather_key_here
TOMTOM_KEY=your_tomtom_key_here
WAQI_KEY=your_waqi_key_here


Running the App
streamlit run app.py




Project Structure

smart_city_analytics/
│
├── app.py                  # Main Streamlit dashboard
├── data_collection.py      # Fetch live traffic, weather, and pollution data
├── data_processing.py      # Clean, merge, and forecast data
├── visualization.py        # Charts and heatmaps
├── alerts.py               # Dynamic alerts based on conditions
├── utils/helpers.py        # Helper functions
├── requirements.txt        # Python dependencies
├── config.py               # Reads API keys from .env
├── .env                    # API keys (ignored in GitHub)
├── .gitignore              # Ignored files


