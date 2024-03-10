import unittest
from unittest.mock import patch
from app.weather_sdk import WeatherSDK


class TestWeatherSDK(unittest.TestCase):
    def setUp(self):
        self.apiKey = "68563960d8d155dceaa2bf642c137a4c"
        self.sdk = WeatherSDK(self.apiKey)

    @patch('app.http_utils.HttpUtils.fetchJSON')
    def test_getWeather(self, mock_fetchJSON):
        mock_fetchJSON.side_effect = [
            '[{"lat": 51.51, "lon": -0.13}]',
            '{"weather": [{"main": "Rain", "description": "light rain"}]}'
        ]

        data = self.sdk.getWeather("London")

        self.assertIn("json", data)
        self.assertIn("timestamp", data)

    @patch('app.http_utils.HttpUtils.fetchJSON')
    def test_getWeather_cityNotFound(self, mock_fetchJSON):
        mock_fetchJSON.side_effect = ['[]']

        with self.assertRaises(IOError):
            self.sdk.getWeather("NonexistentCity")


if __name__ == '__main__':
    unittest.main()
