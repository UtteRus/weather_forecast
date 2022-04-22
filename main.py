import requests
from pathlib import Path
from datetime import datetime

APPID = "cf3125640bfec6ccb4f76e30231735c5"
URL_BASE = "http://api.openweathermap.org/data/2.5/onecall?"


def get_forecast(lat: float = 57.09, lon: float = 65.32,
                 appid: str = APPID, lang: str = "ru",
                 units: str = "metric", exclude: str = "hourly") -> dict:
    return requests.get(URL_BASE, params=locals()).json()


pogoda = get_forecast()


def get_pogoda(pogoda):
    daily_pogoda = pogoda.get('daily')
    day_forecast = {}
    for day in daily_pogoda:
        day_time = datetime.fromtimestamp(day['dt'])

        day_forecast[f'{day_time}'] = [
            f'Погода утром {int(day["temp"]["morn"])}',
            f'Погода днём {int(day["temp"]["day"])}',
            f'Погода вечером {int(day["temp"]["eve"])}',
            f'Погода ночью {int(day["temp"]["night"])}',
            f'Влажность {int(day["humidity"])}%',
            f'Ветер(Метрологические градусы) {day["wind_deg"]}',
            f'Скорость ветра м/с {day["wind_speed"]}',
            f'Небо {day["weather"][0]["description"]}',
        ]

    print(day_forecast)


get_pogoda(pogoda)
