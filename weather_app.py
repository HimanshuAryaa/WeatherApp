import customtkinter as ctk
from tkinter import IntVar
import requests
from datetime import datetime

API_KEY = 'your_api_key_here'
CURRENT_URL = 'https://api.openweathermap.org/data/2.5/weather'
DAYS_URL = "https://api.openweathermap.org/data/2.5/forecast/daily"

def format_date(unix_time):
    return datetime.fromtimestamp(unix_time).strftime("%d %b %Y")

def get_weather():
    result_label.configure(text="")
    text_area.delete(1.0, "end")

    choice = x.get()
    city = city_entry.get()

    if not city:
        result_label.configure(text="Please enter a city name")
        return

    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}

    try:
        response = requests.get(CURRENT_URL, params=params)
        data = response.json()

        if data.get('cod') != 200:
            result_label.configure(text="Sorry, we couldn't find that city")
            return

        lat = data['coord']['lat']
        lon = data['coord']['lon']

        # ---------------- CURRENT WEATHER ----------------
        if choice == 0:
            text_area.pack_forget()
            result_label.pack(fill="both", expand=True)

            name = data["name"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"].capitalize()

            info = f"{name}\nTemp: {temp}°C\nHumidity: {humidity}%\n{desc}"
            result_label.configure(text=info)

        # ---------------- 7 DAYS ----------------
        elif choice == 1:
            result_label.pack_forget()
            text_area.pack(side="left", fill="both", expand=True)

            params = {'lat': lat, 'lon': lon, 'cnt': 7, 'appid': API_KEY, 'units': 'metric'}
            data = requests.get(DAYS_URL, params=params).json()

            text_area.insert("end", "📅 Extended 7-Day Forecast\n\n")

            for day in data['list']:
                date = format_date(day['dt'])
                desc = day['weather'][0]['description'].capitalize()
                t = (
                    f"📌Date: {date}\n"
                    f"Morning: {day['temp']['morn']}°C\n"
                    f"Afternoon: {day['temp']['day']}°C\n"
                    f"Night: {day['temp']['night']}°C\n"
                    f"{desc}\n\n"
                )
                text_area.insert("end", t)

        # ---------------- 15 DAYS ----------------
        elif choice == 2:
            result_label.pack_forget()
            text_area.pack(side="left", fill="both", expand=True)

            params = {'lat': lat, 'lon': lon, 'cnt': 15, 'appid': API_KEY, 'units': 'metric'}
            data = requests.get(DAYS_URL, params=params).json()

            text_area.insert("end", "📅 Extended 15-Day Forecast\n\n")

            for day in data['list']:
                date = format_date(day['dt'])
                desc = day['weather'][0]['description'].capitalize()
                t = (
                    f"📌Date: {date}\n"
                    f"Morning: {day['temp']['morn']}°C\n"
                    f"Afternoon: {day['temp']['day']}°C\n"
                    f"Night: {day['temp']['night']}°C\n"
                    f"{desc}\n\n"
                )
                text_area.insert("end", t)

    except requests.exceptions.RequestException:
        result_label.configure(text="Error: Cannot connect to server")

    except Exception as e:
        result_label.configure(text=f"An error occurred: {e}")


# ---------------- UI ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Weather App")
root.geometry("700x400")
root.resizable(False, False)

# LEFT BAR
left_frame = ctk.CTkFrame(root, width=180, corner_radius=0)
left_frame.pack(side="left", fill="y")

title = ctk.CTkLabel(left_frame, text="Weather App", font=("Segoe UI", 22, "bold"))
title.pack(pady=15)

city_entry = ctk.CTkEntry(left_frame, placeholder_text="Enter city", font=("Segoe UI", 15))
city_entry.pack(pady=10, padx=20, fill="x")

options = ["Current", "7 Days", "15 Days"]
x = IntVar()

radio_frame = ctk.CTkFrame(left_frame)
radio_frame.pack(pady=10, padx=10, fill="x")

for i, opt in enumerate(options):
    r = ctk.CTkRadioButton(radio_frame, text=opt, variable=x, value=i)
    r.pack(anchor="w", pady=4)

btn = ctk.CTkButton(left_frame, text="Get Weather", command=get_weather, font=("Segoe UI", 14))
btn.pack(pady=15)

# RIGHT SIDE
right_frame = ctk.CTkFrame(root)
right_frame.pack(side="left", fill="both", expand=True)

result_label = ctk.CTkLabel(right_frame, text="", font=("Segoe UI", 16), justify="center")
result_label.pack(pady=10, padx=10, fill="both")

text_area = ctk.CTkTextbox(right_frame, font=("Segoe UI", 13))
text_area.pack_forget()

root.mainloop()