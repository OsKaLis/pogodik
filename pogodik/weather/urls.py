from django.urls import path

from . import views

app_mame = 'weather'

urlpatterns = [
    path('', views.showing_weather_forecast, name='showing_weather_forecast'),
]