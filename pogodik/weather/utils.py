import pandas as pd
import requests_cache
import openmeteo_requests
from retry_requests import retry
from geopy.geocoders import Nominatim as nom


def coordinates_city(name: str) -> dict:
    """Получение кординат по названию города."""
    geolocator = nom(user_agent='pogodik')
    location = geolocator.geocode(name)
    if location is not None:
        return {'lon': location.longitude, 'lat': location.latitude}


def weather_forecast_city(name_city: str, number_days: int) -> list:
    """Получаю с api прогноз погоды на N количество дней."""
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    location = coordinates_city(name_city)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location['lat'],
        "longitude": location['lon'],
        "hourly": "temperature_2m",
        "forecast_days": number_days,
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )}
    temp = list()
    for x in range(len(hourly_data['date'])):
        temp.append(float(hourly_temperature_2m[x]))
    return temp, hourly_data['date']
