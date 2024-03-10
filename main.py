from weather_sdk import WeatherSDK

if __name__ == "__main__":
    apiKey1 = "68563960d8d155dceaa2bf642c137a4c"
    apiKey2 = "cfe6733e91a4dd47d99756ce2fd9f0b5"

    sdk1 = WeatherSDK(apiKey1)
    sdk2 = WeatherSDK(apiKey2)

    try:
        data1 = sdk1.getWeather("London")
        print(data1["json"])
    except IOError as e:
        print(e)

    try:
        data2 = sdk2.getWeather("Paris")
        print(data2["json"])
    except IOError as e:
        print(e)
