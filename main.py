import requests
from pathlib import Path
from datetime import datetime

APPID = "cf3125640bfec6ccb4f76e30231735c5"
URL_BASE = "http://api.openweathermap.org/data/2.5/onecall?"


def get_forecast(lat: float = 57.09, lon: float = 65.32,
                 appid: str = APPID, lang: str = "ru",
                 units: str = "metric", exclude: str = "hourly") -> dict:
    return requests.get(URL_BASE, params=locals()).json()


def get_pogoda(pogoda):
    daily_pogoda = pogoda.get('daily')
    day_forecast = {}
    for day in daily_pogoda:
        day_time = str(datetime.fromtimestamp(day['dt']))
        day_forecast[f'{day_time[:10]}'] = [
            f'Погода утром {int(day["temp"]["morn"])}',
            f'Погода днём {int(day["temp"]["day"])}',
            f'Погода вечером {int(day["temp"]["eve"])}',
            f'Погода ночью {int(day["temp"]["night"])}',
            f'Влажность {int(day["humidity"])}%',
            f'Ветер(Метрологические градусы) {day["wind_deg"]}',
            f'Скорость ветра м/с {day["wind_speed"]}',
            f'Небо {day["weather"][0]["description"]}',
        ]

    return day_forecast


def set_file_forecast(forestcast):
    for element in forestcast.keys():
        file_name = Path(f'day_forestcast/{element}.txt')
        file_name.touch()


def set_info_in_file_forecast(pogoda):
    for txt_file in Path('day_forestcast').glob("*.txt"):
        if txt_file.with_suffix('').name in pogoda.keys():
            stroka = ' '.join(pogoda.get(txt_file.with_suffix('').name))
            txt_file.write_text(stroka)


set_file_forecast(get_pogoda(get_forecast()))
pogoda = get_pogoda(get_forecast())
set_info_in_file_forecast(pogoda)
