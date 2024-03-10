# Тестовое задание в Kameleoon

**Цель тестового задания**: Создание собственного SDK для работы с [OpenWeatherMapAPI](https://openweathermap.org/).

Выбранный язык для реализации - Python.

Выполнил: [Кияшко Артём](https://hh.ru/resume/7c4c1c18ff0c7bb9430039ed1f575473717058).

## Описание проекта
Данный проект представляет собой Python SDK для работы с API OpenWeatherMap. SDK предоставляет возможность получения данных о погоде для указанного города.

## Примеры использования

### Получение данных о погоде для города

```python
from weather_sdk import WeatherSDK

apiKey = "your-api-key"
sdk = WeatherSDK(apiKey)

try:
    data = sdk.getWeather("London")
    print(data["json"])
except IOError as e:
    print(e)
```

## API Reference

### WeatherSDK

Конструктор

```python
def __init__(self, apiKey: str)
```
Создает новый объект WeatherSDK с указанным API ключом OpenWeatherMap.

Метод ``getWeather``
```python
def getWeather(self, city: str) -> dict
```
Получает данные о погоде для указанного города.

### WeatherDataParser

Метод ``parseWeatherData``

```python
def parseWeatherData(city: str, apiKey: str, sdk) -> dict
```
Парсит данные о погоде из API OpenWeatherMap для указанного города и API ключа.

### WeatherData
Конструктор
```python
def __init__(self, json: str)
```

Метод ``getJson``

```python
def getJson(self) -> str
```
Возвращает JSON представление данных о погоде.

Метод ``getTimestamp``

```python
def getTimestamp(self) -> int
```
Возвращает временную метку создания объекта WeatherData.