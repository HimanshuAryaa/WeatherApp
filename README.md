# 🌤️ Weather App (Python GUI Project)

A modern, elegant **Python Weather Application** built with
**CustomTkinter** and the **OpenWeather API**.\
The app provides **Current Weather**, **7-Day Forecast**, and **15-Day
Extended Forecast**, all displayed in a clean UI.

------------------------------------------------------------------------

## 📌 Features

-   🔍 Search weather by city name
-   🌡️ Current Temperature, Humidity & Conditions
-   📆 7-Day Forecast (Morning, Afternoon, Night temperatures)
-   📆 15-Day Extended Forecast
-   🎨 Modern Dark UI made with CustomTkinter
-   🧹 Auto-clear & responsive UI
-   🖼️ Scrollable forecast section (for long results)
-   ⚙️ API-powered dynamic weather data

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python 3**
-   **CustomTkinter (Modern UI)**
-   **Requests (API Calls)**
-   **OpenWeather API**
-   **Pillow (for icons/images if used)**

------------------------------------------------------------------------

## 🏗️ Project Structure

    WeatherApp/
    │── weather_app.py          # Main GUI script
    │── assets/
    │     ├── Homepage UI.png
    │     ├── Current Weather.png
    │     ├── 7-Day Forecast.png
    │     ├── 15-Day Forecast.png
    │── README.md

------------------------------------------------------------------------

## 🖼️ Screenshots

### 🏠 Home Page

![Homepage](assets/Homepage%20UI.png)

### 🌤️ Current Weather

![Current Weather](assets/Current%20Weather.png)

### 📆 7-Day Forecast

![7 Day Forecast](assets/7-Day%20Forecast.png)

### 📆 15-Day Extended Forecast

![15 Day Forecast](assets/15-Day%20Forecast.png)

------------------------------------------------------------------------

## 🚀 How to Run

1.  Clone the repository:

    ``` bash
    git clone https://github.com/HimanshuAryaa/WeatherApp.git
    cd WeatherApp
    ```

2.  Install dependencies:

    ``` bash
    pip install customtkinter requests pillow
    ```

3.  Add your **OpenWeather API Key** inside the script:

    ``` python
    API_KEY = "your_api_key_here"
    ```

4.  Run the application:

    ``` bash
    python weather_app.py
    ```

------------------------------------------------------------------------

## 📦 Features Breakdown

### 🔹 Current Weather

Shows: - Temperature
- Humidity
- Weather Conditions
- Clean center-aligned display

### 🔹 7-Day Forecast

-   Daily breakdown
-   Morning / Afternoon / Night temperatures
-   Weather description

### 🔹 15-Day Forecast

-   Extended range
-   Scrollable list
-   Detailed daily temperature values

------------------------------------------------------------------------

## 🧰 Example API Flow

    Enter City: Shimla

    Current Weather:
    Temp: 2.49°C
    Humidity: 42%
    Clear sky

7-Day Forecast Example:

    Date: 04 Dec 2025
    Morning: 2.21°C
    Afternoon: 12.4°C
    Night: 3.08°C
    Overcast clouds

------------------------------------------------------------------------
## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.x-blue)
![API](https://img.shields.io/badge/API-OpenWeather-blue)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-lightgrey)
![Platform](https://img.shields.io/badge/OS-Windows%20%7C%20Linux-blue)

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add weather icons
-   Add weekly chart graphs
-   Add temperature unit switch (°C / °F)
-   Add location auto-detection

------------------------------------------------------------------------

## 👨‍💻 Author

**Himanshu Arya**\
🔗 LinkedIn: https://linkedin.com/in/himanshuaryaa \
🐙 GitHub: https://github.com/HimanshuAryaa

------------------------------------------------------------------------

## ⭐ If you like this project, don't forget to star the repo!
