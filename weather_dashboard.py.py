# Weather Forecast Visualization using OpenWeatherMap API

import requests
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Set Seaborn theme for better visuals
sns.set_theme(style="darkgrid")



# API Configuration
api_key = 'f7ef261bd1ae619b759db68550ef4a0c'
city = 'Hyderabad'
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

# Fetch Data from OpenWeatherMap API
response = requests.get(url)
data = response.json()

# Check if the API call was successful
if response.status_code == 200:
    # Extract Data for Plotting
    dates = []
    temperatures = []
    humidity = []
    weather_description = []

    for forecast in data['list']:
        dates.append(forecast['dt_txt'])
        temperatures.append(forecast['main']['temp'])
        humidity.append(forecast['main']['humidity'])
        weather_description.append(forecast['weather'][0]['description'])

    # 🌡️ Temperature over Timeline Graph
    plt.figure(figsize=(14, 6))
    sns.lineplot(x=dates, y=temperatures, marker='o')
    plt.xticks(rotation=45)
    plt.title(f'Temperature Forecast for {city}')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.tight_layout()
    plt.show()

    # 💧 Humidity over Timeline Graph
    plt.figure(figsize=(14, 6))
    sns.lineplot(x=dates, y=humidity, color='blue', marker='o')
    plt.xticks(rotation=45)
    plt.title(f'Humidity Forecast for {city}')
    plt.xlabel('Date and Time')
    plt.ylabel('Humidity (%)')
    plt.tight_layout()
    plt.show()

    # 🌥️ Weather Description Bar Chart
    desc_counts = Counter(weather_description)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(desc_counts.keys()), y=list(desc_counts.values()))
    plt.title(f'Weather Description Count in Forecast for {city}')
    plt.xlabel('Weather Condition')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("Failed to fetch data. Check your API key and city name.")
