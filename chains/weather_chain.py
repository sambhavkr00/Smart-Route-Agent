import requests
from utils.api_keys import OPENWEATHERMAP_API_KEY
from datetime import datetime

def get_weather_forecast(destination, date):
    url = f"http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": destination,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return "Error fetching weather"

    forecasts = response.json().get("list", [])
    # Filter forecasts for the requested date
    target_date = date.strip()
    filtered = [f for f in forecasts if f['dt_txt'].startswith(target_date)]
    if not filtered:
        return f"No weather data available for {target_date}"
    summary = []
    for f in filtered:
        summary.append(f"{f['dt_txt']}: {f['weather'][0]['description']}, Temp: {f['main']['temp']}°C")
    # print(summary)
    return "\n".join(summary)
