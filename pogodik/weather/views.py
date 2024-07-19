from django.shortcuts import render

from .forms import WeatherForms
from .utils import weather_forecast_city


def showing_weather_forecast(request):
    """Прогнос погоды на заданое число дней."""
    form = WeatherForms(request.GET or None)
    context = {'form': form}
    result = dict()
    if form.is_valid():
        result['name_city'] = form.cleaned_data['name_city']
        result['number_days'] = form.cleaned_data['number_days']
        result['temp'], result['time'] = weather_forecast_city(
            result['name_city'], result['number_days']
        )
        context['result'] = result
    template = 'weather/showing_weather.html'
    return render(request, template, context)
