import time
from app.weather_data_parser import WeatherDataParser


class WeatherSDK:
    MAX_CACHE_SIZE = 10
    CACHE_EXPIRY_TIME = 600000

    def __init__(self, apiKey: str):
        self.apiKey = apiKey
        self.cache = {}

    def getWeather(self, city: str) -> dict:
        if city in self.cache:
            cachedData = self.cache[city]
            if self.current_millis() - cachedData["timestamp"] < self.CACHE_EXPIRY_TIME:
                return cachedData

        weatherData = WeatherDataParser.parseWeatherData(city, self.apiKey, self)

        if len(self.cache) >= self.MAX_CACHE_SIZE:
            oldestCity = min(self.cache, key=lambda k: self.cache[k]["timestamp"])
            del self.cache[oldestCity]

        self.cache[city] = weatherData

        return weatherData

    @staticmethod
    def current_millis() -> int:
        return int(round(time.time() * 1000))
