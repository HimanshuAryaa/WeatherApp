# 🌤️ Weather App (Python GUI Project)

A modern, elegant **Python Weather Application** built with
**CustomTkinter** and the **OpenWeather API**.\
The app provides **Current Weather**, **7-Day Forecast**, and **15-Day
Extended Forecast**, all displayed in a clean UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📌 Features

* 🔍 **City Search** - Search weather for any city worldwide
* 🌡️ **Current Weather** - Real-time temperature, humidity & weather conditions
* 📆 **7-Day Forecast** - Week-long forecast with morning, afternoon & night temperatures
* 📅 **15-Day Extended Forecast** - Two-week weather prediction
* 🎨 **Modern Dark UI** - Clean, responsive interface built with CustomTkinter
* 🔄 **Auto-Clear Display** - Smart UI that switches between single & scrollable views
* 📜 **Scrollable Results** - Easily browse through extended forecasts
* ⚙️ **API-Powered** - Live data from OpenWeather API



## 🛠️ Technologies Used

* **Python 3**
* **CustomTkinter** (Modern UI framework)
* **Requests** (HTTP API calls)
* **OpenWeather API** (Weather data provider)
* **Datetime** (Date formatting)



## 🏗️ Project Structure

```
WeatherApp/
│── weather_app.py          # Main application script
│── assets/                 # Screenshots & images
│     ├── Homepage_UI.png
│     ├── Current_Weather.png
│     ├── 7Day_Forecast.png
│     └── 15Day_Forecast.png
│── README.md              # Project documentation
```

## 🖼️ Screenshots

### 🏠 Home Page

![Homepage](assets/Homepage%20UI.png)

### 🌤️ Current Weather

![Current Weather](assets/Current%20Weather.png)

### 📆 7-Day Forecast

![7 Day Forecast](assets/7-Day%20Forecast.png)

### 📆 15-Day Extended Forecast

![15 Day Forecast](assets/15-Day%20Forecast.png)


## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenWeather API Key (free at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/HimanshuAryaa/WeatherApp.git
cd WeatherApp
```

2. **Install required dependencies:**
```bash
pip install customtkinter requests
```

3. **Get your OpenWeather API Key:**
   - Sign up at [OpenWeather](https://openweathermap.org/api)
   - Copy your API key from the dashboard

4. **Add your API key to the script:**

Open `weather_app.py` and replace the API key:
```python
API_KEY = 'your_api_key_here'
```

5. **Run the application:**
```bash
python weather_app.py
```

## 📦 Features Breakdown

### 🔹 Current Weather
Get instant weather data for any city:
- **Temperature** in Celsius
- **Humidity** percentage
- **Weather Description** (e.g., Clear sky, Cloudy, Rainy)
- **City Name** confirmation
- Clean, centered display

**Example Output:**
```
Shimla
Temp: 2.49°C
Humidity: 42%
Clear sky
```

### 🔹 7-Day Forecast
Detailed weekly forecast with three daily readings:
- **Morning Temperature** - Early day weather
- **Afternoon Temperature** - Peak day temperature
- **Night Temperature** - Evening conditions
- **Weather Description** - Daily conditions
- **Date** - Formatted as "DD Mon YYYY"

**Example Output:**
```
📌Date: 04 Dec 2024
Morning: 2.21°C
Afternoon: 12.4°C
Night: 3.08°C
Overcast clouds
```

### 🔹 15-Day Extended Forecast
Two-week weather prediction:
- Same detailed format as 7-day forecast
- Scrollable text area for easy navigation
- Perfect for trip planning
- Extended range visibility

## 🧰 How It Works

### API Flow
```
1. User enters city name
2. App requests current weather from OpenWeather API
3. Extract coordinates (lat, lon) from response
4. Use coordinates to fetch forecast data
5. Format and display results based on user selection
```

### Radio Button Options
- **Current** (0) - Shows current weather in label
- **7 Days** (1) - Shows 7-day forecast in scrollable text area
- **15 Days** (2) - Shows 15-day forecast in scrollable text area

### API Endpoints Used
```python
# Current Weather
CURRENT_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Daily Forecasts (7 & 15 days)
DAYS_URL = "https://api.openweathermap.org/data/2.5/forecast/daily"
```

## 🎨 UI Components

### Left Sidebar (180px width)
- Title label
- City input field
- Radio button selection (Current/7 Days/15 Days)
- "Get Weather" button

### Right Display Area (Expandable)
- **Result Label** - For current weather (centered)
- **Text Area** - For forecast data (scrollable)
- Smart switching between label and text area based on selection

## ⚠️ Error Handling

The app handles various error scenarios:
- ❌ Empty city input
- ❌ City not found (404 error)
- ❌ Network connection issues
- ❌ API request failures
- ❌ Invalid API responses

## 🚀 Future Improvements

* 🌡️ **Temperature Unit Toggle** - Switch between Celsius and Fahrenheit
* 🎨 **Weather Icons** - Visual weather condition icons
* 📊 **Temperature Graphs** - Chart.js integration for visual trends
* 📍 **Auto-Location** - Detect user's location automatically
* 🌙 **Light/Dark Mode** - Theme switching option
* 💾 **Favorite Cities** - Save and quick-access favorite locations
* 🔔 **Weather Alerts** - Severe weather notifications
* 🌐 **Multiple Languages** - Internationalization support
* 📱 **Responsive Design** - Better mobile/tablet layouts

## 🔧 Configuration

### Customizing the UI
You can modify these settings in `weather_app.py`:

```python
# Window size
root.geometry("700x400")

# Appearance mode
ctk.set_appearance_mode("dark")  # "light", "dark", "system"

# Color theme
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
```

### API Parameters
```python
params = {
    'q': city,           # City name
    'appid': API_KEY,    # Your API key
    'units': 'metric'    # 'metric' (Celsius) or 'imperial' (Fahrenheit)
}
```

## 📝 Code Highlights

### Date Formatting Function
```python
def format_date(unix_time):
    return datetime.fromtimestamp(unix_time).strftime("%d %b %Y")
```

### Smart UI Switching
```python
# For current weather - show label
result_label.pack(fill="both", expand=True)
text_area.pack_forget()

# For forecasts - show scrollable text area
result_label.pack_forget()
text_area.pack(side="left", fill="both", expand=True)
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Himanshu Arya**  
🔗 LinkedIn: [himanshuaryaa](https://linkedin.com/in/himanshuaryaa)  
🐙 GitHub: [HimanshuAryaa](https://github.com/HimanshuAryaa)

## 🙏 Acknowledgments

- [OpenWeather API](https://openweathermap.org/) for weather data
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern UI framework
- Python community for excellent documentation

---

⭐ **If you like this project, don't forget to star the repo!**

💬 **Found a bug or have suggestions?** Open an issue on GitHub!

---