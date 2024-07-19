from django import forms

from .utils import coordinates_city


class WeatherForms(forms.Form):
    """Форма для запроса города и количество дней прогноза погоды."""
    name_city = forms.CharField(label='Название города',)
    number_days = forms.IntegerField(label='Количество дней',)

    def clean(self):
        """Валидация входных данных."""
        super().clean()
        name_city = self.cleaned_data['name_city']
        number_days = self.cleaned_data['number_days']

        # проверка name_city
        rez = coordinates_city(name_city)
        if rez is None or not isinstance(name_city, str):
            raise forms.ValidationError(
                {'name_city': ('Город ведён неправильно!')}
            )

        # проверка number_days
        if (
                number_days >= 14 or
                number_days <= 0 or
                not isinstance(number_days, int)
        ):
            raise forms.ValidationError(
                {'number_days': ('Должно быдь число от 1 до 13 !')},
            )
