<div id="header" align="center">
  <h1>Pogodik</h1>
</div>

> [!NOTE]
> ##	Проект магазина продуктов со следующим функционалом:
*	Cайт, где пользователь вводит название города,
*   и получает прогноз погоды в этом городе на ближайшее время от 1 до 13 дней.

### Cтек технологий:
![Python 3.12](https://img.shields.io/badge/Python-3.12-brightgreen.svg?style=flat&logo=python&logoColor=white)
![Django 3.2.16](https://img.shields.io/badge/Django-3.2.16-brightgreen.svg?style=flat&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-22.2-%238511FA.svg?style=flat&logo=bootstrap&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.2.2-%23150458.svg?style=flat&logo=pandas&logoColor=white)
<img src="https://img.shields.io/badge/geopy-2.4.1-black">
![NumPy](https://img.shields.io/badge/numpy-2.0.0-%23013243.svg?style=flat&logo=numpy&logoColor=white)
<img src="https://img.shields.io/badge/retry--requests-2.0.0-black">
<img src="https://img.shields.io/badge/python--dotenv-1.0.1-black">
<img src="https://img.shields.io/badge/openmeteo--requests-1.2.0-black">
<img src="https://img.shields.io/badge/requests--cache-1.2.1-black">

### Запуск
* [0] (Клонируем проект):git clone git@github.com:OsKaLis/pogodik.git
* [1] cd pogodik
* [2] (Создание файла с настройками ".env"):
>   ```
>   SECRET_KEY=[{Своё значение key}]
>   DEBUG=True
>   ```
* [3] (Запускаем виртуальное окружение):poetry shell
* [4] (Устанавливаем установка зависимости для окружения):poetry install
* [5] (перейти в каталог): cd pogodik
* [6] (Применить структуру): python manage.py migrate
* [8] (Запуск приложение): python manage.py runserver

### Дальнейшие планы в разработке
* написаны тесты
* Помстить в докер контейнер
* Сделаны автодополнение (подсказки) при вводе города
* при повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее
* будет сохраняться история поиска для каждого пользователя, и будет API, показывающее сколько раз вводили какой город

### Автор: Юшко Ю.Ю.
