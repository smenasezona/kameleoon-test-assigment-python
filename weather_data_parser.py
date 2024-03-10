import json
from http_utils import HttpUtils


class WeatherDataParser:
    @staticmethod
    def parseWeatherData(city: str, apiKey: str, sdk) -> dict:
        try:
            coordUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={apiKey}"
            coordResponse = json.loads(HttpUtils.fetchJSON(coordUrl))

            if not coordResponse:
                raise IOError("City not found")

            coordObject = coordResponse[0]
            lat = coordObject["lat"]
            lon = coordObject["lon"]

            weatherUrl = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"
            weatherResponse = HttpUtils.fetchJSON(weatherUrl)

            return WeatherDataParser.parseWeatherResponse(weatherResponse, sdk)
        except IOError as e:
            raise IOError(f"Failed to parse weather data: {e}")

    @staticmethod
    def parseWeatherResponse(response: str, sdk) -> dict:
        weatherObject = json.loads(response)
        return {"json": json.dumps(weatherObject), "timestamp": sdk.current_millis()}
