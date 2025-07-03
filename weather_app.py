import customtkinter as ctk
import requests

Api_key= "00aa306c3e2f8a8e243b682d942797a8"

def clear_window():
    for widget in app.winfo_children():
        widget.destroy()

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.configure(text="please enter a valid city")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            result = f"🌡 Temp: {temp}°C\n☁ Weather: {weather}\n💧 Humidity: {humidity}%"
        else:
            result = f"City not found ❌"

        result_label.configure(text=result)
    except Exception as e:
        result_label.configure(text="Error retrieving data.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Weather App")
app.geometry("500x500")

title = ctk.CTkLabel(app, text="🌤 Weather App", font=("Arial", 20))
title.pack(pady=10)

city_entry = ctk.CTkEntry(app, width=450, placeholder_text="Enter city name")
city_entry.pack(pady=10)

search_button = ctk.CTkButton(app, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14), justify="left")
result_label.pack(pady=10)

app.mainloop()
